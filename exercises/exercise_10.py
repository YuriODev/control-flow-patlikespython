# Your solution to Exercise 10
x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
x3, y3 = int(input("Enter x3: ")), int(input("Enter y3: "))
a2 = (x2-x1)**2 + (y2-y1)**2
b2 = (x3-x2)**2 + (y3-y2)**2
c2 = (x1-x3)**2 + (y1-y3)**2
if a2==0 or b2==0 or c2==0:
  print("No")
elif a2+b2==c2 or b2+c2==a2 or c2+a2==b2:
  print("yes")
else: 
  print("no")
  
  