#A string is text enclosed in quotation marks.

#A string method is an operation you can perform on a string. The basic syntax is:
#variable.method()

#For the following 3 methods assume that the name entered is "    rishit singh    "

#1 variable.strip() - removes whitespace from the beginning and end of a string.

name = input("Enter your name: ")
name = name.strip()
print(name) # Output will be "rishit singh"

#2 variable.lstrip() - removes whitespace from the beginning of a string.
name = input("Enter your name: ")
name = name.lstrip()
print(name) # Output will be "rishit singh    "

#3 variable.rstrip() - removes whitespace from the end of a string.
name = input("Enter your name: ")
name = name.rstrip()
print(name) # Output will be "    rishit singh"

#4 variable.upper() - Converts all letters to uppercase.
a = "hello, Rishit"
a = a.upper()
print(a) # Output "HEllO, RISHIT"

#5 variable.lower() - Converts all letters to lowercase.
a = "Hello, Rishit"
a = a.lower() 
print(a) # Output "hello, rishit"

#6 variable.capitalize() - Makes the first character uppercase and converts the remaining characters to lowercase.
b = "heLLo Python"
print(b.capitalize()) # Output "Hello python"

#7 variable.title() - Capitalizes the first character of each word and lowercases the other letters.
name = "riShit SINgh"
print(name.title()) # Output "Rishit Singh"

#8 variable.replace(...) - This method replaces one piece of text with another.
text = "I like Java"
print(text.replace("Java","Pyhton"))

text = "Python"
print(text.replace("o", "a")) # Output "Pythan"

text = "banana"
print(text.replace("a", "o", 2)) # Output "bonona"

#9 variable.split() - breaks a string into smaller pieces and returns a list.
data = "Maths Science SST"
print(data.split()) # Output ['Maths', 'Science', 'English'],

##We can specify a separator:

data = "Rishit,10,28"
print(data.split(",")) # Output ['Rishit', '10', '28']

a = "red-blue-green"
print(a.split("-")) # Output ['red', 'blue', 'green']

#10 variable.find() - returns the index (position) where a piece of text first appears.
name = "Rishit is a good boy"
print(name.find("Rishit")) # Output "0"

#11 variable.count() - tells you how many times a character or substring appears.
x = "banana"
print(x.count("a")) #Output "3"

#12 variable.startswith() - Checks whether a string begins with specific text.
text = "I am having a good day"
print(text.startswith("I")) #Output "True"
print(text.startswith("am")) #Output "False"

#13 variable.endswith() - Checks whether a string ends with specific text.
text = "I am having a good day"
print(text.endswith("day")) # Output "True"
print(text.endswith("a")) # Output "False"

#  FORMATTING SETTINGS
# f string - An f-string lets you insert variables or expressions directly into text.
name = "Rishit"
age = "15"
print(f"My name is {name} and I am {age} years old") # Output "My name is Rishit and I am 15 years old"

maths = 95
science = 90
print(f"Total marks: {maths + science}")  # Output "185"

# Formatting Decimal Places
percentage = 94.4444456
print(f"Percentage : {percentage:.2f}%") # Output "94.44"
#Here, .2f means display the number with two digits after the decimal point.

#format() - This is another way to insert values into a string.
name = "Rishit"
marks = 95
print("Name: {}, Marks: {}".format(name, marks)) #Name: Rishit, Marks: 95









