
class student:
    total_no = 60

    def __init__(self, argument, argument2, argument3):
        self.name = argument
        self.roll = argument2
        self.id = argument3

    def print_info(self):
        return f"The name of the student is '{self.name}', roll no is {self.roll} and the id is '{self.id}'."

    @classmethod
    def new_change(cls, argument4):
        cls.total_no = argument4

    @staticmethod
    def print_only(string):
        return f"Hello, how are you {string}?"

    def __add__(self, b):
        return self.roll + b.roll

    def __truediv__(self, argument5):
        return self.roll/argument5.roll

    def __mul__(self, var):
        return self.roll*var.roll


object1 = student("Aditya mangal", 333, '34e19')
object2 = student('mangal', 444, '43e0g')

# print(object1.print_info())
# print(object2.print_info())
# print(object1.print_only('Aditya mangal'))
print(object1 + object2)
print(object1 * object2)
# print(object1/object2)
