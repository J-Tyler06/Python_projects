#jack tyler
#19/11/24

import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def toss_coin():
    """Simulate tossing a coin."""
    return random.choice(['Heads', 'Tails'])

def play_game():
    """Main function to play the Coin Tossing Simulator."""
    clear_screen()
    
    print("Welcome to the Coin Tossing Simulator!")
    
    while True:
        # Ask the user if they want to toss the coin
        input("Press Enter to toss the coin (or type 'exit' to quit): ").lower()
        
        # Simulate the coin toss
        result = toss_coin()
        
        # Show the result of the toss
        print(f"\nThe result of the coin toss is: {result}!")
        
        # Ask if the user wants to toss again
        play_again = input("\nDo you want to toss again? (yes/no): ").lower()
        
        if play_again == 'no':
            print("Thanks for playing!")
            break
        elif play_again != 'yes':
            print("Invalid input. Exiting the game.")
            break
        else:
            clear_screen()  # Clear the screen for the next toss

if __name__ == '__main__':
    play_game()
