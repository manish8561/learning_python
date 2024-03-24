# import os


try:
    f = open("testfile.txt")
    if f.name == "testfile.txt":
        raise Exception("Error while handling the file")  # throw exception
except FileNotFoundError as e:
    print("Sorry! This file doesn't exists.", e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally.....")
