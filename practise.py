# # example string
# string = 'cat'
# width = 5

# print right justified string
# print(string.rjust(width))
# print(string.rjust(width))


# # example string
# string = 'cat'
# width = 5
# fillchar = '*'

# # print right justified string
# print(string.rjust(width, fillchar))


# # .centre function
# string = "Python is awesome"

# new_string = string.center(24)
# print(string.center(24))

# print("Centered String: ", new_string)
# print(new_string)

# s = input()
# list1 = [word.capitalize() for word in s.split(' ')]
# a = ' '.join(list1)
# print(a)
# print(list1)
size = 5
a = list(map(chr, range(97, 122)))
m = a[size-1::-1] + a[:size]
print(m)
