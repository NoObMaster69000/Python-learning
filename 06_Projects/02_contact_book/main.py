import json
import os

# Define the filename for storing contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """
    Loads contacts from the contacts.json file.
    If the file doesn't exist or is empty, it returns an empty dictionary.
    """
    if not os.path.exists(CONTACTS_FILE):
        return {}
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle cases where the file is empty or corrupted
        return {}

def save_contacts(contacts):
    """
    Saves the current dictionary of contacts to the contacts.json file.
    """
    with open(CONTACTS_FILE, "w") as f:
        # indent=4 makes the JSON file human-readable
        json.dump(contacts, f, indent=4)

def show_contacts(contacts):
    """
    Displays all contacts in a formatted way.
    """
    print("\\n--- Your Contacts ---")
    if not contacts:
        print("Your contact book is empty.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            for key, value in info.items():
                print(f"  {key.capitalize()}: {value}")
            print("-" * 20)
    print("---------------------\\n")

def add_contact(contacts):
    """
    Adds a new contact to the book. The name is the key.
    """
    name = input("Enter contact's name: ")
    if name in contacts:
        print("A contact with this name already exists.")
        return

    phone = input("Enter contact's phone number: ")
    email = input("Enter contact's email: ")

    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    """
    Searches for a contact by name.
    """
    name = input("Enter the name of the contact to search for: ")
    if name in contacts:
        info = contacts[name]
        print("\\n--- Contact Found ---")
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print("---------------------\\n")
    else:
        print(f"No contact found with the name '{name}'.")

def remove_contact(contacts):
    """
    Removes a contact by name.
    """
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' removed successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    """
    The main function that runs the contact book application loop.
    """
    contacts = load_contacts()

    while True:
        print("Contact Book Menu:")
        print("1. Show all contacts")
        print("2. Add a new contact")
        print("3. Search for a contact")
        print("4. Remove a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
