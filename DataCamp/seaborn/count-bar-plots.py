# is a categorical plots, involve categorical variable.
# used in comparisons between groups.
# use catplot() to create categorical plot, same as relplot()

import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(x="how_masculine",
            data=masculinity_data,
            kind="count")
plt.show()

# to change the order of the count, create a list with the order and use order parameter.

import matplotlib.pyplot as plt
import seaborn as sns
category_order = ["No answer",
                  "not at all",
                  "not very",
                  "somewhat",
                  "very"]

sns.catplot(x="how_masculine",
            data=masculinity_data,
            kind="count",
            order=category_order)
plt.show()

# bar plot shows the mean, uses 95% confidence intervals. setting ci parameter to None to turnoff

import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(x="day",    # switching x and y into one another to rotate it 90 degree
            y="total_bill",
            data=tips,
            kind="bar")
plt.show()
