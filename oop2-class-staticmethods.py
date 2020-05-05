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

    @classmethod  # decorator
    # altering the functionality of the method where now it receives the class as the 1st argument vs. an instance
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    # if you do not access the instance or the class in the method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            False
        return True


emp_1 = Employee("Tom", "Hanks", 50000)
emp_2 = Employee("Brad", "Pitt", 80000)

# Change raise amt to 1.05 from 1.04
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# print(emp_1.fullname()) # method requires the () at the end
# print(Employee.fullname(emp_1))
# print(Employee.__dict__)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "John-Doe-90000"

first, last, pay = emp_str_1.split("-")

new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_1 = Employee.from_string(emp_str_1)
print(emp_str_1)
print(new_emp_1.email)

import datetime

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
