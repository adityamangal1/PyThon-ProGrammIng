from collections import Counter


def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key


user = list(map(int, input().split()))
my_dict = Counter(user)
b = min(my_dict.values())
print(get_key(b))
