#Estimated time to run:  

from netCDF4 import Dataset
from netCDF4 import num2date
import numpy as np
import os
import pandas as pd

#Change file names as per your years

#surface level
files = ['air.sig995.2013.nc','pr_wtr.eatm.2013.nc','pres.sfc.2013.nc','rhum.sig995.2013.nc','uwnd.sig995.2013.nc', 'vwnd.sig995.2013.nc']
#multiple levels
file_mul = ['air.2013.nc','omega.2013.nc', 'uwnd.2013.nc', 'rhum.2013.nc', 'vwnd.2013.nc']

for flname in file_mul:
	flnamelist=flname.split(".")
	name=flnamelist[0]
	year=flnamelist[-2]
	outfilename=name+'.'+year+".csv"
	jan = Dataset(flname,mode='r',format='NETCDF4')

	print(jan.variables.keys())
	print(jan.dimensions.keys())
	# print(jan.dimensions['time'])
	print(jan.variables[name])

# read data
	vin = jan.variables[name]
	# print(vin.long_name)
	# print(vin.units)
	# print(vin.get_dims())

	time = jan.variables[name]

	time_dim ,levels, lat_dim, lon_dim= vin.get_dims()
	time_var = jan.variables[time_dim.name]
	times = num2date(time_var[:], time_var.units)
	level = jan.variables[levels.name][:]
	# level = [850, 600, 400]
	latitudes = jan.variables[lat_dim.name][:]
	longitudes = jan.variables[lon_dim.name][:]
	output_dir = './'
	filename = os.path.join(output_dir, outfilename)
	print(f'Writing data in tabular form to {filename} (this may take some time)...')
	times_grid,level_grid,latitudes_grid, longitudes_grid = [x.flatten() for x in np.meshgrid(times,level,latitudes, longitudes, indexing='ij')]
	df = pd.DataFrame({
    	'time': [t.isoformat() for t in times_grid],
    	'level': level_grid,
    	'latitude': latitudes_grid,
    	'longitude': longitudes_grid,
    	name: vin[:].flatten()})
	df=df.loc[(df['latitude']>=5) & (df['latitude']<=40) & (df['longitude']>=65) & (df['longitude']<=100) & ((df['level'] == 850) | (df['level'] == 600) | (df['level'] == 400 ))]
	df.to_csv(filename, index=False)	
	print('Done')


for flname in files:
	flnamelist=flname.split(".")
	name=flnamelist[0]
	year=flnamelist[-2]
	outfilename=name+'.'+flnamelist[1]+year+".csv"
	jan = Dataset(flname,mode='r',format='NETCDF4')
	# print(jan.variables.keys())
	# print(jan.dimensions.keys())
	# print(jan.dimensions['time'])

# read data
	vin = jan.variables[name]
	# print(vin.long_name)
	# print(vin.units)

	time = jan.variables[name]

	time_dim, lat_dim, lon_dim = vin.get_dims()
	time_var = jan.variables[time_dim.name]
	times = num2date(time_var[:], time_var.units)
	latitudes = jan.variables[lat_dim.name][:]
	longitudes = jan.variables[lon_dim.name][:]
	output_dir = './'
	filename = os.path.join(output_dir, outfilename)
	print(f'Writing data in tabular form to {filename} (this may take some time)...')
	times_grid, latitudes_grid, longitudes_grid = [
    	x.flatten() for x in np.meshgrid(times, latitudes, longitudes, indexing='ij')]
	df = pd.DataFrame({
    	'time': [t.isoformat() for t in times_grid],
    	'latitude': latitudes_grid,
    	'longitude': longitudes_grid,
    	name: vin[:].flatten()})
	df=df.loc[(df['latitude']>=5) & (df['latitude']<=40) & (df['longitude']>=65) & (df['longitude']<=100)]
	df.to_csv(filename, index=False)	
	print('Done')