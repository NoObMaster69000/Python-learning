import os
import datetime

# Define the directory to store blog posts
POSTS_DIR = "posts/"

class Post:
    """
    Represents a single blog post.
    """
    def __init__(self, title, content, author="Admin"):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.datetime.now()

    def get_filename(self):
        """
        Generates a filename from the title and timestamp.
        e.g., '2023-10-27-my-first-post.txt'
        """
        # Create a URL-friendly slug from the title
        slug = self.title.lower().strip().replace(" ", "-")
        date_str = self.timestamp.strftime("%Y-%m-%d")
        return f"{date_str}-{slug}.txt"

    def save(self):
        """
        Saves the blog post to a text file.
        """
        if not os.path.exists(POSTS_DIR):
            os.makedirs(POSTS_DIR)

        filepath = os.path.join(POSTS_DIR, self.get_filename())

        with open(filepath, "w") as f:
            f.write(f"Title: {self.title}\\n")
            f.write(f"Author: {self.author}\\n")
            f.write(f"Published: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\\n")
            f.write("---\\n")
            f.write(self.content)

        print(f"Post '{self.title}' saved to {filepath}")

def create_new_post():
    """
    Gets input from the user to create and save a new post.
    """
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    author = input("Enter author name (or press Enter for 'Admin'): ")

    if not author:
        post = Post(title, content)
    else:
        post = Post(title, content, author)

    post.save()

def list_all_posts():
    """
    Lists all the blog post files in the posts directory.
    """
    if not os.path.exists(POSTS_DIR) or not os.listdir(POSTS_DIR):
        print("No blog posts found.")
        return

    print("\\n--- All Blog Posts ---")
    for filename in sorted(os.listdir(POSTS_DIR)):
        print(f"- {filename}")
    print("----------------------\\n")

def read_post():
    """
    Reads and displays the content of a specific post file.
    """
    list_all_posts()
    filename = input("Enter the full filename of the post to read: ")
    filepath = os.path.join(POSTS_DIR, filename)

    try:
        with open(filepath, "r") as f:
            print("\\n--- Reading Post ---")
            print(f.read())
            print("----------------------\\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def main():
    """
    The main function that runs the blog system application loop.
    """
    while True:
        print("Simple Blog System Menu:")
        print("1. Create a new post")
        print("2. List all posts")
        print("3. Read a post")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_new_post()
        elif choice == '2':
            list_all_posts()
        elif choice == '3':
            read_post()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
