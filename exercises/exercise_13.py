# Your solution to Exercise 13
number=int(input("Enter a number (up to 9999):  "))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10
is_unique = (thousands != hundreds or thousands == 0 or hundreds == 0) and \
(thousands != tens or thousands == 0 or tens == 0) and \
(thousands != ones or thousands == 0) and \
(hundreds != tens or hundreds == 0 or tens == 0) and \
(hundreds != ones or hundreds == 0) and \
(tens != ones or tens == 0)
print(is_unique)


