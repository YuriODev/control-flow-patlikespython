# Your solution to Exercise 7
n1=float(input("Enter first number:  "))
n2=float(input("Enter second number:  "))
operation=str(input("What operation do you want to use?   "))
if operation=="+":
  output=n1+n2
elif operation=="-":
  output=n1-n2
elif operation=="/":
  if n2==0:
    output="Division by 0!"
elif operation=="*":
  output=n1*n2
elif operation=="%":
  output=n1%n2
elif operation=="pow":
  output= n1**n2
elif operation=="div":
  output=n1//n2
else:
  output="Invalid operation"
print(output)
