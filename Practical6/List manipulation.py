# create a list called marks to record all the marks and sort the list in ascending order
# draw a boxplot using matplotlib module
# explore some options to make the boxplot look better
# calculate the average and compare it with 60 to see whether he passes
import matplotlib.pyplot as plt  # import matplotlib module in python for plotting

marks = [45, 36, 86, 57, 53, 92, 65, 45]
marks.sort()  # sort the list in ascending order
print(marks)

# draw the boxplot of the marks
# put the median red, the box cyan and the edge black
plt.boxplot(marks,
            medianprops={'color': 'red'},
            boxprops={'facecolor': 'cyan', 'edgecolor': 'black'},
            patch_artist=True)
plt.title('boxplot for marks of Rob')  # add the boxplot a title
plt.ylabel('marks')
plt.xlabel('Student Rob')
plt.show()

# calculate the average of the 8 marks using loop
total = 0
for i in marks:
    total += i
average = total / len(marks)
print('The average mark Rob has received across the eight practicals is', str(average))
# determine whether the average is greater than 60 or not so to decide Rob passed or not
if average < 60:
    print("It's lower than the pass mark of 60%")
    print('Rob has not passed')
else:
    print("It's higher than the pass mark of 60%")
    print('Rob has passed')
