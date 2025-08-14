# Project 5: Simple Text-Based Blog System

This project is a command-line application that simulates a basic blog. It allows users to create, list, and read blog posts, which are saved as individual text files.

## Concepts Demonstrated
-   **Object-Oriented Programming (OOP):** A `Post` class is used to model the data and behavior of a blog post, encapsulating its title, content, author, and timestamp.
-   **Classes and Methods:** The `Post` class has methods like `.save()` and `.get_filename()` to manage its own data.
-   **File I/O:** Each blog post is saved to its own `.txt` file, demonstrating how to create, write to, and read from files.
-   **Standard Libraries:** The `os` module is used to check for and create directories, and the `datetime` module is used to timestamp posts.
-   **Application Structure:** The code is organized into functions for each feature (creating, listing, reading) and a `main()` function that contains the primary application loop.

## How to Run

1.  Navigate to this directory in your terminal:
    ```bash
    cd 06_Projects/05_blog_system
    ```
2.  Run the Python script:
    ```bash
    python main.py
    ```
3.  Follow the on-screen menu:
    -   **Create a new post:** You will be prompted for a title, content, and author. The application will create a new file in a `posts/` subdirectory.
    -   **List all posts:** This will show you the filenames of all the posts you have created.
    -   **Read a post:** You can enter one of the filenames from the list to view its content.
