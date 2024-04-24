import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    return random.choice(cards)

def calculate_score(cards_given):
    # Blackjack (21) com 2 cartas
    if sum(cards_given) == 21 and len(cards_given) == 2:
        return 0
    # Ajustar Ás (11) para 1 se o total for maior que 21
    if 11 in cards_given and sum(cards_given) > 21:
        cards_given.remove(11)
        cards_given.append(1)
    return sum(cards_given)

def compare_scores(player_score, computer_score):
    if player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    players_cards = []
    computers_cards = []

    # Distribuir cartas iniciais
    for _ in range(2):
        players_cards.append(deal_card())
        computers_cards.append(deal_card())

    while True:
        print(f"\nThese are your cards {players_cards}, score = {calculate_score(players_cards)}. \nThis is the first computer card [{computers_cards[0]}].")
        
        # Perguntar se o jogador deseja outra carta
        draw = input("Do you want to draw another card? [Y] [N]: ").lower()
        if draw == "y":
            players_cards.append(deal_card())
            if calculate_score(players_cards) > 21:
                break
        else:
            break

    # Computador compra cartas até atingir pelo menos 17
    while calculate_score(computers_cards) < 17:
        computers_cards.append(deal_card())

    player_score = calculate_score(players_cards)
    computer_score = calculate_score(computers_cards)

    # Mostrar os resultados finais
    print(f"\nYour final score is {player_score} with cards {players_cards}")
    print(f"Computer's final score is {computer_score} with cards {computers_cards}\n")

    # Comparar pontuações e mostrar resultado final
    print(compare_scores(player_score, computer_score))

    # Perguntar se deseja jogar novamente
    if input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
        clear()
        game()
    else:
        print("Thank you for playing!")

game()
