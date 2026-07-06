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

rps= [rock,paper,scissors]
choice= int(input("what do you choose? choose 0 for rock, 1 for paper, 2 for scissors\n"))
print("you chose- ",choice)

computer= random.randint(0,2)
print("computer chose- ",computer)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print('invalid choice')

if choice == computer:
    print("its a tie lol")
elif choice == 0 & computer == 2:
    print("you win")
elif choice > computer:
    print("you lose")
else:
    print("invalid choice. you lose")
