# Your solution to Exercise 16
day=int(input("Enter a day:    "))
month=int(input("Enter a month:   "))
year=int(input("Enter a year:     "))

check_leap = (year%4==0 and year%100!=0) or (year%400==0)

