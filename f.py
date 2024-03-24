class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return f"({self.name},{self.age},{self.salary})"


from operator import attrgetter

e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]


# def e_sort(emp):
#     return emp.age


s_employees = sorted(employees, key=attrgetter("age"))

print(s_employees)
