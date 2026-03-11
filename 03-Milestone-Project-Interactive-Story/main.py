```python
"""
Project: Cyber-Rescue: A Terminal Adventure
Author: Microsoft SDE-2 Mentor
Description: A modular interactive story demonstrating control flow, 
             input validation, and state management.
"""

import sys

def clear_terminal():
    # Simple trick to keep the UI clean
    print("\n" * 50)

def get_choice(options):
    """
    SDE Tip: Robust input validation function to reuse across the project.
    """
    while True:
        user_input = input(f"\nWhat do you do? ({'/'.join(options)}): ").upper().strip()
        if user_input in options:
            return user_input
        print("System Error: Command not recognized. Please try again.")

def game_over(message):
    print(f"\n--- GAME OVER ---")
    print(message)
    sys.exit()

def server_room(state):
    print("\n[SERVER ROOM]")
    print("The servers are humming. A red light flashes on the console.")
    
    choice = get_choice(["HACK", "LEAVE"])
    
    if choice == "HACK":
        if state["has_virus"]:
            print("You upload the virus! The system crashes. You won!")
        else:
            game_over("You tried to hack without the virus. The security AI caught you.")
    else:
        main_lobby(state)

def main_lobby(state):
    print("\n[MAIN LOBBY]")
    print("You see a 'VAULT' door and a 'SERVER' room.")
    
    choice = get_choice(["VAULT", "SERVER"])
    
    if choice == "VAULT":
        print("\nYou find a USB drive containing a 'De-compiler Virus'!")
        state["has_virus"] = True
        main_lobby(state) # Loop back with new state
    elif choice == "SERVER":
        server_room(state)

def main():
    """
    The entry point of our application.
    """
    # Initializing Game State
    player_state = {
        "name": "",
        "has_virus": False
    }

    clear_terminal()
    print("=== CYBER-RESCUE v1.0 ===")
    player_state["name"] = input("Identity required. Enter Name: ")
    
    print(f"\nAgent {player_state['name']}, your mission is to disable the AI.")
    print("You have successfully breached the outer perimeter.")
    
    # Start the story
    main_lobby(player_state)

if __name__ == "__main__":
    # SDE Best Practice: Only run the code if the script is executed directly
    main()
```