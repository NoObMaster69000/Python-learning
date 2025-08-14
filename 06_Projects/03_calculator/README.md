# Project 3: Simple Command-Line Calculator

This project is a command-line calculator that performs basic arithmetic operations. It is designed to demonstrate the use of functions for organization and `try-except` blocks for robust error handling.

## Concepts Demonstrated
-   **Functions:** Each mathematical operation (`add`, `subtract`, etc.) is encapsulated in its own function, promoting code reuse and readability. A dedicated function also handles user input.
-   **Error Handling:** The application uses `try-except` blocks to gracefully handle common errors, such as a `ValueError` if the user enters non-numeric text, and a logical check to prevent `ZeroDivisionError`.
-   **Conditional Logic:** `if/elif/else` statements are used to route user input to the correct function.
-   **Loops:** A `while` loop keeps the application running until the user chooses to exit.

## How to Run

1.  Navigate to this directory in your terminal:
    ```bash
    cd 06_Projects/03_calculator
    ```
2.  Run the Python script:
    ```bash
    python main.py
    ```
3.  Follow the on-screen menu to perform calculations.
