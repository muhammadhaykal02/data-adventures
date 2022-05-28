#panda data series, subsetting cars into dr
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars.iloc[:, 2]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

#the oneliner version
# Convert code to a one-liner
sel = (cars[cars['drives_right']])
