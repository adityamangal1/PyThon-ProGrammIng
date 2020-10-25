from collections import OrderedDict

user = int(input())
mydict = OrderedDict()

for i in range(user):
    string = input().split()
    item = ' '.join(string[:-1])
    money = int(string[-1])
    if item in mydict.keys():
        mydict[item] = mydict[item] + money
    else:
        mydict[item] = money

print(mydict)
for item, money in mydict.items():
    print('sfnsfeifneinf',item, money)

