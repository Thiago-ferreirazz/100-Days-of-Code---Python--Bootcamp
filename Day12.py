import os
import random

# Número de tentativas para cada modo de dificuldade
hard_mode = 5
easy_mode = 10

# Função para limpar a tela de forma cross-platform
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para receber um número entre 1 e 100
def number():
    while True:
        num = input("Guess a number: ")
        if num.isnumeric():  # Verifica se é um número
            num = int(num)
            if 1 <= num <= 100:  # Verifica se está entre 1 e 100
                return num
            else:
                print("Type a valid number between 1 and 100.")
        else:
            print("This is not a number.")

# Função para selecionar a dificuldade do jogo
def select_difficulty():
    while True:
        diff = input("Do you prefer playing in hard [H] or easy [E] mode? ")
        if diff.lower() == 'e':  # Modo fácil
            return easy_mode
        elif diff.lower() == 'h':  # Modo difícil
            return hard_mode
        else:
            print("Type a valid difficulty. Choose 'H' for hard or 'E' for easy.")

# Função para verificar se o jogador quer continuar jogando
def keep_playing():
    if input("If you want to keep playing, type [Y]. Otherwise, type anything else to exit: ").lower() == 'y':
        clear()
        game()  # Reinicia o jogo
    else:
        print("Goodbye!")

# Função principal do jogo
def game():
    answer = random.randint(1, 100)  # Número aleatório entre 1 e 100
    print(f"For testing: {answer}")  # Para depuração, remove para a versão final
    print("\nWelcome to the guessing game. I'm thinking of a number between 1 and 100...")
    print("Can you guess it?")

    tries = select_difficulty()  # Seleciona o número de tentativas com base na dificuldade
    print(f"You have {tries} tries left.\n")

    # Loop para permitir o jogador tentar adivinhar
    while True:
        player_answer = number()  # Obter a resposta do jogador
        tries -= 1

        if player_answer == answer:  # Se o jogador acertar
            print("Congratulations! You guessed it.")
            break
        elif tries == 0:  # Se acabar o número de tentativas
            print(f"You have no more tries left. The answer was {answer}.")
            break
        elif player_answer > answer:  # Se a resposta do jogador for maior que a resposta correta
            print(f"Too high. You have {tries} tries left.")
        else:  # Se a resposta do jogador for menor que a resposta correta
            print(f"Too low. You have {tries} tries left.")

    # Pergunta se o jogador quer continuar jogando
    keep_playing()

# Inicia o jogo
game()
