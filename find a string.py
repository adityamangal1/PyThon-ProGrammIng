
'''
Author: Aditya Mangal 
Date:  5 october,2020
Purpose: python practise problem

'''


def count_substring(string, sub_string):

    count = 0
    big = 0
    while (big < len(string)):

        x = string.find(sub_string)
        if x != -1:
            big = x + 1
            count += 1

        else:
            break

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
