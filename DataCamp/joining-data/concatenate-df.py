# merging dataframes vertically, this method originally uses outer join.
# we have a dataset of inventory from jan feb and mar with the same columns

pd.concat([inv_jan, inv_feb, inv_mar])
# but the above doesnt ignore the index, means it will repeat from 0-1 then 0-1 again

pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True)

# setting labels to original table in a concatenated form, will result in a multi-index
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False, keys=['jan', 'feb', 'mar'])

# we can concatenate tables with different columns, it will result in merging them all together
pd.concat([inv_jan, inv_feb], sort=True) # the sort acs as sorting the columns alphabetically

# there's a simplified concat method, uses .append(), it supports ignore_index and sort
# but doesnt support keys and join, therefore the join ALWAYS outer.
# .append() is a dataframe method, therefore

inv_jan.append([inv_feb, inv_mar], ignore_index=True, sort=True)

### exercise 1 ###
# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)

### exercise 2 ###
# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

### exercise 3 ###
# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(by=['quantity'], ascending=False))

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind="bar")
plt.show()
