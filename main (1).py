print("*****SIMPLE CALCULATOR****\n")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("\nEnter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for normal divsion\nEnter 5 for remainder\n")

c = int(input("Enter your choice here: "))

if(c==1):
  print("Addition of",a,"and",b,"is = ",a+b)
elif(c==2):
  print("Subtraction of",a,"and",b,"is =",a-b)
elif(c==3):
  print("Multiplication of",a,"and",b,"is =",a*b)
elif(c==4):
  print("Division of",a,"and",b,"is =",a/b)
elif(c==5):
  print("Remainder of",a,"and",b,"is =",a%b)
else:
  print("INVALID")

