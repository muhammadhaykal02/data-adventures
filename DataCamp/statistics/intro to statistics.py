# desc stats: describe and summarize data
# inferential stats: use sample of data to make inferences about a larger population

# numeric/quantitative and categorical/qualitative
# numeric: continuous (measured) and discrete (counted)
# categorical: nominal (unordered) and ordinal (ordered)
# with categorical data, can be represented as numbers (but they are NOT numerical)

# numeric: scatter plot or summary
# categorical: counts and barplot

# typical or center value from a dataset
# mean, median and mode
# mean = average (works better for symmetrical data)
# median = mid point, 50% data is lower and 50% data is higher (skewed)
# mode = most frequest value

# adding an outlier
msleep[msleep['vore'] == "insecti"]['sleep_total'].agg([np.mean, np.median])

# measures of spread
# how far your data being spread
# variance, avg distance from each data point to the mean. the higher means the more spread out
# steps: 1. substract mean from data point
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])

# 2. square each distance
sq_dists = dists ** 2

# 3. sum squared distances
sum_sq_dists = np.sum(sq_dists)

# 4. divide by number of data points - 1
var = summ_sq_dists / (83 - 1)
print(var)

# OR simply you can use
np.var(msleep['sleep_total'], ddof=1) # ddof states a sample variance, without it = population var

# std dev, sqr root of var
np.sqrt(np.var(msleep['sleep_total'], ddof=1))

# OR simply
np.std(msleep['sleep_total'], ddof=1)

# mean absolute dev
dists = msleep['sleep_total'] - mean(msleep$sleep_total)
np.mean(np.abs(dists))

# MAD and SD kinda the same, but MAD penalizes each distance equally while in SD longer = more pelanty

# quantile/percantiles
np.quantile(msleep['sleep_total'], 0.5)
# quartiles, dividing into 4 equal parts
np.quantile(msleep['sleep_total'], [0, 0.25, 0.5, 0.75, 1])

# a shortcut for quantiles using np.linspace()
np.quantile(msleep['sleep_total'], np.linspace(0 , 1, 5)) # start, stop and # of interval respectively

# IQR = height of box in boxplot OR 75th - 25th
from scipy.stats import iqr
iqr(msleep['sleep_total'])

# outliers = data points substantially different from others
# data < Q1 - 1,5 x IQR OR data > Q3 + 1,5 x IQR

# in short, you can find these stats using .describe()
