# OOP

# Why use classes?
# It logically group our data and functions in a way that is easy to use and build upon if need be

# Attributes and Methods
# Methods is a function associated with a class

# Use Case for Class (Blueprint):
# Each employee will have specific attributes and methods (name, pay), so no need to manually create for each new employee
class Employee:

    raise_amt = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1

    # Methods (Regular)
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # Methods (Regular)
    # Class variables that are shared by all instances
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

print(Employee.num_of_emp)

emp_1 = Employee("Tom", "Hanks", 50000)
emp_2 = Employee("Brad", "Pitt", 80000)

# Apply raise amt of 1.04
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(Employee.num_of_emp)

print("Employee Emails")
print(emp_1.email)
print(emp_2.email)

# print(emp_1.fullname()) # method requires the () at the end
# print(Employee.fullname(emp_1))

print("Employee 1 pay:")
print(emp_1.pay)
print("Apply Raise of", Employee.raise_amt, "%")
emp_1.apply_raise()
print("Employee 1 revised pay:")
print(emp_1.pay)
