# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)
===============================
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)
===============================
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
    print(area)
======================
#HOW TO ENUMERATE
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index) +": " + str(a))
=========================
#start numbering colum from 1
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    index += 1
    print("room " + str(index) + ": " + str(area))
    
========================
#list of list
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house :
    print("the " + x[0] + " is " + str(x[1]) + " sqm")
#the list isn't paired, so you can always use x[0] and x[1] to refer the list.

==============================
#loop over dictionary

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for country, capital in europe.items() :
    print("the capital of " + country + " is " + capital)
    
====================================
#loop over numpy array

# Import numpy as np
import numpy as np

# For loop over np_height, a 1D numpy
for height in np_height :
    print(str(height) + " inches")

# For loop over np_baseball, a 2D numpy
for data in np.nditer(np_baseball) :
    print(data)

==================================
#loop over data frame (panda series)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
    
=========================
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop, this is an item (string) so you need to use [0] instead of the name of the column/row.
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row[0]))
    
=========================================
#how to add a new column in your dataframe, adding country name in uppercase (.upper() method)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)
==================================
#adding new column to dataframe in oneliner

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper), the left refers to the column name we want and the right is the column we are referring to.
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
