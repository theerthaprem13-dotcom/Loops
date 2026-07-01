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