

import feather

file_location = "/home/xps/Desktop/schrute.feather"  # actual source of the df is in R file: 'source.R'
schrute = feather.read_dataframe(file_location)

