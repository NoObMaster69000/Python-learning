# Project 2: Contact Book

This project is a command-line application for managing a digital contact book. It demonstrates the use of dictionaries to store structured data and the `json` module to save that data to a file.

## Concepts Demonstrated
-   **Dictionaries:** The core data structure used to store contact information (e.g., `{'Alice': {'phone': '123', 'email': 'alice@email.com'}}`).
-   **JSON:** Used to serialize the Python dictionary into a `contacts.json` file for persistence.
-   **File I/O:** Reading from and writing to the JSON file.
-   **Functions:** The application is organized into functions for each main feature (add, show, search, remove).
-   **User Input and Loops:** A `while` loop runs the main menu, and the `input()` function is used to interact with the user.

## How to Run

1.  Navigate to this directory in your terminal:
    ```bash
    cd 06_Projects/02_contact_book
    ```
2.  Run the Python script:
    ```bash
    python main.py
    ```
3.  Follow the on-screen menu to manage your contacts. Your contacts will be saved automatically in a `contacts.json` file in this directory.
