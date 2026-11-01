# Digital Notes Management System

A beginner-friendly Python 3 command-line application for adding, viewing, searching, editing, and deleting text notes. Notes are stored locally in `notes.txt`, so they remain available after the program exits.

## Features

- **Add notes:** Save a note with a title and content.
- **Automatic IDs:** Assigns IDs such as `N1`, `N2`, and `N3`. The next ID is generated from the highest existing note ID.
- **Title validation:** Empty titles and titles containing only spaces are rejected.
- **View all notes:** Displays every saved note. Shows `No notes found` when there are no notes.
- **Search notes:** Searches both titles and content. Search is case-insensitive.
- **Edit notes:** Finds a note by ID and updates its content while preserving its title and other notes.
- **Delete notes:** Deletes a note by ID while preserving all other notes.
- **Interactive menu:** Returns to the menu after each action and exits when you select option 6.

## Project structure

```text
Digital Notes Management System/
├── main.py     # Application functions and menu
├── notes.txt   # Local plain-text note storage
└── README.md   # Project documentation
```

The program creates `notes.txt` automatically when you first add or view notes. You do not need to create it manually.

## Requirements

- Python 3
- No third-party Python packages

Check whether Python is installed by running either command in a terminal:

```powershell
python --version
```

```powershell
py --version
```

## How to run

1. Open the project folder in VS Code.
2. Select **Terminal → New Terminal**.
3. Make sure the terminal is in the project folder.
4. Start the program:

   ```powershell
   python main.py
   ```

   If the `python` command is unavailable, try:

   ```powershell
   py main.py
   ```

## Menu guide

When the program starts, it displays this menu:

```text
Digital Notes Management System
1. Add Note
2. View All Notes
3. Search Note
4. Edit Note
5. Delete Note
6. Exit
```

Enter an option number at the prompt and press Enter.

### 1. Add Note

Enter a title and content. The program generates an ID and displays a confirmation:

```text
Enter note title: Python
Enter note content: Learn loops
Note saved. ID: N1 | Python
```

An empty title is rejected, and the note is not saved. The program displays `Title cannot be empty. Note not saved.` and returns to the menu.

### 2. View All Notes

Displays each note with its ID, title, and content. If there are no notes, it displays `No notes found`.

### 3. Search Note

Enter a keyword to search for. The program checks both titles and content without regard to letter case. For example, `python`, `Python`, and `PYTHON` match the same text.

An empty keyword displays a prompt message. If there are no matches, the program displays `No matching notes found`.

### 4. Edit Note

Enter a note ID, then enter the new content. This option updates only the content; it does not change the title.

```text
Enter the ID of the note to edit: N1
Enter the new content: Practice functions
Note updated. ID: N1
```

### 5. Delete Note

Enter the ID of the note to delete. If the ID does not exist, the program displays `No note found with ID: ...`.

### 6. Exit

Exits the program. If you enter an option other than 1 through 6, the program displays an invalid-option message and shows the menu again.

## Note storage format

Each note is stored on one line in `notes.txt`:

```text
ID|Title|Content
```

For example:

```text
N1|Python|Learn loops
N2|Shopping|Buy notebook
```

Each record has three fields: ID, title, and content. The program splits a record at most twice on `|`, so the content can contain `|`. **Do not use `|` in a title**, because it is the field separator.

You can edit `notes.txt` with a text editor, but keep each line in this format. Lines with an invalid format may not be processed correctly by the note operations.

## Data and backups

- Notes are stored in a local plain-text file. The program does not use an online service or database.
- You can back up your notes by copying `notes.txt`.
- Deleting `notes.txt` also deletes the saved notes.
- The program looks for `notes.txt` in the current working directory from which `python main.py` is run. For best results, run the command from a terminal opened in the project folder.

## Python concepts used

- **Functions:** `add_note()`, `view_notes()`, `search_notes()`, `edit_note()`, and `delete_note()` each perform a separate task.
- **Loops:** The `while` loop keeps the menu running; `for` loops process notes one at a time.
- **Conditions:** `if`, `elif`, and `else` choose an action based on the menu selection, title, or search results.
- **File handling:** `open()` opens a file. `read()`, `write()`, `readlines()`, and `writelines()` read or write data.
- **File modes:** `"r"` reads a file, `"a"` appends to the end of existing content, and `"w"` rewrites the file.
- **Lists:** Edit and delete operations read notes into a list, update or remove the selected note, and then rewrite the file.
- **String methods:** `.strip()` removes surrounding whitespace, `.split()` separates fields, and `.lower()` supports case-insensitive searching.
- **Exception handling:** Edit and delete operations display an error message if a file operation raises `OSError`.

## Known limitations

- Notes are stored as plain text; they are not encrypted or password-protected.
- Search uses substring matching rather than exact-word matching. For example, the keyword `loop` also matches `loops`.
- The edit option changes only the content; there is no menu option to edit a title.
- The file format uses `|` as a delimiter. Do not use this character in a title.

## Troubleshooting

### `python` command not found

On Windows, try `py main.py`. If that command is also unavailable, install Python 3 and reopen the terminal.

### `No notes found`

This message appears when `notes.txt` in the current working directory is empty. Make sure you are running the program from a terminal opened in the project folder.

### Note ID not found

Use **View All Notes** to check the saved IDs. IDs use a format such as `N1` or `N2`.

## Practice ideas

1. Add two notes and verify them with **View All Notes**.
2. Search for a word in a title or note using uppercase letters.
3. Edit one note's content, then view another note to confirm it remains unchanged.
4. Delete one note and verify that the other notes remain.
