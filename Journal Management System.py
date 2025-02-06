# ---------------------------------------------
# Journal Management System
# ---------------------------------------------
# This program allows users to:
# 1. Add journal entries with automatic timestamps.
# 2. View all saved entries.
# 3. Search entries by date.
# 4. Delete specific entries by date.
# 5. Quit the program.
# ---------------------------------------------

import os
import datetime

# File to store journal entries
JOURNAL_FILE = "journal_entries.txt"

# Ensure the journal file exists
if not os.path.exists(JOURNAL_FILE):
    with open(JOURNAL_FILE, "w") as file:
        print("New journal file created!")

# ---------------------------------------------
# Function to Add a Journal Entry
# ---------------------------------------------

def add_entry():
    """
    Adds a new journal entry with an automatic timestamp.
    """
    try:
        with open(JOURNAL_FILE, 'a') as file:
            entry_content = input("Write your journal entry: ").strip()
            if not entry_content:
                raise ValueError("Entry cannot be empty!")

            timestamp = datetime.datetime.now().strftime("%m-%d-%y %H:%M")
            file.write(f"{timestamp} | {entry_content}\n")

        print("Journal entry added successfully!")

    except ValueError as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to View All Journal Entries
# ---------------------------------------------

def view_entries():
    """
    Displays all journal entries in chronological order.
    """
    try:
        with open(JOURNAL_FILE, 'r') as file:
            entries = file.readlines()

        if not entries:
            print("\nNo journal entries found! Start by adding one.")
            return

        print("\n--- Journal Entries ---")
        for i, entry in enumerate(entries, start=1):
            print(f"\nEntry {i}: {entry.strip()}\n")

    except FileNotFoundError:
        print("Journal file not found. Please add an entry first.")

# ---------------------------------------------
# Function to Search for a Journal Entry
# ---------------------------------------------

def search_entry():
    """
    Searches for journal entries by date (MM-DD-YY format).
    """
    try:
        search_date = input("Enter the date to search (MM-DD-YY): ").strip()

        with open(JOURNAL_FILE, 'r') as file:
            entries = file.readlines()

        found = False
        for entry in entries:
            entry_date = entry[:8]  # Extract first 8 characters (MM-DD-YY)
            if entry_date == search_date:
                print("\nEntry Found:")
                print("-" * 40)
                print(entry.strip())
                print("-" * 40)
                found = True

        if not found:
            print(f"No journal entries found for {search_date}.")

    except FileNotFoundError:
        print("No journal entries found! Start by adding one.")

# ---------------------------------------------
# Function to Delete a Journal Entry
# ---------------------------------------------

def delete_entry():
    """
    Deletes a journal entry by date (MM-DD-YY format).
    """
    try:
        delete_date = input("Enter the date of the entry to delete (MM-DD-YY): ").strip()

        with open(JOURNAL_FILE, 'r') as file:
            entries = file.readlines()

        found = False
        remaining_entries = []

        for entry in entries:
            entry_date = entry[:8]  # Extract first 8 characters (MM-DD-YY)
            if entry_date == delete_date:
                print(f"\nDeleted Entry:\n{entry.strip()}")
                found = True
                continue  # Skip this entry to delete

            remaining_entries.append(entry)  # Keep all other entries

        if not found:
            print(f"No journal entries found for {delete_date}.")

        with open(JOURNAL_FILE, 'w') as file:
            file.writelines(remaining_entries)

    except FileNotFoundError:
        print("No journal entries found! Start by adding one.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ---------------------------------------------
# Function to Display Menu
# ---------------------------------------------

def menu():
    """
    Provides an interactive menu for managing journal entries.
    """
    while True:
        print("\n--- Journal Manager Menu ---")
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete an Entry")
        print("5. Quit")

        try:
            choice = int(input("Enter your choice (1-5): ").strip())

            if choice == 1:
                add_entry()
            elif choice == 2:
                view_entries()
            elif choice == 3:
                search_entry()
            elif choice == 4:
                delete_entry()
            elif choice == 5:
                confirm = input("Are you sure you want to quit? (Y/N): ").strip().lower()
                if confirm == "y":
                    print("Thank you for using the Journal Manager! Goodbye! 👋")
                    break
                else:
                    print("Returning to the menu...")
            else:
                print("Invalid option! Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Journal Manager App!")
    menu()
