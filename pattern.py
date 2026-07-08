#Pattern:It is the arrangement of charachters,numbers or symbols in a specific shape using loops

for i in range(1,6):
    print("*"*i)

#Assignement 1

print("Half pyramid pattern")

n=int(input("Enter the number of rows:"))

for i in range(n+1):
    print("*"*i)

#Assignement 2 : Pattern for diamond

#take input from user
rowSize = int(input("enter the number of rows: "))

if rowSize%2==0: #conditions
  halfDiamRow = int(rowSize/2)
else:
  halfDiamRow = int(rowSize/2)+1 #Value:4
space = halfDiamRow-1            #Value:3

#loop for upper part

for i in range(1, halfDiamRow+1): #loop for rows
  for j in range(1, space+1): #loop for columns
    print(end=" ")
  space = space-1
  num = 1
  for j in range(2*i-1):
    print(end=str(num))
  #incerementing number at each column
    num = num+1
  print()
space = 1
#loop for lower part
for i in range(1, halfDiamRow): #loop for rows
  for j in range(1, space+1):  #loop for columns
    print(end=" ")
  space = space+1
  num = 1
  for j in range(1, 2*(halfDiamRow-i)):
    print(end=str(num)) #display result
  #incerementing number at each column
    num = num+1
  print()





