# a library for data viz
# built on top of matplotlib

# creating scatterplot

sns.scatterplot(x=height, y=weight) # the x and y is the data for each axis
plt.show()

# creating count plot
sns.countplot(x=gender)
plt.show()

====================================================
# pandas with Seaborn

# showing the head of the dataframe we just imported from csv file
import pandas as pd
df = pd.read_csv("masculinity.csv")
df.head()

# use dataframes with countplot()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("masculinity.csv")
sns.countplot(x="how_masculine", data=df) # x shows the name of the column we want to show and
                                          # data refers to which dataframe we are referring the column
plt.show()
