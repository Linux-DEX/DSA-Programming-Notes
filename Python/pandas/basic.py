import pandas as pd 

df = pd.read_csv('sample1.csv') # reading csv file

print(df.to_string() , '\n') # use to print dataframe
print(pd.__version__, '\n') # print panda version

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset) # convert the dictionary to DataFrame
print("data frame - ", myvar, '\n')

# Series - one-dimensional array holding data of any type.
a = [ 1, 7, 2 ]
myvar = pd.Series(a)
print('Series -', myvar , '\n')
# output
# 0 1
# 1 7 
# 2 2

myvar = pd.Series(a, index = ["x", "y", "z"]) # adding x,y,z as labels
print(myvar)
print(myvar["y"], '\n')
# output
# x 1
# y 7 
# z 2

# key/value object series
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print('key/value object series')
print(myvar, '\n')

myvar = pd.Series(calories, index=['day1', 'day2'])
print(myvar, '\n')

# DataFrame 
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data) #load data into a DataFrame object:
print(df, "\n")
# output
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45

print(df.loc[1]) # locate row

df = pd.DataFrame(data, index = ["day1", "day2", "day3"]) # named indexes - DataFrame
print(df, '\n')

# csv files 
df = pd.read_csv('sample1.csv') # reading csv file

print(df.to_string() , '\n') # to print dataframe
# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame
pd.options.display.max_rows = 9999

# json file

pjd = pd.read_json('sample2.json')
print(pjd.to_string(), '\n')

# analyzing data frame 
df = pd.read_csv('sample1.csv')

print(df.head(2), '\n') # The head() method returns the headers and a specified number of rows, starting from the top.

print(df.head(), '\n')
print(df.tail(2), '\n') # The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.info()) # information about the data 
