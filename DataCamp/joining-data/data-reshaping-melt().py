# long format is more accessible for computer, hence still needed.
# changing from horizontal to vertical

social_fin_tall = social_fin.melt(id_vars=['financial','company'])
print(social_fin_tall.head(10))

# melting with value_vars argument, to unpivot certain columns.

social_fin_tall = social_fin.melt(id_vars=['financial','company'],
                                 value_vars=['2018','2017'])
print(social_fin_tall.head(9))

# naming the variable and value name of the long table

social_fin_tall = social_fin.melt(id_vars=['financial','company'],
                                 value_vars=['2018','2017'], var_name=['year'], value_name='dollars')
print(social_fin_tall.head(8))

### exercise 1 ###
# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')


# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values(by=['date'], ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()

### exercise 2 ###
# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars=['metric'], var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', how="inner", suffixes=('_dow','_bond'))


# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()
