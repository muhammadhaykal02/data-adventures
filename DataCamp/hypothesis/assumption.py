# each sample MUST randomly sourced from its population to make sure it's representative
# independence of observations: each row must be independent to make sure there's no false negative/positive error
# sample size: large enough where central limit theorem applies
# for t-test:
# 1 sample: n >= 30, 2 samples: n1/n2 >= 30, ANOVA: ni >= 30, paired sample: # rows in data >= 30
# for proportion test
# 1 sample: n * p-hat >= 10 & n * (1-phat) >= 10, 2 samples: n success (n*phat) and failure (n* 1-phat) >= 10
# for chi square test
# n success (n*phat) and failure (n* 1-phat) >= 5

# if the assumptions from the hypothesis arent met: use non parametric test
# only use non parametric test for small sample size and data is NOT normally distributed
# Wilcoxon rank test == t-test parametric
pingouin.wilcoxon(x=repub_votes_potus_08_12_small['repub_percent_08'],
                  y=repub_votes_potus_08_12_small['repub_percent_12'],
                  alternative="less")
# for small sample size that is UNPAIRED for two groups uses Wilcoxon-Mann-Whitney
# changing the data from long to wide format using pivot
age_vs_comp_wide = age_vs_comp.pivot(columns='age_first_code_cut', values='converted_comp')
pingouin.mwu(x=age_vs_comp_wide["child"],
             y=age_vs_comp_wide['adult'],
             alternative='greater')

# to test MORE than 2 groups uses Kruskal-Wallis test (non parametric ver of ANOVA)
pingouin.kruskal(data=stack_overflow,
                 dv='converted_comp',
                 between='job_sat')

