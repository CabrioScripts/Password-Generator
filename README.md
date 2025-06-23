# Password Generator 
A simple command-line password generator written in Python. It generates random passwords containing letters, numbers, and special characters, saves them to a file, and optionally copies them to the clipboard.

Features
Generates multiple passwords of customizable length.

Saves generated passwords to output.txt.

Optionally copies passwords to the system clipboard.

Colorful ASCII banner with red gradient effects for better UX.

Input validation with clear error messages.

Requirements
Python 3.x

Setup
Install the required Python modules using the provided setup.bat script:

bat
Kopieren
Bearbeiten
setup.bat
This will automatically install the necessary packages (colorama and pyperclip).

Usage
Run the script:

bash
Kopieren
Bearbeiten
python password_generator.py
Follow the prompts to enter:

Password length (numbers only)

Number of passwords to generate

Passwords are saved automatically to output.txt. You will be asked if you want to copy them to your clipboard.
