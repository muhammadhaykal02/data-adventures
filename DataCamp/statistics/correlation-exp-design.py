# correlation
# relationship between numeric vars, can use scatterplot

import seaborn as sns
sns.lmplot(x="sleep_total", y="sleep_rem", data=msleep, ci=None) # lmplot to show scatter with trendline, ci=emits the margin from line 
plt.show()

# computing correlation (Pearson product moment r)
msleep["sleep_total"].corr(msleep['sleep_rem'])

# there's caveats when you see a non-linear relationship.
# dont forget to always visualize your data to determine your correlation

# log transforming the data
msleep["log_bodywt"] = np.log(msleep['bodywt'])

sns.lmplot(x="log_bodywt", y="awake", data=msleep, ci=None)
plt.show()

# another transformations for your data:
# log, square root and reciprocal (1/x) or a combination of those three
# correlation doesn't imply causation
# if x corr with y =/= x causes y

# design of experiments
# 1. controlled experiments: participants assigned to either treatment OR control group
# let's say in an study of advertisement (treatment) towards buying power (response)
# treatment: sees the ads, control: doesn't. each group should be comparable in order to avoid bias/confounding

# the gold standard
# randomized controlled trial: participants assigned to treatment/control group RANDOMLY
# placebo: resembles treatment but has no effect and participants dont know which group they're in
# double blind trial: person running the study doesn't know whether the treatment is real/placebo in order to prevent bias
# fewer opportunities for bias = more reliable conclusion about causation

# 2. observational studies: assigned themselves based on pre-existing characteristics
# this only gives association, not causation and since the participants already got into certain group, there might be confounded factors that made certain people fall into that group
# but there is a way to control that confounders to get more reliable conclusions

# way of collecting data, longitudinal vs cross sectional studies
# longitudinal: participants followed over period of time, more expensive and longer in terms of time
# cross-sectional: data collected from a single snapshot in time, cheaper faster and more convenient
# eg. in a study of height and age, in cross sectional study the effect of age on height is confounded by generation (year they were born and lifestyle)
# whilst in longitudinal, the effect of age is not confounded since we measure the participants' height every year.
