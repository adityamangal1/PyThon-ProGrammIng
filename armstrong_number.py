
def find_armstrong(number):
    sum = 0
    order = len(str(number))
    copy_num = number
    while(number > 0):
        n = number % 10
        sum += n ** order
        number = number // 10

    if (sum == copy_num):
        print(f'{copy_num} is an armstrong number.')

    else:
        print(f'{copy_num} is not an armstrong number.')


if __name__ == '__main__':
    user = int(input("Enter your number.\n"))
    find_armstrong(user)
