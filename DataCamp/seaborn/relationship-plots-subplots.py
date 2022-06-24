# creating subgroup from the sameplot using relplot()
# relplot() = relational plot. visualize two quantitative var.

import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter"
            col="smoker"    # this part specifies if we want to create subplots in col/rows
            col_wrap=2,     # specify how many subplot you want horizontally/vertically
            col_order=["Thur", "Fri", "Sat", "Sun"]) # specify the order
plt.show()

## customizing scatter plots ##
##### point size #####

import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter"
            size="size",  # categorize the data according to the size column
            hue="size")   # differentiate the color
plt.show()

##### point style ######

import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter"
            style="smoker",  # gives different point style for each subgroup
            hue="size")   # differentiate the color
plt.show()

##### point transparency #####

import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter"
            alpha=0.4)   # specify the transparency of the points, 0 being transparent 1 opaque
plt.show()

# LINE PLOT #
# general guidelines for creating line plot
import matplotlib.pyplot as plt
import seaborn as sns

sns.relplot(x="hour", y="NO_2_mean", data=air_df_mean, kind="line")
plt.show()

# customizing line plots
import matplotlib.pyplot as plt
import seaborn as sns

sns.relplot(x="hour", y="NO_2_mean", data=air_df_loc_mean, kind="line", 
            style="location", # to subgroup from a column
            hue="location", # to differentiate the colors
            markers=True # add a marker point
            dashes=False) # line style being turned off, hence all same line except the color.
plt.show()

# in line plot, when you have one x variable with multiple y values it will creates confiddence
# interval all by itself

import matplotlib.pyplot as plt
import seaborn as sns

sns.relplot(x="hour", y="NO_2"
            data=air_df,
            kind="line",
            ci="sd") # we can change the confidence interval into standard deviation, or turn
                     # it off using ci=None
plt.show()
