# Your solution to Exercise 1
alex=int(input("Enter Alex's age:   "))
tatyana=int(input("Enter Tatyana's age:    "))
if alex>tatyana:
  output="Alex is the eldest"
elif alex==tatyana:
  output="Alex and Tatyana are of the same age"
elif tatyana>alex:
  output="Tatyna is the eldest"
else:
  output="Invalid input"
print(output)