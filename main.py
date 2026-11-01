def add_note():
    filename = "notes.txt"

    file = open(filename, "a")
    file.close()

    file = open(filename, "r")
    saved_notes = file.read()
    file.close()

    next_number = 1
    for line in saved_notes.splitlines():
        parts = line.split("|", 1)
        if len(parts) == 2 and parts[0].startswith("N") and parts[0][1:].isdigit():
            saved_number = int(parts[0][1:])
            if saved_number >= next_number:
                next_number = saved_number + 1

    title = input("Enter note title: ").strip()
    if title == "":
        print("Title cannot be empty. Note not saved.")
        return

    content = input("Enter note content: ")
    note_id = f"N{next_number}"

    file = open(filename, "a")
    file.write(note_id + "|" + title + "|" + content + "\n")
    file.close()

    print(f"Note saved. ID: {note_id} | {title}")
    return note_id


def view_notes():
    filename = "notes.txt"

    file = open(filename, "a")
    file.close()

    file = open(filename, "r")
    saved_notes = file.read()
    file.close()

    if saved_notes.strip() == "":
        print("No notes found")
        return

    print("\nAll notes:")
    for line in saved_notes.strip().splitlines():
        parts = line.strip().split("|", 2)
        if len(parts) == 3:
            note_id = parts[0].strip()
            title = parts[1].strip()
            content = parts[2].strip()
            print(f"ID: {note_id} | Title: {title} | Content: {content}")


def search_notes():
    filename = "notes.txt"
    keyword = input("Enter a keyword to search: ").strip().lower()

    if keyword == "":
        print("Please enter a keyword.")
        return

    file = open(filename, "a")
    file.close()

    file = open(filename, "r")
    saved_notes = file.read()
    file.close()

    found_note = False
    for line in saved_notes.strip().splitlines():
        if line == "":
            continue

        parts = line.strip().split("|", 2)
        if len(parts) == 3:
            note_id = parts[0].strip()
            title = parts[1].strip()
            content = parts[2].strip()

            if keyword in title.lower() or keyword in content.lower():
                print(f"ID: {note_id} | Title: {title} | Content: {content}")
                found_note = True

    if not found_note:
        print("No matching notes found")


def edit_note():
    filename = "notes.txt"
    note_id = input("Enter the ID of the note to edit: ").strip()
    if note_id == "":
        print("Note ID cannot be empty.")
        return

    try:
        with open(filename, "a"):
            pass
        with open(filename, "r") as file:
            notes = file.readlines()
    except OSError as error:
        print(f"Could not read notes: {error}")
        return

    for index, line in enumerate(notes):
        parts = line.rstrip("\n").split("|", 2)
        if len(parts) == 3 and parts[0].strip() == note_id:
            new_content = input("Enter the new content: ")
            notes[index] = parts[0] + "|" + parts[1] + "|" + new_content + "\n"

            try:
                with open(filename, "w") as file:
                    file.writelines(notes)
            except OSError as error:
                print(f"Could not update note: {error}")
                return

            print(f"Note updated. ID: {note_id}")
            return

    print(f"No note found with ID: {note_id}")


def delete_note():
    filename = "notes.txt"
    note_id = input("Enter the ID of the note to delete: ").strip()
    if note_id == "":
        print("Note ID cannot be empty.")
        return

    try:
        with open(filename, "a"):
            pass
        with open(filename, "r") as file:
            notes = file.readlines()
    except OSError as error:
        print(f"Could not read notes: {error}")
        return

    remaining_notes = []
    note_found = False
    for line in notes:
        parts = line.rstrip("\n").split("|", 2)
        if len(parts) == 3 and parts[0].strip() == note_id:
            note_found = True
        else:
            remaining_notes.append(line)

    if not note_found:
        print(f"No note found with ID: {note_id}")
        return

    try:
        with open(filename, "w") as file:
            file.writelines(remaining_notes)
    except OSError as error:
        print(f"Could not delete note: {error}")
        return

    print(f"Note deleted. ID: {note_id}")


def main():
    while True:
        print("\nDigital Notes Management System")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")


main()
