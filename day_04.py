#Rock Paper Scissor

#ask user to type 0 for Rock or 1 for Paper or 2 Scissors
'''
Rules of the Game
Rock beats the scissors
scissors beat the paper
paper beats the Rock'''

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_choices =[rock,paper,scissors]
user_choice = int(input("What you choose?\nType 0 for Rock, 1 for paper or 2 for Scissors: "))
#print(list_choices[user_choice])
#computer_choice = random.randint(0,2)
#print(list_choices[computer_choice])
if user_choice <=2:
      print("You choose:",list_choices[user_choice])
      computer_choice = random.randint(0,3)
      print("Computer choose:",list_choices[computer_choice])
      if user_choice == computer_choice:
            print("It's a draw")
      elif user_choice==0 and computer_choice==1:
            print("You loose!")
      elif user_choice==1 and computer_choice ==2:
            print("you loose!")
      elif user_choice ==2 and computer_choice == 0:
            print("you loose!")
      else:
            print("Huhu, You Won!")
else:
      print("Sorry you should have entered a number between 0 to 2")