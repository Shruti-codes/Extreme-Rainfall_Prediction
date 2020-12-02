# Extreme-Rainfall_Prediction
CS685 Data Mining Project

#Data Collection

Step 1) Get weather variables from : 1) https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.surface.html   <- at surface level and multiple levels

Step 2) Get Gridded Rainfall (1.0 x 1.0) NetCDF File (y-value) from : http://imdpune.gov.in/Clim_Pred_LRF_New/Grided_Data_Download.html

#Data Processing

Step 3) Run nc.py for all datafiles (change file names as per the years). (for each year individually)

Step 4) Run combine.py on the extracted csv files. (for each year individually)

Step 5) Run data_prep.py on the output files of Step 4 to get gridwise combined file (columns = 22\*225\*2\+3 = 9903)

Step 6) Run nc-rainfall.py on files downloaded in Step 2 (change years, latitude/longitude of region and filenames according to the ones you need) to get the amount of rainfall in that particular region across those years. This is used for next 48 hour prediction.

Step 7) Run data_prep_24.py on files downloaded in Step 2 (change years, latitude/longitude of region and filenames according to the ones you need) to get the amount of rainfall in that particular region across those years. This is used for next 24 hour prediction.


Website (in progress) : https://shruti-codes.github.io/ExtremeRainfall/landingpage.html
