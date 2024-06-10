# Your solution to Exercise 4
grade=int(input("Enter your grade:     "))
if 1<=grade<=3:
  output="Intial level"
elif 4<=grade<=6:
  output="Average level"
elif 7<=grade<=9:
  output="Sufficient level"
elif 10<=grade<=12:
  output="High level"
else:
  grade="Level is absent"
print(output)

