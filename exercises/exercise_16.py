# Your solution to Exercise 16


day=int(input("Enter a day:    "))
month=int(input("Enter a month:   "))
year=int(input("Enter a year:     "))

leap_year = (year%4==0 and year%100!=0) or (year%400==0)

if month==1:
  if 1<day<=31:
    day-=1
  elif day==1:
    day=31
    month=12
    year-=1

elif month==5 or month==7 or month==8 or month==10 or month==12:
  if day<=31:
    day-=1
  elif day==1:
    day=30
    month-=1
    
elif month==3:
  if 1<day<=31:
    day-=1
  elif day==1:
    if leap_year is True:
      day=29
      month-=1
    elif leap_year is False:
      day=28  
      month-=1
      
if month==4 or month==6 or month==9 or month==11:
  if 1<day<=30:
    day-=1
  elif day==1:
    day=31
    month-=1
    
print(f"The previous date is {day}.{month}.{year}")