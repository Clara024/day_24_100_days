import random
print ("Infinity Dice")
number= int(input("How many sides do you want the dice to have?:"))

game = "yes"

def rolldice(number):
  print ("You rolled",random.randint(1,number)) 

while True:
        rolldice(number)
        game = input("Do you want to play again?:")
        if game == "yes":
            continue
        else:
            print("Bye, see you soon!")
            break