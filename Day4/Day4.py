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
computer_choice = random.randint(0, 2)

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")


if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
elif player_choice == "2":
    print(scissors)
else:
    print("Please follow the rules of the game.")


if computer_choice == "0":
    print(paper)
elif computer_choice == "1":
    print(scissors)
elif computer_choice == "2":
    print(rock)
