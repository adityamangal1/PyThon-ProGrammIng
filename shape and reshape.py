import numpy
user = list(map(int ,input().split()))
my_array = numpy.array([user])
print(numpy.reshape(my_array, (3,3)))