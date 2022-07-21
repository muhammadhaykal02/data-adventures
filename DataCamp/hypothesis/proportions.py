# it's okay to use z test instead of t because there's only p-hat (sample proportion) in the numerator
# example: stack overflow age categories with alpha 0.01 (single proportion)
# H0 = proportion of SO users under thirty = 0.5
# HA = proportion of SO users under thirty != 0.5

# checking the data using value counts
stack_overflow['age_cat'].value_counts(normalize=True)
# finding variables for z
p_hat = (stack_overflow['age_cat'] == 'Under 30').mean()
p_0 = 0.5 # from null hypothesis
n = len(stack_overflow) # sample size
# calculating z-score
import numpy as np
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)
z_score = numerator / denominator
# transforming z score into p value based on the distribution
# for left tail
from scipy.stats import norm
p_value = norm.cdf(z_score)
# for right tail
p_value = 1 - norm.cdf(z_score)
# for two tailed
p_value = norm.cdf-z_score) + 1 - norm.cdf(z_score) # or simplified
p_value = 2 * (1 - norm.cdf(z_score))

# double proportions in 2 populations
# H0 = proportion of SO users that is hobbyist the same for under thirty and above
# HA = proportion of SO users that is hobbyist different for under thirty and above
# we need to find 4 variables, p-hat >30 and <30, population number >30 and <30.
p_hats = stack_overflow.groupby("age_cat")["hobbyist"].value_counts(normalize=True)
p_hat_at_least_30 = p_hats[("At least 30", "Yes")]
p_hat_under_30 = p_hats[("Under 30", "Yes")]
print(p_hat_at_least_30, p_hat_under_30)

n = stack_overflow.groupby("age_cat")["hobbyist"].count()
n_at_least_30 = n["At least 30"]
n_under_30 = n["Under 30"]
print(n_at_least_30, n_under_30)

# then proceeds to calculate the total p_hat, std_error and z_score and print it.
# simpler way
age_by_hobbyist = stack_overflow.groupby("age_cat")['hobbyist'].value_counts()
from statsmodels.stats.proportion import proportions_ztest
success_counts = np.array([812, 1021]) # from the data age of hobbyist
n = np.array([812 + 238, 1021 + 190]) # adding the data
stat, p_value = proportions_ztest(count=success_counts, nobs=n, alternative="two-sided")

# for more than 2 groups, use chi-test of independence to determine its dependence
# in visualizing the data, if the stacked bar happens to be at the same height = independent, otherwise it's associated.
import pingouin
expected, observed, stats = pingouin.chi2_independence(data=stack_overflow, x='hobbyist', y='age_cat', correction=False)
print(stats)

# comparing single categorical var to hypothesized dist.
# from the SO user survey, how would they feel if they've visited the web for question they googled
# we are hypothesizing that from each answers, the proportions are as such
# renaming column
purple_link_counts = purple_link_counts.rename_axis('purple_link').reset_index(name='n')

# chi-square is used to measure how far observed results are from expectations.
from scipy.stats import chisquare
chisquare(f_obs=purple_link_counts['n'], f_exp=hypothesized['n'])
