# SBB Train delay
Discovery of a dataset from the Swiss Federal Railway company (SBB).
Lots of open source data published on their platform : https://data.sbb.ch/pages/home/

This project is looking into the the ist-daten (actual data) which contains information about every stop made by every public transport in Switzerland for a given date. Daily datasets are published early in the morning (Zurich/Europe time) for the previous day.

- Ist-Daten sample : https://opentransportdata.swiss/dataset/istdaten
- Archives : https://drive.google.com/drive/folders/1SVa68nJJRL3qgRSPKcXY7KuPN9MuHVhJ

# Blog 
https://medium.com/@christopher.hogendijk/sbb-trains-delay-4b1e23f3bd15

## Files 
1. data_discovery_entire_SET.ipynb
	- file to discover the content of the ist-daten data from SBB. Look at one sample file for a single day (needs to be downloaded prior to running the script, approx 500 MB). 
2. unzip_files.py
	- unzip and preprocess archive files to have one year of data. Outcome can then be used in the third file for a deeper analysis.
3. data_discovery_ZugSBB.ipynb
	- analysis of the actual data of trains in Switzerland. First steps of this discovery work was to look into the delays and try to output some interesting statistics about it.
	
	