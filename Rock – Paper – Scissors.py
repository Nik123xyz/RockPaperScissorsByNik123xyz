import random

choices = {
    'r': "Rock",
    'p': "Paper",
    's': "Scissors",
}

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

user_score = 0
computer_score = 0
rounds_played = 0

def determine_winner(player_choice, computer_choice):
    global user_score, computer_score, rounds_played
    if player_choice == computer_choice:
        return "Draw"
    elif (
        (player_choice == 'r' and computer_choice == 's') or
        (player_choice == 'p' and computer_choice == 'r') or
        (player_choice == 's' and computer_choice == 'p')
    ):
        user_score += 1
        return "User"
    else:
        computer_score += 1
        return "Computer"

while True:
    print(f"Round {rounds_played + 1}")
    print(f"User Score: {user_score}  Computer Score: {computer_score}")

    # User input
    while True:
        user_move = input("Choose [r]ock, [p]aper, or [s]cissors (or 'q' to quit): ").lower()
        if user_move == 'q':
            print("Thanks for playing!")
            exit()
        if user_move in choices:
            break
        else:
            print("Invalid input. Try again.")

    player_move = choices[user_move]
    
    computer_move = choices[random.choice(list(choices.keys()))]
    print(f"The computer chose {computer_move}.")

    result = determine_winner(user_move, random.choice(list(choices.keys())))

    if result == "Draw":
        print(YELLOW + "It's a draw!" + RESET)
    elif result == "User":
        print(GREEN + f"You win! {player_move} beats {computer_move}" + RESET)
    else:
        print(RED + f"You lose! {computer_move} beats {player_move}" + RESET)

    rounds_played += 1