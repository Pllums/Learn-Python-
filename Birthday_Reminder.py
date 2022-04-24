#Create a simple script that when prompted will be able to tell me a given person's birthday

#define the function for how I am asking for the birthday

def bday ():
  family = input ("Way to go... What birthday list do I need to load? ")

#defining the different lists for families

  elwood = ("09/07/1988 07/10/1988 10/25/2018 02/03/2021") #Jesse , Stephanie , Easton , Oliver birthdays respectively
  elwood_list = elwood.split()

  smolenski = ("05/28/1988 11/02/1988 12/20/2018 12/29/2020") #Tim , Chelsea , Margo , Mia birthdays respectively
  smolenski_list = smolenski.split()

  bierman = ("12/12/1990 08/25/1992 05/23/2017") #Jake , Samantha , Theo birthdays respectively
  bierman_list = bierman.split()

  abdullah = ("11/22/1994 07/06/1993 07/10/2017 09/16/2020") # Arik , Alyssa , Cora , Isaac birthdaays respectively
  abdullah_list = abdullah.split()
  
  #Actually asking the user for input regarding whose birthday they forgot
  if family == "Elwood":  #Elwood questions
    elwood_list
    person = input("Which birthday do you need help remembering? ")
    if person == "Jesse":
      print(elwood_list[0])
    elif person == "Stephanie":
      print(elwood_list[1])
    elif person == "Easton":
      print(elwood_list[2])
    elif person == "Oliver":
      print(elwood_list[3])
    
  
  elif family == "Smolenski":  #Smolenski questions
    smolenski_list
    person = input("Which birthday do you need help remembering? ")
    if person == "Tim":
      print(smolenski_list[0])
    elif person == "Chelsea":
      print(smolenski_list[1])
    elif person == "Margo":
      print(smolenski_list[2])
    elif person == "Mia":
      print(smolenski_list[3])

  elif family == "Bierman":  #Bierman questions
    bierman_list
    person = input("Which birthday do you need help remembering? ")
    if person == "Jake":
      print(bierman_list[0])
    elif person == "Samantha":
      print(bierman_list[1])
    elif person == "Theo":
      print(bierman_list[2])
    elif person == "":
      print(bierman_list[3])
      
  elif family == "Abdullah":  #Abdullah questions
    abdullah_list
    person = input("Which birthday do you need help remembering? ")
    if person == "Arik":
      print(abdullah_list[0])
    elif person == "Alyssa":
      print(abdullah_list[1])
    elif person == "Cora":
      print(abdullah_list[2])
    elif person == "Isaac":
      print(abdullah_list[3])
     
bday()





















