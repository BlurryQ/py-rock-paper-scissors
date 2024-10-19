import random

def declare_round_start(user_score, computer_score, round, rounds):
    print(f"|| Your score:{user_score} || Opponent Score: {computer_score} ||")
    if round == rounds - 1: print("FINAL ROUND!! FIGHT FOR YOUR LIIIIIIIIIFFFEEEEEE")
    print(f"--- ROUND {round + 1} ---")

def declare_winner(user_score, computer_score, rounds):
    print("--- GAME OVER ---")
    if user_score > computer_score:
        print(f"You are the overall victor, you won the best of {rounds}!! :D")
    elif user_score < computer_score:
        print("You suck!! You couldn't beat a computer!! :P")
    else: 
        print("Inconclusive results. Try again or else!! -.-")

def get_player_choice():
    user_choice = input("rock, paper or scissors? ")
    user_choice = user_choice.lower()
    print(f"You have selected {user_choice}")
    return user_choice

def get_computer_choice():
    random_number = random.randrange(1,4)
    computer_choice = ""
    if random_number == 1:
        computer_choice = "scissors"
    elif random_number == 2:
        computer_choice = "rock"
    else:
        computer_choice = "paper"
    print(f"Your opponent has chosen {computer_choice}")
    return computer_choice

def get_results(user_choice, computer_choice):
        if user_choice == computer_choice: 
            print("This is a draw :/")
            return "draw"
        elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper")):
            print("Well done, you have won!! :D")
            return "user"
        else: 
            print("You have lost :(")
            return "computer"

def rock_paper_scissors(rounds):
    user_score = 0
    computer_score = 0
    for round in range(int(rounds)):
        declare_round_start(user_score, computer_score, round, int(rounds))
        user_choice = get_player_choice()
        computer_choice = get_computer_choice()
        results = get_results(user_choice, computer_choice)
        if results == "user":  user_score += 1
        if results == "computer": computer_score += 1
    else: 
        declare_winner(user_score, computer_score, rounds)

total_rounds = input("How many rounds would you like to play? ")
rock_paper_scissors(int(total_rounds))