#Tressure Island

#to understand conditional statements
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

user_input = input("You're at crossroad. where do you want to go?\n Type 'left' or 'right' - ").lower()
if user_input == "left":
      print("You've come to lake. There is an island in the middle of the lake.")
      user_input = input("Type 'wait' to wait for boat. Type 'swim' to swim across. - ").lower()
      if user_input =="wait":
            print("you arrived at the Island Unharmed")
            print("There is a house with 3 Doors. \nOne Red, One Yellow and One Blue")
            user_input = input("Which colour do you choose? \n ").lower()
            if user_input == "red":
                  print("It's a room full of Fire. \nGame Over!")
            elif user_input =="yellow":
                  print("Huhu, You found the tressure!\nYou win!")
            elif user_input=="blue":
                  print("you get attacked by an anger trout.\nGmae over!")
            else:
                  print("Door you entered does not exist")
      elif user_input =="swim":
            print("Sorry! you got eaten by crocodile. \n Game Over!")
      else:
            print("You pressed the wrong key!")
elif user_input == "right":
      print("OOPS! you got hit by bus. \n Game Over!")
else:
      print("You pressed the wrong key!")