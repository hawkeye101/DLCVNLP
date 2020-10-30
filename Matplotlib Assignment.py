# Matplotlib Assignment

# Problem 1
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

xdata = np.linspace(1,12,12)
Max = [39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25]
Min = [21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18]

def func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

xcurve = np.linspace(0,13,100)

from scipy.optimize import curve_fit

ydata = Max
popt_max, pcov_max = curve_fit(func, xdata, ydata)
ycurve_max = [func(xcurve[i], popt_max[0], popt_max[1], popt_max[2], popt_max[3]) for i in range(len(xcurve))]

plt.plot(xdata, ydata, marker = 'o', ls = 'None', color = 'red')
plt.plot(xcurve, ycurve_max, color = 'red')

ydata = Min
popt_min, pcov_min = curve_fit(func, xdata, ydata)
ycurve_min = [func(xcurve[i], popt_min[0], popt_min[1], popt_min[2], popt_min[3]) for i in range(len(xcurve))]

plt.plot(xdata, ydata, marker = 'o', ls = 'None', color = 'blue')
plt.plot(xcurve, ycurve_min, color = 'blue')
plt.show()


# Problem 2
# Part 1
import pandas as pd
url = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)[0:1309]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Male', 'Female']

from collections import Counter
mpl.rcParams['font.size'] = 14.0
gender = [Counter(titanic['sex'])['male'], Counter(titanic['sex'])['female']]
ax.pie(gender, labels = langs,  autopct='%1.2f%%')
plt.show()

# Part 2
import seaborn as sns
scplot = sns.scatterplot(titanic['age'], titanic['fare'], hue = titanic['sex'].values)
plt.title("Age vs Fare colored by sex")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()