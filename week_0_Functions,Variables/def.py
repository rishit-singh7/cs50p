#def function is used to create a customized function

def greet():
    print("Good, Morning")

greet()
print("End")


def greet(name):         
    print(f"Hello, {name}")

greet("Rishit")

def add(a, b):
    print(a+b)

result = add(27, 56) #Output is 83
print(result) #Output is none because it does not return a value

#Now to fix this we have to use return
def multiply(a, b):
    return(a * b)

x = multiply(56, 65)
print(x + 3)

# Build a calculator ehich divides two digits but with an exception that it cannot divide by 0

def divide(a,b):
    if b==0:
        return("Error, cannnot divide by zero")
    else:
        return(a/b)


x = divide(45,5)
y = divide(56,0)

print(x)
print(y)









    


