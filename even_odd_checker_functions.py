def get_integer_input():
    """Handles user input to obtain an integer."""

        try:
    while True:
            user_input = input("Please enter an integer: ")
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    """Determines if a given number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """Main program flow."""
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()