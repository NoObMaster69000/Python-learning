# Project 6: Simple Quiz Game

This project is a command-line quiz game that asks the user a series of questions and keeps track of their score. It is designed to be a clear example of Object-Oriented Programming (OOP) in Python.

## Concepts Demonstrated
-   **Object-Oriented Programming (OOP):** The application is structured around classes that model the real-world components of a quiz.
-   **`Question` Class:** A class to represent a single question, encapsulating the question text and the correct answer. It has a method (`check_answer`) to verify the user's input.
-   **`Quiz` Class:** A class to manage the overall game. It holds a list of `Question` objects, tracks the current score and question number, and contains the main game loop (`run` method).
-   **Encapsulation:** Each class manages its own data (e.g., the `Quiz` class manages the score, the `Question` class manages its answer).
-   **Application Logic:** The main part of the script creates instances of these classes and starts the game, showing how objects interact.

## How to Run

1.  Navigate to this directory in your terminal:
    ```bash
    cd 06_Projects/06_quiz_game
    ```
2.  Run the Python script:
    ```bash
    python main.py
    ```
3.  The quiz will start. Answer each question and press Enter. Your final score will be displayed at the end.
