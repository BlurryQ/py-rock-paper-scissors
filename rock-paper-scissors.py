import random
import inquirer

def declare_round_start(round, rounds):
    print("                          ")
    print(f"--- ROUND {round + 1} ---")
    if round == rounds - 1: print("FINAL ROUND!!")

def declare_winner(user_score, computer_score, rounds):
    print("--- GAME OVER ---")
    print("                          ")
    if user_score > computer_score:
        print(f"You are the overall victor, you won the first to {rounds}!! :D")
    elif user_score < computer_score:
        print("You suck!! You couldn't beat a computer!! :P")
    else: 
        print("Inconclusive results. Try again or else!! -.-")


def get_player_choice():
    get_choice = [inquirer.List("weapon",
                message="Pick your weapon wisely...",
                choices=["Rock", "Paper", "Scissors"]
                )]

    user_choice = inquirer.prompt(get_choice)
    user_choice = user_choice ["weapon"].lower()
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
            print("                          ")
            return "draw"
        elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper")):
            print("Well done, you have won!! :D")
            print("                          ")
            return "user"
        else: 
            print("You have lost :(")
            print("                          ")
            return "computer"

def rock_paper_scissors(rounds):
    user_score = 0
    computer_score = 0
    round = 0
    # test the below line out, think it works as a single
    while user_score < rounds | computer_score < rounds:
        declare_round_start(round, rounds)
        user_choice = get_player_choice()
        computer_choice = get_computer_choice()
        results = get_results(user_choice, computer_choice)
        if results == "user":  user_score += 1
        if results == "computer": computer_score += 1
        print("_______________________________________")
        print(f"|| Your score:{user_score} || Opponent Score: {computer_score} ||")
        print("                          ")
        round += 1
    else: 
        declare_winner(user_score, computer_score, rounds)

valid_rounds_value = False
while not valid_rounds_value:
    try:
        total_rounds = int(input("How many rounds would you like to play? "))
        rock_paper_scissors(total_rounds)
        valid_rounds_value = True
    except:
        print("You have entered an invalid number, please try again")