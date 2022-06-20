# left join merge the left table with only the key columns from the right table.
# the code persist only an added argument how='left'

# example
movies_taglines = movie.merge(taglines, on='id', how='left')
print(movies_taglines.head())

### exercise 1 ###
# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

