# Stats Assignment 1

import numpy as np

# Problem 1
print('Problem 1')
from scipy import stats

input = [6,7,5,7,7,8,7,6,9,7,4,10,6,8,8,9,5,6,4,8]

print('Mean = %f' % np.mean(input))
print('Median = %f' % np.median(input))
print('Mode = ', stats.mode(input)[0][0])
print('\n')

# Problem 2
print('Problem 2')
input = [28, 122, 217, 130, 120, 86, 80, 90, 140, 120, 70, 40, 145, 113, 90, 68, 174, 194, 170, 100, 75, 104, 97, 75, 123, 100, 75, 104, 97, 75, 123, 100, 89, 120, 109]

print('Mean = %f' % np.mean(input))
print('Median = %f' % np.median(input))
print('Mode = ', stats.mode(input)[0][0])
print('\n')

# Problem 3
print('Problem 3')
x = [0,1,2,3,4,5]
f = [0.09,0.15,0.4,0.25,0.1,0.01]
mean = np.sum([a*b for a,b in zip(x,f)])
print('Mean = %f' % mean)
deviation = x - mean
variance = np.sum([a*a*b/(len(x)-1) for a,b in zip(deviation,f)])
#std_deviation = np.sqrt(variance)
print('Variance = %f' % variance)
print('\n')

# Problem 4
print('Problem 4')
def pdf(d):
    return 20*np.e - 20*(d-12.5)

max_d = 12.5 + np.e
pdf_min = 20*np.e
Normalization = 1/2 * (max_d-12.5) * pdf_min # Area of triangle

d_value = 12.6
proportion_of_parts = 1/2 * (max_d - d_value) * pdf(d_value) / Normalization
print('Proportion of parts > 12.6 mm = %f' % proportion_of_parts)
print('CDF when d = 11mm is 0 because pdf is 0 for d<12.5mm')
print('Conclusion: Proportion of parts closer to 12.5mm is higher')
print('\n')

# Problem 5
print('Problem 5')
import math
from sympy import * 

def ncr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

def probability_calc(a, b, c):
    expr = ncr(b, a) * c**a * (1-c)**(b-a)
    return expr
    
print('Probability of 2 faulty bulbs = %f' % probability_calc(2,6,0.3))

mean = 0.3*6
print('Average number of faulty bulbs out of 6 = %f' % mean)

deviances = [(x - mean)**2 * probability_calc(x, 6, 0.3) for x in range(7)]
#print(deviances)
variance = np.sum(deviances)
print('Standard deviation = %f' % sqrt(variance))

print('\n')

# Problem 6
print('Problem 6')

Gaurav_total = 8
Gaurav_correct_rate = 0.75
Barakha_total = 12
Barakha_correct_rate = 0.45

def p_correct(no_of_correct, total, correct_rate):
    return probability_calc(total - no_of_correct, total, 1 - correct_rate)

Gaurav_no_of_correct = 5
p_Gaurav = [p_correct(Gaurav_no_of_correct, Gaurav_total, Gaurav_correct_rate) for Gaurav_no_of_correct in range(Gaurav_total+1)]
p_Barakha = [p_correct(Barakha_no_of_correct, Barakha_total, Barakha_correct_rate) for Barakha_no_of_correct in range(Barakha_total+1)]

print('Probability that Gaurav gets 5 out of 8 correctly = %f' % p_Gaurav[5])
print('Probability that Barakha gets 5 out of 12 correctly = %f' % p_Barakha[5])

print('Probability that Gaurav gets 4 out of 8 correctly = %f' % p_Gaurav[4])
print('Probability that Barakha gets 6 out of 12 correctly = %f' % p_Barakha[6])

print('Two main factors affecting ability to solve questions correctly are total number of questions and correction rate.')

import matplotlib.pyplot as plt
plt.figure()
plt.plot(p_Gaurav, '-bo')
plt.title('Problem 6, Gaurav (CR %d %% Total %d)' % (Gaurav_correct_rate * 100, Gaurav_total))
plt.xlabel('No. of correct answers')
plt.ylabel('Probability of correct answers')
plt.show()

plt.figure()
plt.plot(p_Barakha, '-bo')
plt.title('Problem 6, Barakha (CR %d %% Total %d)' % (Barakha_correct_rate * 100, Barakha_total))
plt.xlabel('No. of correct answers')
plt.ylabel('Probability of correct answers')
plt.show()

print('\n')

# Problem 7
print('Problem 7')

def Poisson_dist(rate, k):
    return rate**k * np.exp(-rate) / factorial(k)

print('Probability of k customers in 4 minutes is given by Poisson distribution with rate 4.8 = 72/60*4')
print('Probability of 5 customers = %f' % Poisson_dist(4.8, 5))
not_more_than_3 = Poisson_dist(4.8, 0) + Poisson_dist(4.8, 1) + Poisson_dist(4.8, 2) + Poisson_dist(4.8, 3)
print('Probability of not more than 3 customers = %f' % not_more_than_3)
print('Probability of more than 3 = %f' % (1 - not_more_than_3))

poisson_val = [Poisson_dist(4.8, k) for k in range(16)]
plt.figure()
plt.plot(poisson_val, '-bo')
plt.title('Problem 7, Poisson distribution for rate 4.8')
plt.xlabel('No. of customers in 4 minutes')
plt.ylabel('Probability')
plt.show()
print('\n')

# Problem 8
print('Problem 8')

def p_2errors(no_of_words):
    rate_of_error = no_of_words / 77 * 0.6
    p_2error = Poisson_dist(rate_of_error, 2)
    print('Rate of error = %f' % rate_of_error)
    print('Probability of 2 errors in %d word report = %f' % (no_of_words, p_2error))
    poisson_val = [Poisson_dist(rate_of_error, k) for k in range(16)]
    plt.figure()
    plt.plot(poisson_val, '-bo')
    plt.title('Problem 8, Poisson distribution for rate %f' % rate_of_error)
    plt.xlabel('No. of errors')
    plt.ylabel('Probability')
    plt.show()

p_2errors(455)
p_2errors(1000)
p_2errors(255)
print('\n')

# Problem 9
print('Problem 9')
print('Same as Problem 4')
print('\n')

# Problem 10
print('Problem 10')

from scipy.stats import *
cdf = norm.cdf

print('P(Z > 1.26) = 1 - P(Z < 1.26) = %f' % (1 - cdf(1.26)))
print('P(Z < -0.86) = %f' % cdf(-0.86))
print('P(Z > -1.37) = P(Z < 1.37) = %f' % cdf(1.37))
print('P(-1.25 < Z < 0.37) = P(Z < 0.37) - P(Z < -1.25) = %f' % (cdf(0.37) - cdf(-1.25)))
print('P(Z < -4.6) = %f' % cdf(-4.6))

ppf = norm.ppf

print('PMF (cdf = 0.05) = %f' % ppf(1 - 0.05))
print('For P(-z < Z < z) = 0.99, cdf = 0.99 + (1-0.99)/2 = 0.995, PMF(cdf) = %f' % ppf(0.995))
print('\n')

# Problem 11
print('Problem 11')
print('Z value for 13mA = (13-10)/2 = 1.5')
print('P(Z > 0.75) = %f' % (1 - cdf(1.5)))
print('Z value for 9 and 11 mA = -0.5 and 0.5')
print('P(-0.25 < Z < 0.25) = %f' % (cdf(0.5) - cdf(-0.5)))
z_98 = ppf(0.98)
print('Z value for cdf 0.98 = %f' % z_98)
print('Corresponding current measurement = %f * 2 + 10 = %f mA' % (z_98, z_98*2 + 10))

print('\n')

#Problem 12
print('Problem 12')
print('Mean = 0.2508, std = 0.0005')
print('Z value of 0.2515 and 0.2485 = 1.4 and -4.6')
print('P (-4.6 < Z < 1.4) = %f' % (cdf(1.4) - cdf(-4.6)))
print('Thus, roughly 91.9% of shafts are within specifications.')
print('With new mean, Z value is between -3 and 3. Thus,')
print('P(-3 < Z < 3) = %f' % (cdf(3) - cdf(-3)))
print('Thus, 99.7% of shafts are within specifications.')
print('Conclusion: If mean is centered as per specifications, there is lesser chance of error.')

print('\n')
