#importando função para aleatoriedade

import random

#definindo as imagens

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

#Criando variáveis
 
img = [rock, paper, scissors] #Lista para selecionar uma das imgs acima
player_choice = int(input("What is your choice? Type 0 for rock, 1 for paper and 2 for scissors: ")) #escolha do jogador, vai de 0 a 2 para estar de acordo com a lista
computer_choice = random.randint(0, 2) #escolha do computador randomizada

#exibição do game

print("\nYour choice is:")
print(img[player_choice])

print("\nThe computer`s choice is")
print(img[computer_choice])

if player_choice == computer_choice:
    print("\ndraw\n")
elif computer_choice == 0 and player_choice == 2 or  computer_choice == 1 and player_choice == 0 or computer_choice == 2 and player_choice == 1:
    print("\nThe computer wins!!\n")
else:
    print("You win!!!")