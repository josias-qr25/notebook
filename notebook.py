import json
import os
from time import sleep
from datetime import datetime

# Log File
LOG_FILE = "logs.json"

def load_notes():
    """Load notes from logs.json."""
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r') as file:
                return json.load(file)
    except json.JSONDecodeError:
        return []

def save_notes(notes):
    """Save notes to logs.json."""
    with open(LOG_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note(title, note):
    """Add a new note with title, note, and timestamp."""
    notes = load_notes()
    notes_id = max([a['id'] for a in notes], default=0) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:$S")
    new_note = {
            "id": notes_id,
            "title": title,
            "note": note,
            "timestamp": timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print(f"Note '{title} added successfully!")

def show_notes():
    """Show all notes."""
    notes = load_notes()
    if not notes:
        sleep(.4)
        print("\nNo notes found.\n")
        return
    for a in notes:
        print(f"ID: {a['id']}, Title: {a['title']}, Timestamp: {a['timestamp']}")
        print(f"Note: {a['note']}\n")

def main():
    """Main Program Loop"""
    while True:
        sleep(.3)
        print("\n- Notebook -\n")
        print("(A)dd Note")
        sleep(.3)
        print("(S)how Notes")
        sleep(.3)
        print("(E)xit")
        sleep(.3)
        choice = input("\nEnter your choice: ")

        if choice == 'A' or choice == 'a':
            title = input("Title: ")
            note = input("Note: ")
            add_note(title, note)
        elif choice == 'S' or choice == 's':
            show_notes()
        elif choice == 'E' or choice =='e':
            print("\nHave a nice day!")
            sleep(.5)
            print("\nRemember, you can accomplish anything!\n")
            break
        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()
