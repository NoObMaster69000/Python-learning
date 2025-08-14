def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """
    Divides two numbers.
    Handles division by zero by returning an error message string.
    """
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def get_numbers():
    """
    Gets two numbers from the user, with robust error handling.
    Returns a tuple (num1, num2) or (None, None) if input is invalid.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None

def main():
    """
    The main function that runs the calculator application loop.
    """
    while True:
        print("\\n--- Simple Calculator ---")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()

            # If get_numbers returned valid numbers
            if num1 is not None:
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
