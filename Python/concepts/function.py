# sep & end
name = "linuxdex"
age = 23 

print("My name is ", name, "and i am ", age, "years old ", sep="|")

print("hello world", end=" | ")
print("I am", name)

# ----------
# help()
help(print)

def test_func(a, b):
    """
    a: value 1
    b: value 2 

    returns: int
    """
    return a + b

help(test_func)

# ----------
# range()

# rng = range(10)
rng = range(2, 10, 2)

print(list(rng))

# ---------
# map()

strings = [ "my", "world", "apple", "pear" ]

# lengths = map(len, strings)
lengths = map(lambda x: x + "s", strings)

print(list(lengths))

# ---------
# filter()

def longer_than_4(string):
    return len(string) > 4 

stringVal = [ "my", "world", "apple", "pear" ]

filtered = filter(longer_than_4, strings)
print(list(filtered))

# ---------
# sum()

numbers = { 1, 4, 5, 23, 2 }
print(sum(numbers)) # the sum from 0
print(sum(numbers, start=10)) # the sum from 10

# ------------
# sorted()

numberList = [ 4, 5, 2, 3, -1, 0, 9 ]
# sorted_nums = sorted(numberList) 
sorted_nums = sorted(numberList, reverse=True)

print(sorted_nums)

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20}
]

soted_people = sorted(people, key=lambda person: person["age"])

print(soted_people)

# -------------
# enumerate()

tasks = ["Write report", "Attend meeting", "Review code", "Submit timesheets"]

# for index in range(len(tasks)):
#     task = tasks[index]
#     print(f"{index + 1}. {task}")

for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

print(list(enumerate(tasks)))

# -------------
# zip

names = ["Alice", "Bob", "Charlie", "David", "Tim"]
ages = [30, 25, 35, 20]

combined = list(zip(names, ages))

for name, age in combined:
    print(f"{name} is {age} years old")

# -------------
# open()

file = open("test.txt", "w")
file.write("hello world\nmy name is linuxdex")
file.close()

with open("test.txt", "a") as file: 
    text = file.read()
    print(text)
