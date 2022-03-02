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
computer_choice = (random.randint(0, 2))

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))


if player_choice == 0:
    print(f"You chose Rock {rock}")
elif player_choice == 1:
    print(f"You chose Paper {paper}")
elif player_choice == 2:
    print(f"You chose Scissors {scissors}")
else:
    print("Please follow the rules of the game.")
    quit()


if computer_choice == 0:
    print(f"Computer chose rock {rock}")
elif computer_choice == 1:
    print(f"Computer chose paper {paper}")
elif computer_choice == 2:
    print(f"Computer chose Scissors {scissors}")

if computer_choice == 0 and player_choice == 2:
    print("You Lose")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice > computer_choice:
    print("You win")
elif player_choice == computer_choice:
    print("Its a draw")
else:
    print("You lose")
