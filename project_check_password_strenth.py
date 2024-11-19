#jack tyler
#19/11/24
import random
import string
import re

class SecurityCodeManager:
    def __init__(self):
        """Initialize security parameters."""
        self.min_length = 6
        self.max_length = 12
        self.complexity_levels = {
            'low': 3,
            'medium': 5,
            'high': 8
        }

    def generate_security_code(self, complexity='medium'):
        """Generate a secure code based on complexity level."""
        length = random.randint(
            self.complexity_levels[complexity], 
            self.max_length
        )
        
        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine character sets based on complexity
        if complexity == 'low':
            char_set = lowercase + digits
        elif complexity == 'medium':
            char_set = lowercase + uppercase + digits
        else:
            char_set = lowercase + uppercase + digits + symbols

        # Generate code
        security_code = ''.join(random.choice(char_set) for _ in range(length))
        return security_code

    def validate_security_code(self, code):
        """
        Validate security code with comprehensive checks.
        Returns tuple of (is_valid, feedback)
        """
        # Length check
        if len(code) < self.min_length:
            return False, "Code is too short"
        
        # Complexity checks
        checks = {
            'lowercase': r'[a-z]',
            'uppercase': r'[A-Z]',
            'digits': r'\d',
            'symbols': r'[!@#$%^&*(),.?":{}|<>]'
        }
        
        failed_checks = [
            check for check, pattern in checks.items() 
            if not re.search(pattern, code)
        ]
        
        # Generate feedback
        if failed_checks:
            feedback = f"Missing: {', '.join(failed_checks)}"
            return False, feedback
        
        return True, "Valid security code"

def main():
    """Interactive security code management."""
    manager = SecurityCodeManager()

    while True:
        print("\n1. Generate Security Code")
        print("2. Validate Security Code")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            complexity = input("Select complexity (low/medium/high): ").lower()
            if complexity not in ['low', 'medium', 'high']:
                complexity = 'medium'
            
            code = manager.generate_security_code(complexity)
            print(f"\nGenerated Code: {code}")
        
        elif choice == '2':
            code = input("Enter security code to validate: ")
            is_valid, feedback = manager.validate_security_code(code)
            
            print(f"Validation Result: {'✅ Valid' if is_valid else '❌ Invalid'}")
            print(f"Feedback: {feedback}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
