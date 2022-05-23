# input and Turn list paternal_age and list chd into a dictionary
# let the values in the same position in each list correspond to each other
# draw a scatter plot use matplotlib module
# print the corresponding risk rate for a certain age input by the user
import matplotlib.pyplot as plt  # import matplotlib module in python for plotting

paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]  # create two list recording the input data
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
# the code in the next line was obtained from https://stackoverflow.com/questions/44374540/cant-merge
# -two-lists-into-a-dictionary on 22/03/22
# This Python builtin zip() returns an iterable of tuples from each of the arguments.
# Then give this to the dict() create a dictionary where each of the items in paternal_age is the key
# and items in chd is the corresponding value.
dictionary = dict(zip(paternal_age, chd))
print(dictionary)

plt.scatter(paternal_age, chd, marker='o', color='blue')  # draw a scatter plot with blue dot
plt.xticks(paternal_age)  # set label locations with the items in the list input
plt.yticks(chd)
plt.grid()  # add a grid in the background
plt.title('The risk of congenital heart disease in the offspring of a father along with age')
plt.xlabel('age of the father')
plt.ylabel('numbers relative to offspring with a 25-year-old father')
plt.show()

age = int(input('the age you want to search:'))  # where the user can input the age they want to check
# here turn age into int since the keys in the dictionary are all int
risk = dictionary[age]  # find the certain risk rate according to the age input
print('the relative risk of congenital disease for '+str(age)+'-year-old father is '+str(risk))
