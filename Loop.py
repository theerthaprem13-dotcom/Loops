# #Loop: It is used to repeat a block of code multiple times until a condition become false or all items are completed.
# Python has mainly two types of loops: for loop, while loop, nested loop.

# For loop: It is used when we know how many times we want to repeat something. 

# Signature:
# for variable in  sequence:
#     statement
for i in range(5):
    print("The value of i is",i)
for number in range(1,5):
    print("The value of number is",number)

for i in range(2,11,2):
    print("The value of step is", i)

#While loop: It repeats the code as long as the condition is true.

#Signature:while condition:
               # statement
number1=1

while number1<=5:
    print(number1)

    number1= number1+1

#Nested Loop: Ot means one loop inside another loop

for i in range(3):
    for j in range(2):
        print(i,j)


# #Syntax of while loop
# while condition:
#     statement

#Flow chart

# Start
# ↓
# Check Condition
# ↓
# True?
# ↓
# Run Code
# ↓
# Go back
# ↓
# Condition False
# ↓
# Stop


number2=1

while number2<=5:
    print("The number is", number2)
    number2=number2+1

#Assignement: ask the user to enter the correct password

password=""

attempt=1

while password!=1234:
    password=int(input("Enter your password:"))

    if password==1234:
        print("Login Successfull")
    else:
        print("Wrong password")
    
        attempt=attempt+1

    if password!=1234 and attempt>3:
        print("Account Locked")
    
    attempt1=1
    while True:
        password1=input("Enter your password:")

        if password1=="pythonabc":
            print("Login Sucessfull")
            break
        else:
            print("Wrong password")
        attempt1=attempt1+1
        if attempt1>3:
            print("Acount locked") 
            break





