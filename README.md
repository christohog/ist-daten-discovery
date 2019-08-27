# SBB Train delay
Discovery of a dataset from the Swiss Federal Railway company (SBB).
Lots of open source data published on their platform : https://data.sbb.ch/pages/home/

This project is looking into the the ist-daten (actual data) which contains information about every stop made by every public transport in Switzerland for a given date. Daily datasets are published early in the morning (Zurich/Europe time) for the previous day.

- Ist-Daten sample : https://opentransportdata.swiss/dataset/istdaten
- Archives : https://drive.google.com/drive/folders/1SVa68nJJRL3qgRSPKcXY7KuPN9MuHVhJ

## Why ?
Motivation behind this exploratory work was to dig into one of the numerous dataset of the SBB, in this case about delays, and find out interesting statistics about it.
Only some types of transports were selected, long-distant trains operated by SBB, to diminish the number of entries (3.6 millions records for July 2018 to June 2019).
Questions such as what are the most frequented stations and which of them are mostly affected by delays are answered.

## Blog 
https://medium.com/@christopher.hogendijk/sbb-trains-delay-4b1e23f3bd15

## Files 
1. data_discovery.ipynb
	- file to discover the content of the ist-daten data from SBB. Look at one sample file for a single day (needs to be downloaded prior to running the script, approx 500 MB). 
2. preprocess_data.py
	- unzip and preprocess archive files to have one year of data. Outcome can then be used in the third file for a deeper analysis.
3. data_analysis.ipynb
	- analysis of the actual data of trains in Switzerland. This discovery work looks into the delays and try to output some interesting statistics about it.	
	
## Installations 
Whole project was done using python 3, either in juypter notebooks or python file (for the preprocessing of the archive files, which takes approx. 1 hour on a macbook pro 2013).
No special installations required besides the normal data science library. Given the size of the datasets, datasets have to be downloaded prior to runnign the scripts by the users (as described in section "Files")

## Conclusion
This explanatory work has shown that it is possible to get good insights and interesting statistics out of the actual data from SBB. However, several steps of filtering and reducting the data size are absolutely mandatory to be able to naviguate in these GB of data to make some sense out of it.
While Zurich was without surprises the mostly frequented stations, we found otu that Bern and Olten are the ones most often affected by delays.
	
## Acknowledgments
Very gratefull to the SBB in general for the amazing rail service they provide in Switzerland, and in this case for giving the possibility to work with their open source data. (Licence https://data.sbb.ch/page/licence/)