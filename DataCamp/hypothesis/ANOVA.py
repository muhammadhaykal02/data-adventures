# two-sample problems, compare sample statistics across groups of a variable/the mean. (t test)
# we are trying to find whether stackoverflow users who started programming as a child score bigger compensation
# the hypothesis are:
# H0 = mean compensations = in both groups
# HA = mean compensations that started as a child >> adult.
# the summary statistics
stack_overflow.groupby('age_first_code_cut')['converted_comp'].mean()

# the workflow:
# 1. identify population parameter being hypothesized
# 2. specify the null and alternative hypotheses
# 3. determine std test statistic (z) and corresponding null dist
# 4. conduct test in python
# 5. measure evidence against null hypothesis
# 6. make decision comparing evidence to sig level
# 7. interpret result in the context of original problem

# t series = t dist = looks like normal but with fatter tails
# normal dist = t dist with infinite degree of freedom
degrees_of_freedom = observation_group_a + observation_group_b - 2

# usage of t dist cdf using this code
from scipy.stats import t
1 - t.cdf(t_stat, df=degrees_of_freedom)

# PAIRED ANALYSIS, when you want to determine hypothesis but with the dependent data. (from 2 timeframe)
# uses t test, df = number of different - 1

# you can use pingouin package for hypothesis testing
import pingouin
pingouin.ttest(x=sample_data['diff'],
               y=0,
               alternative="less")

# simpler usage of paired test using pingouin package
pingouin.ttest(x=sample_data['repub_percent_08'],
               y=sample_data['repub_percent_12'],
               paired=True 
               alternative="less")
               
# if we have more than 2 groups to pair, we can simply use anova
pingouin.anova(data=stack_overflow,
               dv="converted_comp",
               between="job_sat")
# but the above data doesn't show which categories have significant differences. hence we uses pairwise ttest
pingouin.pairwise_ttests(data=stack_overflow,
                         dv="converted_comp",
                         between="job_sat",
                        padjust="none")
# with expection that as the # of groups increases = higher chance of false positive significant result. that's why we have to use padjust based on our data
pingouin.pairwise_ttests(data=stack_overflow,
                         dv="converted_comp",
                         between="job_sat",
                        padjust="bonf")
# kinds of padjust
# none: no correction
# bonf/sidak: one step Bonferroni/Sidak correction
# holm: step down method using Bonferroni adjustment
# fdr_bh/fdr_by: Benjamini/Hochberg FDR correction OR Benjamini/Yekutieli

