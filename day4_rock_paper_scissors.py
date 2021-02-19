'''
I designed this game to be able to understand logical operators better and their uses
'''

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


human_selection  = int(input("Type '0' for rock, '1' for paper or '2' for scissors.\n"))


print(f"You have selected: {human_selection} ")

if human_selection == 0:
  print(rock)
elif human_selection == 1:
  print(paper)  
else:
  print(scissors)



import random
computer_selection = random.randint(0, 2)
print(f"The computer has selected: {computer_selection}")

if computer_selection == 0:
  print(rock)
elif computer_selection == 1:
  print(paper)  
else:
  print(scissors)

r = 0
p = 1
s = 2

if human_selection == computer_selection:
  print("It's a tie. Try again!!!")
elif human_selection == r and computer_selection == s:
  print("You win")
elif human_selection == s and computer_selection == p:
  print("You win")
elif human_selection == p and computer_selection == r:
  print("You win")
elif computer_selection  == s and human_selection == r:
  print("You lose")
elif computer_selection == p and human_selection == s:
  print("You lose")
elif computer_selection == r and human_selection == p:
  print("You lose")
