# 1. Variables & Data Types 
name = "Athira"
age = 22
height = 5.4
is_student = True
print(name, age, height, is_student)
print("-" * 30)



#2. Operators
a = 10
b = 3
print(a + b)
print(a > b)
print(a % b == 1)
print("-" * 30)



# 3. If-Else 
num = -5
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
print("-" * 30)



# 4. List 
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[1])
print(len(fruits))
print("-" * 30)



# 5. Tuple
colors = ("red", "green", "blue")
print(colors[0])
print("green" in colors)
print("-" * 30)



# 6. Set 
nums = {1, 2, 2, 3, 4}
nums.add(5)
print(nums)
print("-" * 30)



# 7. Dictionary 
student = {"name": "Athira", "age": 24}
student["course"] = "Python"
print(student["name"])
print("-" * 30)



#  8. List Comprehension 
squares = [x*x for x in range(1, 6)]
print(squares)
print("-" * 30)



#9. File Handling 
with open("demo.txt", "w") as f:
    f.write("Hello, Athira!")

with open("demo.txt", "r") as f:
    print(f.read())
print("-" * 30)



# 10. Error Handling
try:
    a = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
print("-" * 30)




# 11. Function 
def square(n):
    return n * n
print(square(4))
print("-" * 30)



# 12. Loops 
for i in range(1, 4):
    print(i)
j = 1
while j <= 3:
    print(j)
    j += 1
print("-" * 30)



# 13. Class 
class Greet:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello", self.name)
g = Greet("Athira")
g.say_hello()
print("-" * 30)