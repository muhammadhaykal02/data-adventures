# limits of simple regression
# regression is asymmetrical, A/B isnt the same as B/A

# multiple regression
# using StatsModels library

import statsmodels.formula.api as smf
results = smf.ols('INCOME2 ~ _VEGESU1', data=brfss).fit() 
results.params    # estimated slope and intercept

# adding another variable
results = smf.ols('realinc ~ educ + age', data=gss).fit() 
results.params

# visualizing regression results, using prediction()
pred12 = results.predict(df)

# logistic regression
# usually for categorical variable data
formula = 'realinc ~ educ + educ2 + age + age2 + C(sex)' # C indicating a categorical var
results = smf.ols(formula, data=gss).fit() 
results.params

# to use it, we have to recode the var into 1 = yes 0 = no for gunlaw from gss dataset
gss['gunlaw'].replace([2], [0], inplace=True)
gss['gunlaw'].value_counts()

formula = 'gunlaw ~ educ + educ2 + age + age2 + C(sex)'
results = smf.logit(formula, data=gss).fit() 
results.params

# the results = positive means more likely, negative unlikely.
# generating predictions
