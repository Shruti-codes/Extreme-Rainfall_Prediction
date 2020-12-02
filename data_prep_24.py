import csv
import pandas as pd
from _datetime import datetime,timedelta
print(datetime.now())
files=['2013/combined2013.csv','2014/combined2014.csv','2015/combined2015.csv','2016/combined2016.csv']
for file in files:
    combined_2009 = pd.DataFrame(pd.read_csv(file))
    dict_grid={}
    list_header = []
    list_of_list = []
    count_months = 0
    past_dates=[]
    print('working on ',file)
    for i in range(0, len(combined_2009), 225):
        list_values = []
        list_values_prev1=[]
        list_values_prev2=[]
        list_header_prev1 = []
        list_header_prev2 = []
        dt = combined_2009.loc[i]['time']
        year_val = dt.split('-')[0]
        if dt != (year_val+'-06-01T00:00:00') and count_months == 0:
            continue
        elif dt == (year_val+'-06-01T00:00:00'):
            count_months = 4
            past_dates=[year_val+'-05-29T00:00:00',year_val+'-05-30T00:00:00']
            # past_dates=[year_val+'-05-28',year_val+'-05-29']
        elif dt == (year_val+'-07-01T00:00:00') or dt == (year_val+'-08-01T00:00:00') or dt == (year_val+'-09-01T00:00:00'):
            count_months -= 1
        elif dt == (year_val+'-10-01T00:00:00'):
            break
        
        if dt!=(year_val+'-06-01T00:00:00') and count_months!=0:
            past_dates[0] = past_dates[1]
            prev_date = str(past_dates[0]).replace('T', '')
            #print(prev_date)
            next_date = datetime.strptime(prev_date, '%Y-%m-%d%H:%M:%S')
            next_date = next_date + timedelta(1)
            next_date = datetime.strftime(next_date, '%Y-%m-%d')
            next_date = next_date + 'T00:00:00'
            past_dates[1] = next_date

        lat = 5.0
        longitude = 65.0
        print(dt)
        dict_grid[dt]={}
        list_values.append(dt)
        list_values_prev1.append(past_dates[0])
        list_values_prev2.append(past_dates[1])

        if dt == '2013-06-01T00:00:00':
            list_header.append('time')
            list_header_prev1.append('past_day1_time')
            list_header_prev2.append('past_day2_time')
        while lat <= 40.0:
            longitude = 65.0
            while longitude <= 100.0:
                # print(lat," ",longitude)
#df.columns= ['time','latitude', 'longitude','air', 'air_850', 'air_600', 'air_400', 'uwnd', 'uwnd_850', 'uwnd_600', 'uwnd_400', 'vwnd', 'vwnd_850',
#'vwnd_600','vwnd_400', 'pres','omega', 'omega_850', 'omega_600', 'omega_400', 'pr_wtr', 'rhum', 'rhum_850', 'rhum_600','rhum_400']
                # air,pres_trop,pres_sfc,rhum,omega,pr_wtr_eatm,uwnd_10m,uwnd,vwnd_10m,vwnd_surf,air_trop,air_2m
                new_str = str(lat) + "_" + str(longitude)
                air = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'air'].iloc[0]
                air_850= combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'air_850'].iloc[0]
                air_600=combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'air_600'].iloc[0]
                air_400=combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'air_400'].iloc[0]
                uwnd = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'uwnd'].iloc[0]
                uwnd_850= combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'uwnd_850'].iloc[0]
                uwnd_600 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'uwnd_600'].iloc[0]
                uwnd_400 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'uwnd_400'].iloc[0]
                vwnd = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'vwnd'].iloc[0]
                vwnd_850 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'vwnd_850'].iloc[0]
                vwnd_600 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'vwnd_600'].iloc[0]
                vwnd_400 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'vwnd_400'].iloc[0]
                pres_sfc = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'pres'].iloc[0]
                omega = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'omega'].iloc[0]
                omega_850= combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'omega_850'].iloc[0]
                omega_600 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'omega_600'].iloc[0]
                omega_400 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'omega_400'].iloc[0]
                pr_wtr_eatm = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'pr_wtr'].iloc[0]
                rhum = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'rhum'].iloc[0]
                rhum_850 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'rhum_850'].iloc[0]
                rhum_600 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'rhum_600'].iloc[0]
                rhum_400 = combined_2009.loc[(combined_2009['time'] == dt) & (combined_2009['latitude'] == lat) & (
                    combined_2009['longitude'] == longitude), 'rhum_400'].iloc[0]


                '''
                list_values.append(air)
                list_values.append(pressure)
                list_values.append(rhum)
                list_values.append(omega)
                list_values.append(pr_wtr)
                list_values.append(uwnd)
                list_values.append(vwnd)
                '''
                dict_grid[dt][new_str]=[air,air_850,air_600,air_400,uwnd,uwnd_850,uwnd_600,uwnd_400,vwnd,vwnd_850,vwnd_600,vwnd_400,
                                        pres_sfc,omega,omega_850,omega_600,omega_400,pr_wtr_eatm,rhum,rhum_850,rhum_600,rhum_400]
                for item in past_dates:
                        date_temp=item
                        #list_values.append(date_temp)
                        if date_temp not in dict_grid:
                            air_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'air'].iloc[0]
                            air_850_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'air_850'].iloc[0]
                            air_600_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'air_600'].iloc[0]
                            air_400_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'air_400'].iloc[0]
                            uwnd_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'uwnd'].iloc[0]
                            uwnd_850_prev=combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'uwnd_850'].iloc[0]
                            uwnd_600_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'uwnd_600'].iloc[0]
                            uwnd_400_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'uwnd_400'].iloc[0]
                            vwnd_prev =combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'vwnd'].iloc[0]
                            vwnd_850_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'vwnd_850'].iloc[0]
                            vwnd_600_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'vwnd_600'].iloc[0]
                            vwnd_400_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'vwnd_400'].iloc[0]
                            pres_sfc_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'pres'].iloc[0]
                            omega_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'omega'].iloc[0]
                            omega_850_prev =combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'omega_850'].iloc[0]
                            omega_600_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'omega_600'].iloc[0]
                            omega_400_prev =  combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'omega_400'].iloc[0]
                            pr_wtr_eatm_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'pr_wtr'].iloc[0]
                            rhum_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'rhum'].iloc[0]
                            rhum_850_prev= combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'rhum_850'].iloc[0]
                            rhum_600_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'rhum_600'].iloc[0]
                            rhum_400_prev = combined_2009.loc[(combined_2009['time'] == date_temp) & (combined_2009['latitude'] == lat) & (
                                combined_2009['longitude'] == longitude), 'rhum_400'].iloc[0]

                        else:
                            air_prev = dict_grid[date_temp][new_str][0]
                            air_850_prev = dict_grid[date_temp][new_str][1]
                            air_600_prev = dict_grid[date_temp][new_str][2]
                            air_400_prev = dict_grid[date_temp][new_str][3]
                            uwnd_prev = dict_grid[date_temp][new_str][4]
                            uwnd_850_prev = dict_grid[date_temp][new_str][5]
                            uwnd_600_prev = dict_grid[date_temp][new_str][6]
                            uwnd_400_prev = dict_grid[date_temp][new_str][7]
                            vwnd_prev = dict_grid[date_temp][new_str][8]
                            vwnd_850_prev = dict_grid[date_temp][new_str][9]
                            vwnd_600_prev = dict_grid[date_temp][new_str][10]
                            vwnd_400_prev = dict_grid[date_temp][new_str][11]
                            pres_sfc_prev = dict_grid[date_temp][new_str][12]
                            omega_prev = dict_grid[date_temp][new_str][13]
                            omega_850_prev = dict_grid[date_temp][new_str][14]
                            omega_600_prev = dict_grid[date_temp][new_str][15]
                            omega_400_prev = dict_grid[date_temp][new_str][16]
                            pr_wtr_eatm_prev = dict_grid[date_temp][new_str][17]
                            rhum_prev = dict_grid[date_temp][new_str][18]
                            rhum_850_prev = dict_grid[date_temp][new_str][19]
                            rhum_600_prev = dict_grid[date_temp][new_str][20]
                            rhum_400_prev = dict_grid[date_temp][new_str][21]


                        
                        if date_temp == past_dates[0]:

                            list_values_prev1.append(air_prev)
                            list_values_prev1.append(air_850_prev)
                            list_values_prev1.append(air_600_prev)
                            list_values_prev1.append(air_400_prev)
                            list_values_prev1.append(uwnd_prev)
                            list_values_prev1.append(uwnd_850_prev)
                            list_values_prev1.append(uwnd_600_prev)
                            list_values_prev1.append(uwnd_400_prev)
                            list_values_prev1.append(vwnd_prev)
                            list_values_prev1.append(vwnd_850_prev)
                            list_values_prev1.append(vwnd_600_prev)
                            list_values_prev1.append(vwnd_400_prev)
                            list_values_prev1.append(pres_sfc_prev)
                            list_values_prev1.append(omega_prev)
                            list_values_prev1.append(omega_850_prev)
                            list_values_prev1.append(omega_600_prev)
                            list_values_prev1.append(omega_400_prev)
                            list_values_prev1.append(pr_wtr_eatm_prev)
                            list_values_prev1.append(rhum_prev)
                            list_values_prev1.append(rhum_850_prev)
                            list_values_prev1.append(rhum_600_prev)
                            list_values_prev1.append(rhum_400_prev)


                        else:
                            list_values_prev2.append(air_prev)
                            list_values_prev2.append(air_850_prev)
                            list_values_prev2.append(air_600_prev)
                            list_values_prev2.append(air_400_prev)
                            list_values_prev2.append(uwnd_prev)
                            list_values_prev2.append(uwnd_850_prev)
                            list_values_prev2.append(uwnd_600_prev)
                            list_values_prev2.append(uwnd_400_prev)
                            list_values_prev2.append(vwnd_prev)
                            list_values_prev2.append(vwnd_850_prev)
                            list_values_prev2.append(vwnd_600_prev)
                            list_values_prev2.append(vwnd_400_prev)
                            list_values_prev2.append(pres_sfc_prev)
                            list_values_prev2.append(omega_prev)
                            list_values_prev2.append(omega_850_prev)
                            list_values_prev2.append(omega_600_prev)
                            list_values_prev2.append(omega_400_prev)
                            list_values_prev2.append(pr_wtr_eatm_prev)
                            list_values_prev2.append(rhum_prev)
                            list_values_prev2.append(rhum_850_prev)
                            list_values_prev2.append(rhum_600_prev)
                            list_values_prev2.append(rhum_400_prev)


                if dt == '2013-06-01T00:00:00':
                    # list_header.append('time')

                    ##
                    list_header_prev1.append('past_day1_air_' + new_str)
                    list_header_prev1.append('past_day1_air_850_' + new_str)
                    list_header_prev1.append('past_day1_air_600_' + new_str)
                    list_header_prev1.append('past_day1_air_400_' + new_str)
                    list_header_prev1.append('past_day1_uwnd_' + new_str)
                    list_header_prev1.append('past_day1_uwnd_850_' + new_str)
                    list_header_prev1.append('past_day1_uwnd_600_' + new_str)
                    list_header_prev1.append('past_day1_uwnd_400_' + new_str)
                    list_header_prev1.append('past_day1_vwnd_' + new_str)
                    list_header_prev1.append('past_day1_vwnd_850_' + new_str)
                    list_header_prev1.append('past_day1_vwnd_600_' + new_str)
                    list_header_prev1.append('past_day1_vwnd_400_' + new_str)
                    list_header_prev1.append('past_day1_pres_sfc_' + new_str)
                    list_header_prev1.append('past_day1_omega_' + new_str)
                    list_header_prev1.append('past_day1_omega_850_' + new_str)
                    list_header_prev1.append('past_day1_omega_600_' + new_str)
                    list_header_prev1.append('past_day1_omega_400_' + new_str)
                    list_header_prev1.append('past_day1_pr_wtr_' + new_str)
                    list_header_prev1.append('past_day1_rhum_' + new_str)
                    list_header_prev1.append('past_day1_rhum_850_' + new_str)
                    list_header_prev1.append('past_day1_rhum_600_' + new_str)
                    list_header_prev1.append('past_day1_rhum_400_' + new_str)

                    list_header_prev2.append('past_day2_air_' + new_str)
                    list_header_prev2.append('past_day2_air_850_' + new_str)
                    list_header_prev2.append('past_day2_air_600_' + new_str)
                    list_header_prev2.append('past_day2_air_400_' + new_str)
                    list_header_prev2.append('past_day2_uwnd_' + new_str)
                    list_header_prev2.append('past_day2_uwnd_850_' + new_str)
                    list_header_prev2.append('past_day2_uwnd_600_' + new_str)
                    list_header_prev2.append('past_day2_uwnd_400_' + new_str)
                    list_header_prev2.append('past_day2_vwnd_' + new_str)
                    list_header_prev2.append('past_day2_vwnd_850_' + new_str)
                    list_header_prev2.append('past_day2_vwnd_600_' + new_str)
                    list_header_prev2.append('past_day2_vwnd_400_' + new_str)
                    list_header_prev2.append('past_day2_pres_sfc_' + new_str)
                    list_header_prev2.append('past_day2_omega_' + new_str)
                    list_header_prev2.append('past_day2_omega_850_' + new_str)
                    list_header_prev2.append('past_day2_omega_600_' + new_str)
                    list_header_prev2.append('past_day2_omega_400_' + new_str)
                    list_header_prev2.append('past_day2_pr_wtr_' + new_str)
                    list_header_prev2.append('past_day2_rhum_' + new_str)
                    list_header_prev2.append('past_day2_rhum_850_' + new_str)
                    list_header_prev2.append('past_day2_rhum_600_' + new_str)
                    list_header_prev2.append('past_day2_rhum_400_' + new_str)




                    # print(pressure)
                longitude += 2.5
            lat += 2.5
        #print(list_header_prev1," ",len(list_header_prev1))
        #print(list_values_prev1," ",len(list_values_prev1))
        #print(list_header_prev2," ",len(list_header_prev2))
        #print(list_values_prev2," ",len(list_values_prev2))
        if len(list_header_prev1) != 0:
            list_header.extend(list_header_prev1)
        if len(list_header_prev2) != 0:
            list_header.extend(list_header_prev2)
        #print("Hi ",list_values, " ", len(list_values))
        if len(list_values_prev1) != 0:
            list_values.extend(list_values_prev1)
        if len(list_values_prev2) != 0:
            list_values.extend(list_values_prev2)
        if len(list_values) != 0:
            list_of_list.append(list_values)
        #print(list_header," ",len(list_header))
        #print(list_values," ",len(list_values))
        #break



    with open('Data_Required/combined_gridview_data_2013_2016_24hrs.csv', 'a+', newline='') as f:
        write = csv.writer(f)
        if len(list_header)!=0:
            write.writerow(list_header)
        write.writerows(list_of_list)
    print('done writing',file)
print(datetime.now())





