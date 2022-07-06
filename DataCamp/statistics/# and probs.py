# sampling from df
sales_counts.sample() # but this wont result in the same one if being done twice

# to get the same result each time you run the code, set a random seed
np.random.seed(10)  # the number can be anything but you have to run it using the same one
sales_counts.sample()

# sampling without replacement, no turning back
sales_counts.sample(2) # if you want to sample twice

# to determine sampling with/without replacement, use the argument
sales_counts.sample(5, replace=True)

# probability dist = desc the prob of each possible outcome
# expected value: mean of prob dist. 
np.mean(die['number'])

# discrete dist: describe probs for discrete outcomes (can be counted)

rolls_10['number'].hist(bins=np.linspace(1, 7, 7))
plt.show()

# continuous dist: 
# uniform dist
from scipy.stats import uniform
uniform.cdf(7, 0, 12) # 7 is the time, 0 is lower and 12 is upper limit

# generating random numbers using uniform dist
from scipy.stats import uniform
uniform.rvs(0, 5, size=10)

# binomial dist: probs distribution of number success in sequence of independent trials
# n: total number of trial, p: probability of success
# in case of coin flipping, number of head
from scipy.stats import binom
binom.rvs(1, 0.5, size=8) # number of coins, probability/chance of success, how many times

# if we want to know the probability for certain number of head
binom.pmf(7, 10, 0.5) # number of success, trials and probability

# expected value: n x p



