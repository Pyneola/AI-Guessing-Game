import threading
import random
import time

# ANSI Escape Codes for colors
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

# Secret number
SECRET_NUMBER = random.randint(1, 100)
found = False
player_attempts = 0
ai_attempts = 0

# Store guess history for player and AI
player_history = []
ai_history = []


def print_separator(char="-", length=60, color=BLUE):
    """Prints a colored separator line for better output readability."""
    print(f"{color}{char * length}{RESET}")


# AI uses Binary Search to guess the number
def ai_guess():
    global found, ai_attempts
    low, high = 1, 100
    while not found:
        if low > high:
            break
        ai_number = (low + high) // 2
        ai_attempts += 1
        ai_history.append(ai_number)

        print_separator("-", color=BLUE)
        print(f"{YELLOW}AI is guessing... {ai_number}{RESET}")

        if ai_number == SECRET_NUMBER:
            found = True
            print_separator("=", color=GREEN)
            print(
                f"{GREEN}AI WINS! It took {ai_attempts} attempts to find {SECRET_NUMBER}{RESET}"
            )
            print_separator("=", color=GREEN)
        elif ai_number < SECRET_NUMBER:
            low = ai_number + 1
        else:
            high = ai_number - 1

        time.sleep(4.5)  # Delay to simulate AI thinking


# Create a separate Thread for AI
ai_thread = threading.Thread(target=ai_guess)
ai_thread.start()

print_separator("=", color=BLUE)
print(f"{YELLOW}Welcome to the Number Guessing Game!{RESET}")
print("Try to guess the secret number before the AI does.")
print_separator("=", color=BLUE)

while not found:
    try:
        user_input = int(input("\nEnter your guess (1-100): "))

        if user_input in player_history:
            print(f"{RED}You have already guessed this number. Try again!{RESET}")
            continue

        player_attempts += 1
        player_history.append(user_input)

        if user_input == SECRET_NUMBER:
            found = True
            print_separator("=", color=GREEN)
            print(f"{GREEN}YOU WIN! The correct number is {SECRET_NUMBER}{RESET}")
            print(f"{GREEN}You took {player_attempts} attempts.{RESET}")
            print_separator("=", color=GREEN)
        elif user_input < SECRET_NUMBER:
            print_separator("-", color=YELLOW)
            print(f"{YELLOW}HINT: Try a HIGHER number!{RESET}")
            print_separator("-", color=YELLOW)
        else:
            print_separator("-", color=YELLOW)
            print(f"{YELLOW}HINT: Try a LOWER number!{RESET}")
            print_separator("-", color=YELLOW)

        print(f"{BLUE}Your guess history: {player_history}{RESET}")

    except ValueError:
        print(f"{RED}Invalid input! Please enter a number between 1 and 100.{RESET}")

# Wait for AI Thread to finish before exiting
ai_thread.join()

# Score summary
print_separator("=", color=BLUE)
if player_attempts < ai_attempts:
    print(
        f"{GREEN}Congratulations! You outperformed the AI!\n"
        f"Your attempts: {player_attempts} | AI's attempts: {ai_attempts}{RESET}"
    )
elif player_attempts > ai_attempts:
    print(
        f"{RED}The AI was smarter this time!\n"
        f"Your attempts: {player_attempts} | AI's attempts: {ai_attempts}{RESET}"
    )
else:
    print(
        f"{YELLOW}It's a tie! Both you and the AI took {player_attempts} attempts.{RESET}"
    )
print_separator("=", color=BLUE)
