a = 19245301  # total cases of 2022
b = 4218520  # total cases of 2021
c = 271  # total cases of 2020
d = b-c  # 2021-2020
e = a-b  # 2022-2021
# compare d to e
if d > e:
    print('d is greater than e')
else:
    print('e is greater than d ')
# 2022 has the greatest number of new COVID-19 cases
x = bool(input('x:'))  # input 2 boolean value
y = bool(input('y:'))
w = x and y
print(w)
