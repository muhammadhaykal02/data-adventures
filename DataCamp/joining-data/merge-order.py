# compared to the regular .merge() method
# merge_ordered() is the same for the columns to join on; on, left_on, right_on
# type of join: how; (left, right, inner, outer) but the default is outer for *ordered*.
# you can use suffixes= for overlapping column names
# calling the method uses pd.merge_ordered(df)

# example #
import pandas as pd
pd.merge_ordered(appl, mcd, on='date', suffixes=('_appl', '_mcd'))

# forward fill, interpolate missing value. (but only for the time-date forward)
pd.merge_ordered(appl, mcd, on='date', suffixes=('_aapl', '_mcd'), fill_method='ffill')

### exercise 1 ###
# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())

### exercise 2 ###
# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, on='date', how='inner')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x='unemployment_rate', y='cpi', kind='scatter')
plt.show()
