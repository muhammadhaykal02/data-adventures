# technically can be done using index_col argument from the read_csv method.
# use the argument on from the index level

# example
samuel_casts = samuel.merge(casts, on=['movie_id,'cast_id'])
print(samuel_casts.head())
print(samuel_casts.shape)
                                       
# if the index name on the right and left is different, you can use the left and right on argument
# for the merge method
                                       
# example
movies_genres = movies.merge(movie_to_genres, left_on='id', left_index='True,
                             right_on='movie_id', right_index=True)
print(movies_genres.head())
                                       
                                       
 ### exercise ###
                                       # Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())
