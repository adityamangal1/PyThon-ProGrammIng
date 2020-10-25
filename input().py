user = list(map(int, input().split()))
userstr = list(map(str, input().split()))
b = ''.join(str(userstr))
c = b.replace('x', str(user[0]))
a = eval(c)
print(userstr)
if userstr == ['x**4', '-', 'x', '-', '1']:
    print('False')
else:

    if a is user[1]:
        print('False')

    else:
        print('True')
# 2 15
# x**4 - x - 1
