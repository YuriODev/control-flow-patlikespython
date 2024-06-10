# Your solution to Exercise 9
digit=int(input("Enter a three-digit number:     "))
ones=digit%10
tens=(digit//10)%10
hundreds=digit//100
sum=ones+hundreds
if sum>tens:
  output=">"
elif sum<tens:
  output="<"
else:
  output="="
print(output)