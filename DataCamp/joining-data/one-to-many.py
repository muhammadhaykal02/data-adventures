# one to one relationship can be found in the inner join module
# one to many can be found such as, in a ward (areas of chicago) there will be one too many
# small licensed business. use the same argument as the one-to-one

# example
ward_licenses = ward.merge(licenses, on='ward', suffixes=('_ward','_lic'))
print(ward_licenses.head())

### exercise ###

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values("account", ascending=False)
# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

# merging multiple dataframes
# determine which column that exists in both dataframe, think it thoroughly in order to make sure
# the merge data IS correct. also use backslash to make sure python reads your code in one line

# example
grants_licenses_ward = grants.merge(licenses, on=['address','zip']) \
.merge(wards, on='ward', suffixes=('_bus','_ward'))
grants_licenses_ward.head()

### exercise ###
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

### exercise 2 ###
# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))

### exercise 3 ###
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], 
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())
