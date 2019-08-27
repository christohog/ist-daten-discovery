#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prior to this script, archives files from the Ist-Daten from the SBB (Swiss Federal Rails)
need to be downloaded. The data is described here in german : https://opentransportdata.swiss/dataset/istdaten
The archived files can then be downloaded here : https://drive.google.com/drive/folders/1SVa68nJJRL3qgRSPKcXY7KuPN9MuHVhJ
Every archived files contains a month of data. There exist a csv file for every day in the month.
For exemple the file 19_6.zip will contain following files : 
- 2019-06-01_IstDaten.csv
- 2019-06-02_IstDaten.csv
- ...
- 2019-06-30_IstDaten.csv
Every csv files is approximatively 500 MB.

This script unzip files and processes+parses every csv that it finds (one for each day). 
It builds a big dataframe that enables
with selected data. For 12 months of data (12 zip files), from 2018-07-01 to 2019-06-30,
the obtained dataframe was approx. 500 MB, saved in a pkl file.
"""

import datetime as dt
import numpy as np
import pandas as pd
import zipfile
import glob

# Where are the zip files downloaded
project_path = '/Provide_here_the_folder_with_files'

# Initialize data_tot
data_tot = pd.DataFrame()

# Find all zip files and loop over them
for m in glob.glob(project_path+"/data/*.zip"):
    # Get zip file of year m
    with zipfile.ZipFile(m, 'r') as z:
        for file in z.namelist():
            # Following file has a different encoding
            if file=='18_11/2018-11-02istdaten.csv':
                encoding = "ISO-8859-1"
            # Ignore files that are not csv or if they start with the MACOSX prefix
            elif file[-4:]!='.csv' or '__MACOSX' in file:
                print('FILE IS NOT A CSV')
                continue
            else:
                encoding = "utf-8"
                
            #print(f)
            with z.open(file) as f:
                print(file)
                data_raw = pd.read_csv(f, sep=";",encoding = encoding)
                print(' --> loaded successfully.')
                data_all = data_raw[['BETRIEBSTAG',
                                     'BETREIBER_ABK',
                                     'PRODUKT_ID',
                                     'LINIEN_TEXT',
                                     #'UMLAUF_ID',
                                     'VERKEHRSMITTEL_TEXT',
                                     'ZUSATZFAHRT_TF',
                                     'FAELLT_AUS_TF',
                                     'HALTESTELLEN_NAME',
                                     'ANKUNFTSZEIT',
                                     'AN_PROGNOSE',
                                     'AN_PROGNOSE_STATUS',
                                     'ABFAHRTSZEIT',
                                     'AB_PROGNOSE',
                                     'AB_PROGNOSE_STATUS',
                                     'DURCHFAHRT_TF']]
                
                # Keep only train information
                data = data_all[data_all['PRODUKT_ID']=='Zug']
                # Keep only SBB trains
                data = data[data['BETREIBER_ABK']=='SBB']
                # Keep only train IC, RE, IR and R
                data = data[data['VERKEHRSMITTEL_TEXT'].isin(['IC','RE','IR'])]
                # Create IS_LATE column
                data['DELAY_AN'] = pd.to_datetime(data['AN_PROGNOSE'],format="%d.%m.%Y %H:%M:%S") - pd.to_datetime(data['ANKUNFTSZEIT'],format="%d.%m.%Y %H:%M")
                data['DELAY_AB'] = pd.to_datetime(data['AB_PROGNOSE'],format="%d.%m.%Y %H:%M:%S") - pd.to_datetime(data['ABFAHRTSZEIT'],format="%d.%m.%Y %H:%M")
                
                data = data.drop(['BETREIBER_ABK','PRODUKT_ID'],axis = 1)
                
                data_tot = data_tot.append(data)
                
# Save data in pickle file
data_tot.to_pickle('data_clean_201807-201906.pkl')
                