import sys
import os

# Numbers
num = 3.15

print(type(num))

num1 = "3"
num2 = 3

print(num1 != num2)
# List
courses = ["English", "Arts", "Science", "Math"]

for item in courses:
    print(item)
# Dictionary
student = {}

student.update(
    {"name": "manish", "age": 25, "cousrse": ["Eng", "Phy", "Chem", "Maths"]}
)

print(student)

for key, value in student.items():
    print(key, value)
# Conditions
language = "Go"

if language == "Python":
    print("Language is Python")
elif language == "Go":
    print("Language is Go")
else:
    print("No match")

l = {"a": "manish", "b": "sharma"}

if "c" in l:
    print("found")
else:
    print("not found")

# Iteration
for i in range(1, 11):
    print(i)

for i in l:
    print(l[i])
else:
    print("for else statement")


# Functions
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math", "Art"]
info = {"name": "Manish Sharma", "age": 38}

student_info(*courses, **info)


print(sys.path)

print(os.__file__)
