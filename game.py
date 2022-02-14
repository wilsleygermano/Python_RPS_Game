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

#Write your code below this line 👇
import random

plays = [rock, paper, scissors]

userChoices = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

pcChoice = random.randint(0, 2)

print(plays[userChoices], plays[pcChoice])

if userChoices == 0 and pcChoice == 2:
  print(f"Congratulations, {plays[userChoices]} beats {plays[pcChoice]}, you've won")
elif userChoices == 1 and pcChoice == 0:
  print(f"Congratulations, {plays[userChoices]} beats {plays[pcChoice]}, you've won")
elif userChoices == 2 and pcChoice == 1:
  print(f"Congratulations, {plays[userChoices]} beats {plays[pcChoice]}, you've won")
else:
  print(f"I am sorry, but {plays[pcChoice]} beats {plays[userChoices]}, you've lost")
