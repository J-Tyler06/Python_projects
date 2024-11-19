#Jack tyler
# word guessing game
#19/11/24
import random

def load_word_list():
    """Load a list of words for the game."""
    words = [
        "python", "coding", "computer", "algorithm", "game", 
        "programming", "developer", "challenge", "learning", "create"
    ]
    return words

def generate_masked_word(word):
    """Create a masked version of the word with underscores."""
    return ['_'] * len(word)

def play_word_guessing_game():
    """Main game logic for the Word Guessing Game."""
    # Game setup
    word_list = load_word_list()
    target_word = random.choice(word_list)
    max_attempts = len(target_word) + 3
    attempts = 0
    score = 100
    
    # Create masked word
    display_word = generate_masked_word(target_word)
    guessed_letters = set()

    print("Welcome to the Word Guessing Game!")
    print(f"I've chosen a word. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        # Display current state of word
        print("\n" + " ".join(display_word))
        print(f"Attempts left: {max_attempts - attempts}")
        
        # Get user's guess
        guess = input("Guess a letter or the whole word: ").lower()
        attempts += 1

        # Check full word guess
        if guess == target_word:
            print(f"Congratulations! You guessed the word '{target_word}'!")
            print(f"Your final score is: {max(0, score - (attempts-1)*10)}")
            return

        # Check letter guess
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter!")
                attempts -= 1
                continue

            guessed_letters.add(guess)

            # Update word display and check for correct guess
            word_updated = False
            for i in range(len(target_word)):
                if target_word[i] == guess:
                    display_word[i] = guess
                    word_updated = True
            
            # Provide feedback and adjust score
            if word_updated:
                print("Correct letter!")
                score += 10
            else:
                print("Incorrect letter!")
                score -= 15

            # Check if word is completely revealed
            if '_' not in display_word:
                print(f"\nCongratulations! You guessed the word '{target_word}'!")
                print(f"Your final score is: {max(0, score)}")
                return

    # Game over if max attempts reached
    print(f"\nGame Over! The word was '{target_word}'.")
    print("Better luck next time!")

def main():
    """Allow multiple game plays."""
    while True:
        play_word_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    main()
