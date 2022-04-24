#Attempting to create a table that houses family member names and ages
import random

def family_number():
  
  members = input("Please enter your families names seperated by a space ") #establish how many people are in the family
  list = members.split()
  print(type(list))
  person = random.choice(list)
  age = input("How old is " + person +" " )
  #person_age = person += age
  print("Wow! "+person+" is " + age + " years old!")
  #print(person_age)

family_number()


