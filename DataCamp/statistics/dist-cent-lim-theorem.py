# normal distribution
# based on mean and standard deviation
# example: women's height
from scipy.stats import norm
norm.cdf(154, 161, 7) # lower than 154, 161 is the mean and 7 is the SD

# to determine the height of 90% women shorter than use ppf
norm.ppf(0.9, 161, 7)

# generating random numbers
norm.rvs(161, 7, size=10) # mean, SD, sample size

# central limit theorem
# sampling dist statistic becomes closer to normal dist as the number of trials inc
# only applies in a randomly and independent samples.

# poisson dist
# event appear to happen at certain rate but completely random. ex: animal adopted per week or number of people arriving at rest
# time unit is irrelevant but this talks about # of events occuring over a period of time
# lambda (expected value) change the distribution peak

# to calc prob of 5 adop per week if the avg is 8
from scipy.stats import poisson
poisson.pmf(5,8)

# to find =< 5
poisson.cdf(5, 8)

# to sample
poisson.rvs(8, size=10)

# exp dist
# probability of time between poisson events, uses lambda and continuous (poisson = discrete).
# example: ticket sold

# to find wait time < 1 min)
from scipy.stats import expon
expon.cdf(1, scale=0.5) # wait time, scale=lambda

# t distribution, student's t dist
# shape looks like normal dist. has parameter of degree of freedom = affect the thickness
# higher df = closer to normal dist, lower df = thicker tails, higher sd

# log-normal dist = var whose logarithm is normally distributed
# example: adult blood pressure, # hospitalization in 2003 sars outbreak

