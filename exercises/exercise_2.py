# Your solution to Exercise 2
age=int(input("Enter your age:    "))
if age<=1:
  person="Infant"
elif 1<age<13:
  person="Child"
elif 13<=age<20:
  person="Teenager"
else:
  person="Adult"
print(person)

