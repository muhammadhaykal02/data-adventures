# panda can read data in csv, excel, hdf5
# shape = # of (rows, columns)

# using the nsfg dataframe
# finding the number of rows and columns
nsfg.shape

# displaying the columns name
nsfg.columns

# creating a variable for a selected column
ounces = nsfg["birthwgt_oz1"]
print(ounces.head())

# you can *validate* the data you have using value_counts() then *match* it with the codebook
pounds = nsfg["birthwgt_lb1"]
pounds.value_counts().sort_index()  # value_counts looking at the values from the column that is in lbs
                                    # then sort_index is sorting the data in index instead of values

 # another way using .describe() which will gives the statistical data from our dataframe.
pounds.describe()

# in *cleaning* the value of indexes we don't want, we can use replace()
# let's say we want to remove the values from index 98 and 99 (because they are not relevant)
pounds = pounds.replace([98, 99], np.nan) # we are assigning pounds again to replace the first one
                                          # nan means we are replacing the value with not a number
# there is a way to cleanly do the replace (without assigning new variable using inplace)
ounces.replace([98, 99], np.nan, inplace=True)

# to *filter* and *visualize* the data
plt.hist(birth_weight.dropna(), bins=30)    # cleaning using .dropna()
plt.xlabel('Birth weight (lb)')
plt.ylabel('Fraction of births')
plt.show()

# when COMPARING series to a value, will result in a Boolean series
preterm = nsfg['prglngth'] < 37 # the series is prglngth and the value is 37

# in boolean series, we can calculate how much data that satisfied our condition
# in this case, babies that is in preterm condition
preterm.sum()
preterm.mean()

# another way we can filter, after we made the variable
preterm_weight = birth_weight[preterm]
preterm_weight.mean()

full_term_weight = birth_weight[~preterm]   # instantly uses the logical NOT makes the TRUE = FALSE
full_term_weight.mean()                     # this works because our data was a boolean series

# sometimes, the data provided have certain oversampled groups. to resample we can use
resample_rows_weighted()


