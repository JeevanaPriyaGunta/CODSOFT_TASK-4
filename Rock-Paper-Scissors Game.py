import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # User input
    
    user_input = input("Choose rock, paper, or scissors: ").lower()
    
    # Computer selection
    choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(choices)
    
    # Determine the winner
    if user_input == computer_input:
        result = "It's a tie!"
    elif (
        (user_input == "rock" and computer_input == "scissors") or
        (user_input == "scissors" and computer_input == "paper") or
        (user_input == "paper" and computer_input == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    # Display choices and result
    print(f"You chose {user_input}, computer chose {computer_input}. {result}")
    
    # Display scores
    print(f"User: {user_score}, Computer: {computer_score}")
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break