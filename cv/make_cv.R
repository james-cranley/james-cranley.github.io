#Load packages
#devtools::install_github("nstrayer/datadrivencv",force=TRUE)

library(datadrivencv)

# run use_datadriven_cv()
datadrivencv::use_datadriven_cv(full_name = "James Cranley",
data_location = "https://docs.google.com/spreadsheets/d/1FDKosbW_bC9WvQKVsqhHbHmzXRIXS0sBUvE8cBBl2Ww/edit#gid=917338460",
pdf_location = "https://james-cranley.github.io/cranley_cv.pdf",
html_location = "https://james-cranley.github.io/cranley_cv.html",
source_location = "/Users/jc48/Documents/GitHub/james-cranley.github.io/cv/")


