from collections import OrderedDict

user = int(input())
mydict = OrderedDict()

for _ in range(user):
    string = input().split()
    item = ' '.join(string[:-1])
    money = int(string[-1])
    mydict[item] = mydict[item] + money if item in mydict.keys() else money
print(mydict)
for item, money in mydict.items():
    print('sfnsfeifneinf',item, money)

