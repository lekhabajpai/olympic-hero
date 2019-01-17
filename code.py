# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here
data = pd.read_csv(path)
data.rename(index=str, columns={"Total": "Total_Medals"}, inplace=True)
print(data.head(10))



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
better_event = data['Better_Event'].value_counts()
better = ['Summer', 'Winter', 'Both']
better_value = max(better_event[0], better_event[1], better_event[2])
better_event = better[0]
print(better_event)





# --------------
#Code starts here
#print(data.head())
def top_ten(countries, column_name):
    country_list = {}
    country_list = list((countries.nlargest(10,column_name)['Country_Name']))
    #print(country_list)
    return country_list

top_countries = pd.DataFrame(data, columns = ['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals'])
top_countries=top_countries[:-1]
#print(top_countries)
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
print('SummerT', top_10_summer)
print('WinterT', top_10_winter)
print('MedalsT', top_10)

common = list(set(top_10_summer) & set( top_10_winter) & set(top_10))
print('COM', common)




# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
#summer_df.sort_values(by='Total_Summer', inplace=True, ascending=False)
#print(summer_df)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
#winter_df.sort_values(by='Total_Winter', inplace=True, ascending=False)
#print(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]
#top_df.sort_values(by='Total_Medals', inplace=True, ascending=False)
#print(top_df)

plt.figure(figsize=(20,6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.title('Top 10 Countries in Summer Olympics')
plt.xlabel('Country Name')
plt.ylabel('Total Medals in Summer')
plt.show()

plt.figure(figsize=(20,6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Winter'])
plt.title('Top 10 Countries in Winter Olympics')
plt.xlabel('Country Name')
plt.ylabel('Total Medals in Winter')
plt.show()

plt.figure(figsize=(20,6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Medals'])
plt.title('Top 10 Countries in Medals Olympics')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.show()




# --------------
#Code starts here
#Summer
summer_df['Golden_Ratio']=(summer_df['Gold_Summer']/summer_df['Total_Summer'])
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(), 'Country_Name']
print('Country with Max Gold in Summer: ', summer_country_gold)
#Winter
winter_df['Golden_Ratio']=(winter_df['Gold_Winter']/winter_df['Total_Winter'])
print(winter_df)
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']
print('Country with Max Gold in Winter: ', winter_country_gold)
#Top
top_df['Golden_Ratio']=(top_df['Gold_Total']/top_df['Total_Medals'])
top_max_ratio = max(top_df['Golden_Ratio'])
#print(top_max_ratio)
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(), 'Country_Name']
print('Top Country with Max Gold: ', top_country_gold)





# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points']=3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + 1*data_1['Bronze_Total']
most_points=max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)




# --------------
best=data[data['Country_Name'] == best_country]
best=best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
print(best)
best.plot(kind='bar', stacked=True, title='Best Country', figsize=(20,6))
#plt.bar(best, best_country)
plt.xlabel('United States', rotation=45)
plt.ylabel('Medals Tally')
plt.show()


