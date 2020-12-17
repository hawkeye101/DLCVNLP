# Stats Assignment 3
from numpy import *
from scipy.stats import *
cdf = norm.cdf
ppf = norm.ppf
cdf_t = t.cdf
ppf_t = t.ppf

# Problem 1
print('Problem 1')

print('Null Hypothesis: Raw cornstarch had NO effect.')
print('Alternate hypothesis: Raw cornstarch had an effect.')
print('Two tailed Z-test is used.')
Z = (108-100) / (15/sqrt(36))
print('Z = |X - μ|/ (σ/√n) = %f' % Z)
print('95%% confidence interval statistic = %f' % ppf(0.95+0.05/2))
print('Thus, we reject the null hypothesis with 5% level of significance.\n')

# Problem 2
print('Problem 2')

from scipy.special import binom

# Formula computed using probability model and combinatorics
def p_sample(a,b,k):
    p = a**k * (1-a)**(b-k) * binom(b,k)
    return p

reqd_p = 0

for k in range(1,100+1):
    for l in range(0,k):
        reqd_p = reqd_p + p_sample(0.52, 100, l) * p_sample(0.47, 100, k)
print('Required probability = %f\n' % reqd_p)

# Problem 3
print('Problem 3')
print('Assuming the SAT scores are normally distributed,')
print('Score of 1100 is in %f percentile.' % (100*cdf((1100-1026)/209)) )