# Run a simple script to determine if CJ should be in kindergarten

from tkinter.tix import InputOnly


K_age = 5

print ("Let's figure out if Cora should be in preschool or kindergarten.")

#Asking the user for input on how old Cora is

Cj_age = input("How old is Cora? ") 

#Converting input from string class to integer since age is a number.

Cj_age = int(Cj_age)

print ("She is " + str(Cj_age) + " years old.")

input ("Press ENTER to continue...")

if Cj_age < K_age:
  print ("She's too young for kindergarten, and she's probably in preschool.")
elif Cj_age == K_age:
  print ("I'm sure she's having a great day in kindergarten.")
elif Cj_age > K_age:
  print ("To infinity and beyond!!!") 