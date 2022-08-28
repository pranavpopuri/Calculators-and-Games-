import random

#anything random here

z = input("Do you want to play against Jeff(easy), Joe(normal), Jim (hard) or Jay(extended game)?")

print("You are playing against" + " " + z)

hp = 2

botHp = 2

if z == "Jeff" or z == "jeff":
    print ("Your health has increased by 2")
    hp += 2

if z == "Jim" or z == "jim":
    print ("Opponent's health has increased by 1")
    botHp +=1

if z == "Jay" or z == "jay":
    print ("Opponent's health has increased by 3")
    print("Your health has increased by 3")
    hp += 3
    botHp +=3

for i in range(0, 100):
    y = input ("Rock, Paper, or Scissors?")
    y = y.lower()
    
    x =("Rock", "Paper", "Scissors")  
    x =(random.choice(x))

 

    if y =="rock" and x == "Scissors":
        print (z + " chose Scissors")
        print("You Win!")
        print ("Your health is at " + str(hp))
        botHp -= 1
        print ("Your opponent's health is at " + str(botHp))

    if y =="rock" and x == "Paper":
        print (z + " chose Paper")
        print("You Lose!")
        hp -= 1
        print ("Your health is at " + str(hp))
        print ("Your opponent's health is at " + str(botHp))

    if y == "rock" and x == "Rock":
        print (z + " chose Rock")
        print("Tie!")
        print ("Your health is at " + str(hp))
        print ("Your opponent's health is at " + str(botHp))

    if y == "paper" and x == "Rock":
        print (z + " chose Rock")
        print("You Win!")
        print ("Your health is at " + str(hp))
        botHp -= 1
        print ("Your opponent's health is at " + str(botHp))

    if y == "paper" and x == "Scissors":
        print (z + " chose Scissors")
        print("You Lose!")
        hp -= 1
        print ("Your health is at " + str(hp))
        print ("Your opponent's health is at " + str(botHp))

    if y == "paper" and x == "Paper":
        print (z + " chose Paper")
        print("Tie!")
        print ("Your health is at " + str(hp))
        print ("Your opponent's health is at " + str(botHp))

        
    if y =="scissors" and x == "Paper":
        print (z + " chose Paper")
        print("You Win!")
        print ("Your health is at " + str(hp))
        botHp -= 1
        print ("Your opponent's health is at " + str(botHp))
        

    if y =="scissors" and x == "Rock":
        print (z + " chose Rock")
        print("You Lose!")
        hp -= 1
        print ("Your health is at " + str(hp))
        print ("Your opponent's health is at " + str(botHp))

    if y =="scissors" and x == "Scissors":
        print (z + " chose Scissors")
        print("Tie!")
        print ("Your health is at " + str(hp))
        print ("Your opponent's health is at " + str(botHp))

    if y =="god_mode" and (x == "Scissors" or x == "Paper" or x == "Rock"):
        botHp = 0

    if hp == 0:
        print ("You have lost the rock paper scissors battle!")
        break 

    if botHp == 0:
        print ("You have won the rock paper scissors battle!")
        break

            


            

              
