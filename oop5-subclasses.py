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


# Inheritance
class Developer(Employee):
    # Creating Subclasses
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # let employee class handle
        self.prog_lang = prog_lang


# Inheritance
class Manager(Employee):
    # Creating Subclasses
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # let employee class handle
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Tom", "Hanks", 50000, "Python")
dev_2 = Developer("Brad", "Pitt", 80000, "Java")

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

print("isinstance")
print("Manager:  " + str(isinstance(mgr_1, Manager)))
print("Developer:" + str(isinstance(mgr_1, Developer)))
print("Employee: " + str(isinstance(mgr_1, Employee)))

print("issubclass")
print("Developer, Employee: " + str(issubclass(Developer, Employee)))
print("Manager, Developer : " + str(issubclass(Manager, Developer)))
print("Manager, Employee  : " + str(issubclass(Manager, Employee)))
