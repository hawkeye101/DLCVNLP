# Stats Assignment 4
from numpy import *
from scipy.stats import *
cdf = norm.cdf
ppf = norm.ppf
cdf_t = t.cdf
ppf_t = t.ppf
import pandas as pd

# Problem 1
print('Problem 1')
print('Null Hypothesis: There is no relation between gender and education level.')
print('Alternate Hypothesis: There is a relation between gender and education level.')

observed = [[60, 54, 46, 41, 54 + 46 + 41],
                   [40, 44, 53, 57, 44 + 53 + 57],
                   [100, 98, 99, 98, 98 + 99 + 98]]

df = pd.DataFrame(observed,
                  index=['Female', 'Male', 'Total'],
                  columns=['High school', 'Bachelors', 'Masters', 'PhD', 'Total'])

print(df)
print('\n We next see the expected frequencies for each column.\n')

df = pd.DataFrame([[100/295, 98/295, 99/295, 98/295, 1]],
                  index=['Ex. Fr'],
                  columns=['High school', 'Bachelors', 'Masters', 'PhD', 'Total'])

print(df)

print('\n We next see the expected values table.\n')

expected = [[100/295 * 141, 98/295 * 141, 99/295 * 141, 98/295 * 141, 141],
                   [100/295 * 154, 98/295 * 154, 99/295 * 154, 98/295 * 154, 154],
                   [100, 98, 99, 98, 295]]

df = pd.DataFrame(expected,
                  index=['Female', 'Male', 'Total'],
                  columns=['High school', 'Bachelors', 'Masters', 'PhD', 'Total'])
print(df)
#print('\n We compute the chi-square statistic as follows.')

l,r = shape(observed)
chisq = 0
for i in range(l-1):
    for j in range(r-1):
        chisq = chisq + (observed[i][j] - expected[i][j])**2/(expected[i][j]) 
        
DOF = (4-1)*(2-1)        

print('\nChi-square statistic = %f, DOF = %d' % (chisq, DOF))
print('p-Value = %f' % (1-chi2.cdf(chisq, DOF)))
print('Thus, we reject the null hypothesis with 95% confidence.\n')

# Problem 2
print('Problem 2')
print('Null Hypothesis: All groups have same mean.')
print('Alternate Hypothesis: All groups dont have same mean.')
print('One way ANOVA is conducted using F-test.')
m = 5
n = 3

x1 = [51, 45, 33, 45, 67]
x2 = [23, 43, 23, 43, 45]
x3 = [56, 76, 74, 87, 56]

mu1 = mean(x1)
mu2 = mean(x2)
mu3 = mean(x3)

# mean = mean([mu1, mu2, mu3])

from statistics import *

v1 = stdev(x1)**2
v2 = stdev(x2)**2
v3 = stdev(x3)**2

MSB = stdev([mu1, mu2, mu3])**2 * m
MSW = mean([v1, v2, v3])

f_statistic = MSB/MSW

print('\nF statistic = %f' % (f_statistic))
print('p-value = %f' % (1-f.cdf(f_statistic, n-1, n*(m-1))))
print('Thus, we reject the null hypothesis with 95% confidence.\n')

# Problem 3
print('Problem 3')
print('Null Hypothesis: All groups have same mean.')
print('Alternate Hypothesis: All groups dont have same mean.')
print('One way ANOVA is conducted using F-test.')

m = 5
n = 2

x1 = [10, 20, 30, 40, 50]
x2 = [5, 10, 15, 20, 25]

mu1 = mean(x1)
mu2 = mean(x2)

# mean = mean([mu1, mu2])

v1 = stdev(x1)**2
v2 = stdev(x2)**2

MSB = stdev([mu1, mu2])**2 * m
MSW = mean([v1, v2])

f_statistic = MSB/MSW

print('\nF statistic = %f' % (f_statistic))
print('p-value = %f' % (1-f.cdf(f_statistic, n-1, n*(m-1))))
print('Thus, we cannot reject the null hypothesis with 95% confidence.')