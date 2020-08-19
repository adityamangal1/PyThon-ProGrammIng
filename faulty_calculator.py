# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


# solution

var1 = int(input("ENTER YOUR FIRST number\n"))
var2 = int(input("ENTER YOUR SECOUND number\n"))

opp1 = input("NOW ENTER THE OPERATOR\n")
# opp2 = opp1

if var1 == 45 and var2 == 3 and opp1 == "*":
    print("YOU CHEATER\nYOUR ANSWER IS ", 555)
elif var1 == 56 and var2 == 9 and opp1 == "+":
    print("YOU CHEATER\nYOUR ANSWER IS ", 77)
elif var1 == 56 and var2 == 6 and opp1 == "/":
    print("YOU CHEATER\nYOUR ANSWER IS ", 4)
elif opp1 == "+":
    print("YOUR ANSWER IS ", var1 + var2)
elif opp1 == '/':
    print("YOUR ANSWER IS ", int((var1/var2)))
elif opp1 == '*':
    print("YOUR ANSWER IS ", var1 * var2)
else:
    print("HELLO")
