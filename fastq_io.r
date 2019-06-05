#install.packages('tidyverse')
library(tidyverse)

#This data is from a Thermo Ion S5 sequencer. 
#Metabarcoding data from a malaise trap ontario provincial parks dataset
data = readFastq('/home/cnuge/Documents/barcode_data/mBRAVE_raw_read_data/GMP-03299)CCDB-S5-0084)CBGMB-00030.fastq')

#on server
#data = readFastq('/home/cnugent/barcode_data/mBRAVE_raw_read_data/GMP-04500)CCDB-S5-0084)CBGMB-00030.fastq')

head(data)
names(data)


#try to dereplicate these reads

#get the 
