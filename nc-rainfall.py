from netCDF4 import Dataset
from netCDF4 import num2date
import numpy as np
import os
import pandas as pd
files=['2013/RFone_imd_rf_1x1_2013.nc','2014/RFone_imd_rf_1x1_2014.nc','2015/RFone_imd_rf_1x1_2015.nc','2016/RFone_imd_rf_1x1_2016.nc']
emptydf=pd.DataFrame()
for item in files:
    data = Dataset(item,mode='r',format='NETCDF4')
    fname=item.split(".")[0]
    fyr=fname.split("_")[-1]
    startdate=fyr+'-06-01'
    enddate=fyr+'-09-31'
    vin =data.variables['rf']
    time_dim, lat_dim, lon_dim = vin.get_dims()

    time_var = data.variables[time_dim.name]
    times = num2date(time_var[:], time_var.units)
    latitudes = data.variables[lat_dim.name][:]
    longitudes = data.variables[lon_dim.name][:]

    times_grid, latitudes_grid, longitudes_grid = [x.flatten() for x in np.meshgrid(times, latitudes, longitudes, indexing='ij')]
    df = pd.DataFrame({
        'time': [t.isoformat() for t in times_grid],
        'latitude': latitudes_grid,
        'longitude': longitudes_grid,
        'rf': vin[:].flatten()})


    df=df.loc[(df['latitude']==18.5) & (df['longitude']==72.5) ]#mumbai
    #df = df.loc[(df['latitude'] == 26.5) & (df['longitude'] == 92.5)]  # assam
    #df = df.loc[(df['latitude'] == 22.5) & (df['longitude'] == 88.5)]  # kolkata
    emptydf=emptydf.append(df.loc[(df['time']>=startdate) & (df['time']<=enddate) ])
    emptydf.to_csv('2013-2016_yvalue_mumbai.csv',index=False)