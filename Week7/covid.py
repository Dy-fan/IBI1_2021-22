import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\cygwin64\home\yifan.21\IBI1_21-22\IBI1_2021-22\Practical7")
covid_data = pd.read_csv('full_data.csv')
print('the first and third columns from rows 10-20: ')
print(covid_data.iloc[10:21, [0, 2]])  # showing the first and third columns from rows 10-20 (inclusive)
print('\ntotal cases for all rows corresponding to Afghanistan:')
print(covid_data.loc[covid_data['location'] == "Afghanistan", "total_cases"])
# show total cases for all rows corresponding to Afghanistan
china_new_data = covid_data.loc[covid_data['location'] == 'China', ['date', 'new_cases', 'new_deaths']]
# the mean number of new cases and new deaths in China.
m_cases = np.mean(china_new_data['new_cases'])
m_deaths = np.mean(china_new_data['new_deaths'])
print(f'The mean number of new cases in China is {m_cases}')
print(f'The mean number of new deaths in China is {m_deaths}')
china_dates = china_new_data['date']
china_new_cases = china_new_data['new_cases']
china_new_deaths = china_new_data['new_deaths']

# a boxplot of new cases and new deaths in China worldwide
plt.subplot(211)
plt.boxplot([china_new_cases, china_new_deaths], labels=['new cases', 'new deaths'])
plt.title('new cases and new deaths in China')
plt.ylabel('numbers')
plt.yscale('log')

# a plot of both new cases and new deaths in China over time
plt.subplot(212)
plt.plot(china_dates, china_new_cases, 'r')
plt.plot(china_dates, china_new_deaths, 'b')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.xlabel('dates')
plt.ylabel('numbers')
plt.legend(['new cases', 'new deaths'])
plt.title('new cases and new deaths in China over time')
plt.show()

# The code to answer the question
low_infections = covid_data.loc[
    (covid_data['total_cases'] <= 10) & (covid_data['date'] == '2020-03-31'), ['location', 'total_cases']]
countries = list(low_infections['location'])
if len(countries) > 0:
    print(f'\nAnswer for the chosen question:\nYes, there places in theWorld '
          f'where there have not yet been more than 10 total infections. The places are as followed in the list. '
          f'The number of them is {len(countries)}. ')
    print(countries)

