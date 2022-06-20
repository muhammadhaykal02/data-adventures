# inner join essentially means you are merging two dataframes into one where there must be an overlapping between the two dataframes.
# inner join only works for the same shape of dataframe (number of rows and columns)
# use the function .merge

# example
wards_cencus = wards.merge(census, on='ward')
print(wards_cencus.head(4))

# the above code will print a new dataframe from two different one, with census as the main df
# and it will be merge from the column 'ward'
# they usually will end up with indexes of _x and _y if theres overlapping columns
# use suffixes to get replace the x and y

# example
wards_cencus = wards.merge(census, on='ward', suffixes=('_ward','_cen'))
print(wards_cencus.head())
print(wards_cencus.shape)
