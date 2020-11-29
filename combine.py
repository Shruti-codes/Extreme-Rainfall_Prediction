from netCDF4 import Dataset
from netCDF4 import num2date
import numpy as np
import os
import pandas as pd
from functools import reduce

#change the years

airdata_mul = pd.read_csv("air.2013.csv", delimiter=',')
airdata = pd.read_csv("air.sig9952013.csv", delimiter=',')
uwnddata_mul =pd.read_csv("uwnd.2013.csv", delimiter=',')
uwnddata=pd.read_csv("uwnd.sig9952013.csv", delimiter=',')
vwnddata_mul=pd.read_csv("vwnd.2013.csv", delimiter=',')
vwnddata=pd.read_csv("vwnd.sig9952013.csv", delimiter=',')
presdata_sfc = pd.read_csv("pres.sfc2013.csv", delimiter=',')
omegadata = pd.read_csv("omega.sig9952013.csv", delimiter=',')
omega_mul = pd.read_csv("omega.2013.csv", delimiter=',')
pr_wtrdata = pd.read_csv("pr_wtr.eatm2013.csv", delimiter=',')
rhumdata = pd.read_csv("rhum.sig9952013.csv", delimiter=',')
rhum_mul = pd.read_csv("rhum.2013.csv", delimiter=',')

air_850 = airdata_mul.loc[(airdata_mul['level'] == 850)].drop('level', axis=1)
air_600 = airdata_mul.loc[(airdata_mul['level'] == 600)].drop('level', axis=1)
air_400 = airdata_mul.loc[(airdata_mul['level'] == 400)].drop('level', axis=1)

uwnd_850 = uwnddata_mul.loc[(uwnddata_mul['level'] == 850)].drop('level', axis=1)
uwnd_600 = uwnddata_mul.loc[(uwnddata_mul['level'] == 600)].drop('level', axis=1)
uwnd_400 = uwnddata_mul.loc[(uwnddata_mul['level'] == 400)].drop('level', axis=1)

vwnd_850 = vwnddata_mul.loc[(vwnddata_mul['level'] == 850)].drop('level', axis=1)
vwnd_600 = vwnddata_mul.loc[(vwnddata_mul['level'] == 600)].drop('level', axis=1)
vwnd_400 = vwnddata_mul.loc[(vwnddata_mul['level'] == 400)].drop('level', axis=1)

omega_850 = omega_mul.loc[(omega_mul['level'] == 850)].drop('level', axis=1)
omega_600 = omega_mul.loc[(omega_mul['level'] == 600)].drop('level', axis=1)
omega_400 = omega_mul.loc[(omega_mul['level'] == 400)].drop('level', axis=1)

rhum_850 = rhum_mul.loc[(rhum_mul['level'] == 850)].drop('level', axis=1)
rhum_600 = rhum_mul.loc[(rhum_mul['level'] == 600)].drop('level', axis=1)
rhum_400 = rhum_mul.loc[(rhum_mul['level'] == 400)].drop('level', axis=1)

dfs = [airdata, air_850, air_600, air_400, uwnddata, uwnd_850, uwnd_600, uwnd_400, vwnddata, vwnd_850, vwnd_600,
vwnd_400, presdata_sfc,omegadata, omega_850, omega_600, omega_400, pr_wtrdata, rhumdata, rhum_850, rhum_600, rhum_400]

df=pd.DataFrame()
df = dfs[0]
for df_ in dfs[1:]:
    df = df.merge(df_, on=['time','latitude','longitude'],  how='outer')
    # print(df.head())

df.to_csv("combined2013.csv",index=False, header=None)
df = pd.read_csv('combined2013.csv', header=None)
df.columns= ['time','latitude', 'longitude','air', 'air_850', 'air_600', 'air_400', 'uwnd', 'uwnd_850', 'uwnd_600', 'uwnd_400', 'vwnd', 'vwnd_850',
'vwnd_600','vwnd_400', 'pres','omega', 'omega_850', 'omega_600', 'omega_400', 'pr_wtr', 'rhum', 'rhum_850', 'rhum_600','rhum_400']
df.to_csv("combined2013.csv",index=False)