# let n increase by 1 every loop
# break the loop when p = 64
# print all the result
n = 0
p = 1
while p < 64:
    n += 1
    p = (n ** 2 + n + 2) / 2
    p = int(p)
    print(str(p)+' pieces of pizza can be cut for '+str(n)+' straight cuts')
print('Now we have enough pieces for each member in IBI1 class')
