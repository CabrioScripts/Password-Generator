import os
import time
import random
import pyperclip
from colorama import Fore, init

init(autoreset=True)

# Constants
RED_COLORS = [
    "\033[38;5;52m",
    "\033[38;5;88m",
    "\033[38;5;124m",
    "\033[38;5;160m",
    "\033[38;5;196m"
]
RESET = "\033[0m"

BANNER = """
 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░
"""

CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:,.<>?/|\\"

# Functions

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_int_input(prompt: str) -> int:
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        clear_screen()
        print(Fore.RED + "Only numbers allowed!")

def print_banner():
    lines = BANNER.strip().splitlines()
    for i, line in enumerate(lines):
        color = RED_COLORS[i % len(RED_COLORS)]
        print(f"{color}{line}{RESET}")

def generate_passwords(length: int, amount: int) -> list[str]:
    return [''.join(random.choice(CHAR_SET) for _ in range(length)) for _ in range(amount)]

def save_passwords(passwords: list[str], filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(passwords))

def prompt_clipboard_copy(passwords: list[str]):
    choice = input("Copy passwords to clipboard? (y/n): ").strip().lower()
    clear_screen()
    if choice == 'y':
        pyperclip.copy("\n".join(passwords))
        print(Fore.GREEN + "Passwords successfully copied to clipboard.")
    else:
        print(Fore.RED + "No clipboard save. Exiting.")

def password_generator():
    length = get_int_input("┌──(@cabrio11)─[~//Password-GEN-]\n| Password length: ")
    amount = get_int_input("└─$ Number of passwords: ")
    passwords = generate_passwords(length, amount)
    save_passwords(passwords)
    clear_screen()
    print(f"{amount} passwords saved to 'output.txt'.")
    prompt_clipboard_copy(passwords)
    time.sleep(3)
    clear_screen()

def main():
    print_banner()
    password_generator()

if __name__ == "__main__":
    main()
