class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # Methods (Regular)
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # Methods (Regular)
    # Class variables that are shared by all instances
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): # 
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self): # readable object for the user
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Tom", "Hanks", 50000)
emp_2 = Employee("Brad", "Pitt", 80000)

# Uses __add__ method in the backend
print('Add emp1 + emp2')
print(emp_1 + emp_2)
print("")

# Prints out object
print(emp_1)

# Operators work differently based on different inputs
print(1+2) 
print('a'+'b')

print(repr(emp_1))
print(str(emp_1))
print(len(emp_1))
