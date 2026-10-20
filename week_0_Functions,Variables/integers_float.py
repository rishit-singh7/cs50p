x = int(input("Enter the first number: "))

y = int(input("Enter thr second number: "))

z = x + y
print(z)

# Float are the numbers with decimals
# Round is a built in function which rounds off the output

a = float(input("Enter the number: "))
b = float(input("Enter the number: "))
c = round(a + b)
print(c)

# Division with output of just 2 places after the decimal
p =  float(input("Enter the number: "))
q =  float(input("Enter the number: "))

# there are two ways to print it one by f string and the other by round function

s = round(p/q,2)
print(s)
#OR
print(f"{s:.2f}")

#now to add comma in the output we have to use the f string

p =  float(input("Enter the number: "))
q =  float(input("Enter the number: "))

print(f"{p+q:,}")
