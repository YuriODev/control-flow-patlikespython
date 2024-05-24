# Your solution to Exercise 17
number=int(input("Enter a six digit number:     "))
ones=number%10
tens=(number//10)%10
hundreds=(number//100)%10
thousands=(number//1000)%10
ten_thousands=(number//10000)%10
hundred_thousands=number//100000
first=hundred_thousands+ten_thousands+thousands
second=hundreds+tens+ones
if first==second:
  output="happy"
else:
  output="ordinary"
print(output)