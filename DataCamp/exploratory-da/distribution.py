# to show distribution, we can use histogram, probability mass function, cumulative distribution f
# pmf will display each unique value (unlike histogram where separated by bins)
pmf_educ = Pmf(educ, normalize=False)   # normalize = the count will be in fractions = 1
pmf_educ.head()

# to find how much data from certain value, we can go ahead and bracket the value
pmf_educ[12]    # the number will shows the amount of people that answers the value 12

# creating a bar chart for pmf
pmf_educ.bar(label="educ")
plt.xlabel('Years of education')
plt.ylabel('PMF')
plt.show()

# cdf is cumulative sum of PMF
cdf = Cdf(gss["age"])
cdf.plot()
plt.xlabel('Age')
plt.ylabel('CDF')
plt.show()

# cdf object can be used as function
q = 51
p = cdf(q)
print(p)  # will result in the number (percentage) of (let's say) people 51 yo or *younger*.

# IQR = interquartile range, diff between 75th and 25th percentile
# 75th quartile, cdf.inverse() <<< questionable??

# CDF is smoother in making graphs than PMF, to plot two categories in one
Cdf(income[pre95]).plot(label='Before 1995')
Cdf(income[~pre95]).plot(label='After 1995')

# probability density function (bell curve)
# for nromal distribution
from scipy.stats import norm

xs = np.linspace(-3,3) # create a linear space from -3 and 3 that is equally distributed
ys = norm(0,1).cdf(xs) # norm creates object normal dist with mean 0 sd 1

# to change from pmf to pdf, we use kde
import seaborn as sns
sns.kdeplot(sample)

# CDF = exploration
# PMF = small number of unique value
# KDE = lot of values
