# exploring relationships
# to look the relationship betweeen two var, you can use scatter plot. but sometimes it is way
# too versatile and we can use plot instead with 'o' arg for the marker

plt.plot(height, weight, 'o', markersize=1, alpha=0.02)
plt.show()

# jittering = adding random noise, filling in values that got rounded off.

height_jitter = height + np.random.normal(0, 2, size=len(brfss))
weight_jitter = weight + np.random.normal(0, 2, size=len(brfss))
plt.plot(height_jitter, weight_jitter, 'o', markersize=1, alpha=0.02)
plt.axis([140, 200, 0, 160])
plt.show()

# visualizing relationship
# using boxplot and violin plot
# boxplot and violin plot is essentially KDE from the jittered visualization

# violin plot, using seaborn but have to get rid of rows with missing data
data = brfss.dropna(subset=["AGE", "WTKG3"])
sns.violinplot(x='AGE', y="WTKG3", data=data, inner=None)
plt.show()

# boxplot kinda similar
sns.boxplot(x='AGE', y="WTKG3", data=data, whis=10)
plt.show()

# the box represents IQR, middle line is the median, spine is the min/max value.
# for data that skews towards higher value, we prefer to use log scale
plt.yscale('log')

# correlation
# based on Pearson's correlation between -1 to 1 only works for linear relationship
# usually 1 or -1 means strong relationship. 0 means non-linear

columns = ["HTM4", "WTKG3", "AGE"]
subset = brfss[columns]
subset.corr()

# simple regression
from scipy.stats import linregress
xs = subset['HTM4']
ys = subset['WTKG3']
res = linregress(xs, ys)

fx = np.array([xs.min(), xs.max()])
fy = res.intercept + res.slope * fx
plt.plot(fx, fy, '-')





