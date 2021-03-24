#following Udemy course: 100 days of code by Angela Yu

import random
print('\n\n----------------Flip a coin------------')
input("If you are ready, type: go\n")
random_int = random.randint(0,1)
if random_int == 0:
    print('Heads')
elif random_int == 1:
    print('Tails')
else:
    print('CHeck your code!')
    
    
#---------------------------------------------------------    
import random

print('\n\n----------------WHO pays the bill?------------')
names_string = input("Give me everybody's names, separated by a comma followed by a space.\n")
names = names_string.split(", ")

persons = len(names)
x = random.randint(0,(persons-1))
print(f'{names[x]} will be paying the bill today')

#OR shorter, using .choice()
#who = random.choice(names)
#print(f'{who} will be paying the bill today')


#--------------------------------------------------------- 

print('\n\n----------------TEASURE MAP------------\n')
print('Look, here is your map, you can hide a treasure somewhere here\n')
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position_row = int(input("Where do you want to put the treasure: enter ROW number \n"))
position_column = int(input("Where do you want to put the treasure: enter COLUMN number \n"))

#map[0][1] = ' X'
map[position_column-1][position_row-1] = ' X'
print('\n\nHere you go:\n')
print(f"{row1}\n{row2}\n{row3}\n")
#--------------------------------------------------------- 


import random
print('\n\n----------------rock paper scissors------------\n')

hands=[
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
]

user=int(input("Ready to play?\n 1 for ROCK\n 2 for PAPER\n 3 for SCISSORS\n When you are ready, enter your choice:\n"))

#prnting your choice
print('*you*:')
if user == 1:
    print (hands[0])
elif user == 2:
    print (hands[1])
elif user == 3:
    print (hands[2])
else:
    print ('incorrect entry. Only 1 to 3 is allowed!\n')

#printing computer choice
random_int = random.randint(0,2)
print('*computer*:')
print(hands[random_int])

#printing result:
print('*result*:')
if user == 1:
    if random_int == 0:
        print('EVEN\nbetter try again')
    if random_int == 1:
        print('You LOST')
    if random_int == 2:
        print('You WON')
elif user == 2:
    if random_int == 0:
        print('You WON')
    if random_int == 1:
        print('EVEN\nbetter try again')
    if random_int == 2:
        print('You LOST')
elif user == 3:
    if random_int == 0:
        print('You LOST')
    if random_int == 1:
        print('You WON')
    if random_int == 2:
        print('EVEN\nbetter try again')
        
'''        
-----------------------------------------        
another way to work with a list of images:
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

game_images = [rock,paper,scissors]
print(game_images[0])
'''
