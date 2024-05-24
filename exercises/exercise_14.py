# Your solution to Exercise 14
number=int(input("Enter a four-digit number:     "))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10
palindrome= (thousands==ones) and (hundreds==tens)
print(palindrome)