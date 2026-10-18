#Project 1: Student Profile Generator
#Ask the user for their full name, class and favourite subject. Remove unwanted spaces, format the name, and display a polished profile.


name = input("Enter your full name: ").strip().lower().title()
age = int(input("Enter your age: "))
grade = input("Enter your class: ").strip()
subject = input("Enter your favourite subject: ").strip().lower().title()

print("------YOUR PROFILE------")

print("Name : ", name)

print("Age : ", age)

print("Class : ", grade)

print("Favourite Subject : ", subject)

print("------END OF YOUR PROFILE------")