import requests
from bs4 import BeautifulSoup

def scrape_hacker_news_titles():
    """
    Scrapes the titles of the top stories from the Hacker News homepage.
    """
    # The URL of the site we want to scrape
    url = "https://news.ycombinator.com/"

    print(f"Fetching data from {url}...")

    try:
        # Make an HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch the website. {e}")
        return

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the story titles. On Hacker News, these are in `<span>` tags
    # with the class 'titleline'. We specifically look for the `<a>` tag inside.
    story_links = soup.select('.titleline > a')

    print("\\n--- Top Hacker News Titles ---")
    if not story_links:
        print("Could not find any story titles. The website structure may have changed.")
    else:
        for i, link in enumerate(story_links, 1):
            # The title is the text of the <a> tag
            title = link.get_text()
            print(f"{i}. {title}")
    print("----------------------------\\n")

def main():
    scrape_hacker_news_titles()

if __name__ == "__main__":
    main()
