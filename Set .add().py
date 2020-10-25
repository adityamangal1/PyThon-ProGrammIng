user = int(input())
cityz_list = []
for i in range(user):
    user_cities = input()
    cityz_list.append(user_cities)
cityz_list = len(set(cityz_list))
print(cityz_list)