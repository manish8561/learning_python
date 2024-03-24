# OOPS in Python


class Employee:
    num_of_emps = 0
    raise_amounnt = 1.2

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + "." + last.lower() + "@company.com"

        Employee.num_of_emps += 1

    @property
    def email(self) -> str:
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name) -> None:
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amounnt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amounnt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self) -> str:
        return f"Employee('{self.first}','{self.last}',{self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"

    def __add__(self, other) -> int:
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.fullname)


class Developer(Employee):
    raise_amounnt = 1.4

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employess=None) -> None:
        super().__init__(first, last, pay)
        if employess is None:
            self.employees = []
        else:
            self.employees = employess

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname)


dev_1 = Developer("Manish", "Sharma", 1900000, "Python")
dev_2 = Developer("Rajesh", "Kumar", 1350000, "Java")

print(dev_1)

print(dev_1 + dev_2)

# print(repr(dev_1))
# print(str(dev_1))

print(dev_1.__repr__())
print(dev_1.__str__())

mgr_1 = Manager("Sue", "Smith", 2600000, [dev_1])
print(mgr_1.fullname)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


# print(emp1)
# print(emp2)

# print(emp1.email)
# print(emp2.email)

print(dev_1.fullname)
print(dev_1.prog_lang)

dev_1.fullname = "Maddy Shastri"
print(dev_1.fullname)

del dev_1.fullname
print(dev_1.fullname)

# print(Employee.fullname(dev_2))

Employee.raise_amounnt = 1.6
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

print(Employee.num_of_emps)

print(Employee.raise_amounnt)
print(dev_1.raise_amounnt)
print(dev_2.raise_amounnt)
# print class dict
# print(Employee.__dict__)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
