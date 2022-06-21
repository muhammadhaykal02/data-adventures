# semi join, the same as inner join but only return the left table columns and no duplicate
# so one-to-many relationship is neglected.

# example, music dataset from streaming service we want to find what genre appear on the first df.
# step 1, inner join #
genres_tracks = genres.merge(top_tracks, on='gid')
print(genres_tracks.head())

# step 2, semi join. this line of code is used to find genres that appear in the genres_tracks #
genres['gid'].isin(genres_tracks['gid'])

# step 3, combining everything #
genres_tracks = genres.merge(top_tracks, on='gid')
top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
print(top_genres.head())

# anti joins, returns the left table that doesnt exist in the right one #

# step 1, left join, the argument indicator is used to add a new column whether the rows exists
# in both table or just one of them. #
genres_tracks = genres.merge(top_tracks, on='gid', how='left', indicator=True)
print(genres_tracks.head())

# step 2, uses loc to filter the table that only has left only indicator.
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
print(gid_list.head())

# step 3, combining them all #
genres_tracks = genres.merge(top_tracks, on='gid', how='left', indicator=True)
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]
print(non_top_genres.head())

### exercise 1 ###
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])


### exercise 2 ###
# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid': 'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid').head())

