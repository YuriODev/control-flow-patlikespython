# Your solution to Exercise 8
d1=int(input("Enter a three-digit number:    "))
d2=int(input("Enter a number:   "))
num=d2==d1%10 or d2==(d1//10)%10 or d2==d1//100
print(num)
