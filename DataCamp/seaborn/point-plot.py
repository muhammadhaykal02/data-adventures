# shows mean of quantitative variable
# uses 95% confidence interval
# looks like line plots, shows mean quantitative variable and 95% ci
# but point plot has categorical variable, hence a categorical plot.

import matplotlib.pyplot as plt
import seaborn as 
from numpy import median  # conditional, only required if you want to change from mean to median

sns.catplot(x="age",
            y="masculinity_important",
            data=masculinity_data,
            hue="feel_masculine",
            kind="point",
            join=False,   # to get rid of the line connecting each points.
            capsize=0.2,   # customizing confidence interval
            ci=None
            estimator=median)   # to change from mean to median, used when there's a lot outliers.
plt.show()

