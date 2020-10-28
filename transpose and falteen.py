import numpy
size1, size2 = list(map(int, input().split()))
l1 = []
for i in range(size1):
    user = list(map(int, input().split()))
    l1.append(user)
print(user[0])
print(user[1])
my_array = numpy.array([user[0], user[1]])
print(numpy.transpose(my_array))


my_array2 = numpy.array([user[0], user[1]])
print(my_array2.flatten())
