# Implement a recursive function to calculate the factorial of a given number 
print("\n THE FACTORIAL PROGRAM")
print("************************")
print("\n INPUT")
n=0
n=int(input("Enter the number:"))
print("\n OUTPUT")
def fact(f):
  if f==0:
    return 1
  else:
    return f* fact(f-1)
print("\n THE FACTORIAL VALUE IS",fact(n))
