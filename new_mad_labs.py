#Jack tyler
#mad_labs.py
#18/11/24

import random

# Function to get user input with validation
def get_input(prompt, input_type=str):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
        else:
            return user_input

# Function to display a random story
def generate_mad_libs():
    # Define multiple story templates
    story_templates = [
        """Once upon a time, in a {place}, there was a {adjective} {noun1}.
        It loved to {verb1} and always dreamed of {verb2} with a {noun2}.
        One day, it decided to go on an adventure, and its life was never the same again!""",
        
        """The {adjective} {noun1} walked into the {place}, hoping to {verb1} with a {noun2}.
        Suddenly, it found a {adjective} surprise, and it couldn't believe its {noun2} when it {verb2}.""",
        
        """In a {place} far away, a {adjective} {noun1} decided to {verb1}.
        It was a {adjective} day for the {noun2}, who had always dreamed of {verb2} with a famous {noun2}."""
    ]
    
    # Randomly select a story template
    story_template = random.choice(story_templates)

    # Get user inputs
    adjective = get_input("Enter an adjective: ")
    noun1 = get_input("Enter a noun (singular): ")
    noun2 = get_input("Enter a noun (singular): ")
    verb1 = get_input("Enter a verb (past tense): ")
    verb2 = get_input("Enter a verb (present tense): ")
    place = get_input("Enter a place: ")

    # Format the story with user inputs
    story = story_template.format(
        adjective=adjective,
        noun1=noun1,
        noun2=noun2,
        verb1=verb1,
        verb2=verb2,
        place=place
    )
    
    return story

# Main function
def main():
    print("Welcome to the Mad Libs Generator!\n")

    while True:
        # Generate a random story
        story = generate_mad_libs()

        # Display the completed story
        print("\nHere's your Mad Libs story:")
        print("=" * 50)  # Separator for better presentation
        print(story)
        print("=" * 50)

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
