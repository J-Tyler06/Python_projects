# Jack tyler
#19/11/24


import random
import os
import re

# List of valid moves
valid_moves = ['fire', 'water', 'grass']

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice():
    """Get the user's choice with input validation."""
    while True:
        user_input = input("Enter your move (fire, water, or grass): ").lower()
        if re.match(r'^(fire|water|grass)$', user_input):
            return user_input
        else:
            print("Invalid choice. Please choose 'fire', 'water', or 'grass'.")

def get_computer_choice():
    """Get a random choice for the computer."""
    return random.choice(valid_moves)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'fire' and computer_choice == 'grass') or \
       (user_choice == 'grass' and computer_choice == 'water') or \
       (user_choice == 'water' and computer_choice == 'fire'):
        return "You win!"
    
    return "Computer wins!"

def play_game():
    """Main function to play the game."""
    clear_screen()
    
    print("Welcome to Fire, Water, Grass!")
    
    # Get the user's choice
    user_choice = get_user_choice()
    
    # Get the computer's choice
    computer_choice = get_computer_choice()
    
    # Print choices
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()  # Recursively call the function to play again
    else:
        print("Thanks for playing!")

if __name__ == '__main__':
    play_game()
