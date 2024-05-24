# Your solution to Exercise 3
num=int(input("Enter a number from 0 to 36:   "))
if num==0:
  colour="green"
elif 1<=num<=10:
  if num%2==0:
    colour="black"
  elif num%2!=0:
    colour="red"
elif 11<=num<=18:
  if num%2==0:
    colour="red"
  elif num%2!=0:
    colour="black"
elif 19<=num<=28:
  if num%2==0:
    colour="black"
  elif num%2!=0:
    colour="red"
elif 29<=num<=36:
  if num%2==0:
    colour="red"
  elif num%2!=0:
    colour="black"
else:
  colour="The bet will not play!"
print(colour)

