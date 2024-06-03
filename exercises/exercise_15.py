# Your solution to Exercise 15
day=int(input("Enter a day:    "))
month=int(input("Enter a month:   "))
year=int(input("Enter a year:     "))

check_leap = (year%4==0 and year%100!=0) or (year%400==0)

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
  if day < 31:
    day+=1
  else:
    day=1
    month+=1
  print(f"{day}.{month}.{year}")
elif month==4 or month==6 or month==9 or month==11:
  if day<30:
    day+=1
  else:
    day=1
    month+=1
  print(f"{day}.{month}.{year}")
elif month==2:
  if check_leap is True:
    if day<29:
      day+=1
    else:
      day=1
      month+=1
    print(f"{day}.{month}.{year}")
  elif check_leap is False:
    if day<28:
      day+=1
    else:
      day=1
      month+=1
    print(f"{day}.{month}.{year}")
elif month==12:
  if day<31:
    day+=1
  elif day==31:
    day=1
    month=1
    year+=1
  print(f"{day}.{month}.{year}")
else:
  print("Invalid date")


