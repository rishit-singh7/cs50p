##sep stands for separator. It decides what Python should place between multiple values in a single print() statement.
## By default, the separator is a space. You can change it by using the sep parameter in the print() function.

print("Hello,","World")
## The output will be: Hello, World

print("Hello" , "World", sep="-")
## The output will be: Hello-World

print("Rshit","is","learning","Python", sep="-")
## The output will be: Rshit-is-learning-Python



##  end controls what Python prints at the end of a print() statement.
## By default, the end parameter is a newline character (\n). You can change it by using the end parameter in the print() function.


print("Hello")
print("World")
## The output will be:
## Hello
## World

print("Hello", end=" ")
print("World")
## The output will be: Hello World

print("Loading", end="...")
print("Done")
## The output will be: Loading...Done


##Practice project: Build a mini student dashboardPractice project: Build a mini student dashboard

print("-----STUDENT DASHBOARD-----")
print("Name: Rishit")
print("Roll Number: 28")
print("Class: 10th")
print("Subjects:", "Maths","Science", "English", sep= "|")
print("Marks:", 99,96,88,sep= "|")

maths = 99 
science = 96
english = 88
total = maths + science + english
print("Percentage:", total/300*100, "%", sep= "")
print("-----END OF DASHBOARD-----")
