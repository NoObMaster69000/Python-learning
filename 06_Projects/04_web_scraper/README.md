# Project 4: Simple Web Scraper

This project is a command-line web scraper that fetches and displays the titles of the top stories from the [Hacker News](https://news.ycombinator.com/) homepage.

## Concepts Demonstrated
-   **Third-Party Libraries:** This project relies on external libraries, which must be installed via `pip`.
-   **`requests` library:** Used to make an HTTP GET request to a URL and retrieve the raw HTML content of the webpage.
-   **`BeautifulSoup` library:** Used to parse the HTML content, making it easy to navigate the document tree and find specific elements.
-   **HTML Selectors:** Uses CSS selectors (`.titleline > a`) to precisely target and extract the desired data from the HTML structure.
-   **Error Handling:** Includes a `try-except` block to handle potential network errors when fetching the website.

## How to Run

1.  **Install Dependencies:** Before running the script, you need to install the required libraries. Make sure you have activated your virtual environment, then run:
    ```bash
    pip install requests beautifulsoup4
    ```
    (These are already included in the main `requirements.txt` of the parent project).

2.  **Navigate to the Directory:** Open your terminal and navigate to this project's directory:
    ```bash
    cd 06_Projects/04_web_scraper
    ```
3.  **Run the Script:**
    ```bash
    python main.py
    ```
    The script will then print a numbered list of the current top story titles from Hacker News.
