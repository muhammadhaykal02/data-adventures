# shows the distribution of quantitative data
# each color represent the 25 to 75th percentile
# the line in the middle represents the median

import matplotlib.pyplot as plt
import seaborn as sns

g = sns.catplot(x="time",
                y="total_bill",
                data=tips,
                kind="box",
               order=["Dinner","Lunch"],
               sym="",      #omit the outlier from the plot
                whis=2.0)       # changing whiskers, default 1,5 OR [5,95] or [0,100] (min, max)
plt.show()

