print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")

direction = input("You are at a crossroads. Where do you want to go? Left or right? ")
lower_direction = direction.lower()
if lower_direction == "left":
  print("You've chosen good directon!")
  lake = input("Now you found a lake with an island in the middle of it. What do you want to do? Wait for a boat or swim? ")
  lower_lake = lake.lower()
  if lower_lake == "wait for a boat" or "wait":
    print("You've just escaped death!")
    door = input("Now you found a small cottage with three doors. Which door do you choose? Yellow, red or blue? ")
    lower_door = door.lower()
    if lower_door == "yellow":
      print("Hurray! You've escaped all the dangers! You win the game and get the treasure!")
     
    elif lower_door == "red":
      print("Oh no! You were burned by fire and died! GAME OVER!")
      
    else:
      print("You've chosen the wrong door! You were eaten a tiger! GAME OVER :(")
      
    
  else: 
    print("You got attacked by an alligator. GAME OVER :(")
   
  
else:
  print("It's a game over for you! You fall into a hole :(")