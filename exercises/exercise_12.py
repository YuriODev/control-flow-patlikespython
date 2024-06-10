# Your solution to Exercise 12
number=int(input("Enter a four-digit number:     "))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10

thousands = '*' if thousands % 2 == 0 else str(thousands)
hundreds = '*' if hundreds % 2 == 0 else str(hundreds)
tens = '*' if tens % 2 == 0 else str(tens)
ones = '*' if ones % 2 == 0 else str(ones)

result=thousands+hundreds+tens+ones
print(result)
  
