## this code downloads the latest list of my publications and pulls doi numbers and other others. Feed this into the my_cv_data google sheet and then re-run 'render_cv.r'

import pandas as pd
import requests
import json

_id="0000-0002-0408-5801"

r = requests.get(f"https://pub.orcid.org/v3.0/{_id}/works",
                headers = {'User-Agent':'Mozilla/5.0', 'accept' : 'application/json'})
r=r.json()

titles=[]
journals=[]
years=[]
doi_URLs=[]
dois=[]
author_names=[]


for work in range(len(r['group'])):
    titles.append(r['group'][work]['work-summary'][0]['title']['title']['value'])
    journals.append(r['group'][work]['work-summary'][0]['journal-title']['value'])
    years.append(r['group'][work]['work-summary'][0]['publication-date']['year']['value'])
    
    for ext_id in range(len(r['group'][work]['work-summary'][0]['external-ids']['external-id'])):
        if r['group'][work]['work-summary'][0]['external-ids']['external-id'][ext_id]['external-id-type']=='doi':
            doi_URLs.append(r['group'][work]['work-summary'][0]['external-ids']['external-id'][ext_id]['external-id-url']['value'])
            dois.append(r['group'][work]['work-summary'][0]['external-ids']['external-id'][ext_id]['external-id-value'])
            
for doi in dois:
    doi_r = requests.get(f"https://api.crossref.org/works/{doi}",headers = {'User-Agent':'Mozilla/5.0', 'accept' : 'application/json'})
    doi_r=doi_r.json()

    author_names_for_each_doi=[]

    for author in range(len(doi_r['message']['author'])):
        author_names_for_each_doi.append(doi_r['message']['author'][author]['given']+" "+doi_r['message']['author'][author]['family'])
    
    author_names_for_each_doi=", ".join(str(x) for x in author_names_for_each_doi)
    author_names.append(author_names_for_each_doi)

out_dict={
    'titles':titles,
    'journals':journals,
    'years':years,
    'doi_URLs':doi_URLs,
    'dois':dois,
    'author_names':author_names
    }

df=pd.DataFrame(out_dict)
df.to_csv('works.csv',index=False)
df