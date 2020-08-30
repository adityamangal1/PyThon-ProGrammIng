
# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     def __add__(self, other):
#         return self.salary + other.salary

#     def __truediv__(self, other):
#         return self.salary / other.salary

#     def __repr__(self):
#         return f"Employee('{self.name}', {self.salary}, '{self.role}')"

#     def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
# # print(repr(emp1))
# print(emp1 + emp2)

class student:
    total_no = 60

    def __init__(self,argument,argument2,argument3):
        self.name = argument
        self.roll = argument2
        self.id = argument3
    
    def print_info(self):
        return f"The name of the student is '{self.name}', roll no is {self.roll} and the id is '{self.id}'."


    @classmethod
    def new_change(cls,argument4):
        cls.total_no = argument4

    @staticmethod
    def print_only(string):
        return f"Hello, how are you {string}?"

    def __add__(self,b):
        return self.roll + b.roll
    
    def __truediv__(self,argument5):
        return self.roll/argument5.roll

    def __mul__(self,var):
        return self.roll*var.roll


object1 = student("Aditya mangal",333,'34e19')
object2 = student('mangal',444,'43e0g')

# print(object1.print_info())
# print(object2.print_info())
# print(object1.print_only('Aditya mangal'))
print(object1 + object2)
print(object1 * object2)
# print(object1/object2)


