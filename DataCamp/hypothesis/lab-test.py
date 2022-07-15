# A/B test is one of the example of hypothesis test
# lets say in a stackoverflow survey users on their average annual compensation is $110000
# we can generate a bootstrap distribution

import numpy as np
# 3. repeat step 1 & 2 many times, appending to a list
so_boot_distn = []
for i in range(5000):
  so_boost_distn.append(
    # 2. calculate point estimate
    np.mean(
      # 1. resample
      stack_overflow.sample(frac=1, replace=True)['converted_comp']
    )
)
  
# standarizing values uses z-score: value - mean / std dev (samp - hypothesis / std error)

# p values
# hypothesis testing: H0 and HA
# in a normal distribution, we have left and right tail
# to test: alternative different from: two-tailed, greater than: right, less than: left.
# p-value: probability of obtaiing a result, assuming the null hypothesis is true
# => large p-value: large support for H0, small p value: against H0

# for right tail test, whilst for left tail just use norm.cdf()
from scipy.stats import norm
1 - norm.cdf(z_score, loc=0, scale=1)

# to determine the threshold for p values, we uses significance level or alpha.
# p <= A reject H0, else reject H1
# false positive: hypothesis chosen HA but actually H0 true
# false negative: hypothesis chosen H0 but actually HA true

