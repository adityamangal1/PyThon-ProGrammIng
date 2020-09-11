harry_restaurant = ['burger', 'chowmein', 'noodles',
                    'chilli', 'manchurian', 'chaat', 'pizza']

print(harry_restaurant[::-1])


harry_restaurant[0], harry_restaurant[6] = harry_restaurant[6], harry_restaurant[0]
harry_restaurant[1], harry_restaurant[5] = harry_restaurant[5], harry_restaurant[1]
harry_restaurant[2], harry_restaurant[4] = harry_restaurant[4], harry_restaurant[2]


print(harry_restaurant)
