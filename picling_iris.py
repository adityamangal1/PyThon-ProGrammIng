import pickle
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
a = requests.get(url).text
# data = a.splitlines()
list1 = a.split("\n")
final_list = [items.split(',') for items in list1 if items != 0]
print(final_list)

