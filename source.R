library(schrute)
library(feather)

df <- schrute::theoffice

feather::write_feather(df, "~/Desktop/schrute.feather")
  write.csv(df, "~/Desktop/schrute.csv")
