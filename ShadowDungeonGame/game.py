import time
import os
import sys
import random
import number_guessing_game


def narrate(text):
    print(text)
    time.sleep(1.5)

def encrypt(text, shift):
    result = ""
    for letter in text:
        if not letter.isalpha():
            result += letter
        elif letter.isupper():
            new_num = (ord(letter) - ord('A') + shift) % 26 + ord('A')
            result += chr(new_num)
        elif letter.islower():
            new_num = (ord(letter) - ord('a') + shift) % 26 + ord('a')
            result += chr(new_num)
    return result

def start_game():
    narrate("--- WELCOME TO THE SHADOW DUNGEON ---")
    narrate("You stand in a cold, stone chamber. The air smells of damp earth.")
    narrate("Before you are two heavy oak doors.")

    choice = input("Do you open the LEFT door or the RIGHT door? (left/right): ").strip().lower()
    
    if choice == "left":
        left_door_room()
    elif choice == "right":
        right_door_room()
    else:
        narrate("Confused by your own indecision, you trip over your boots.")
        start_game()

def left_door_room():
    narrate("\nYou step inside. The door slams shut behind you!")
    narrate("A massive, sleeping Orc blocks the exit, guarding a glowing sword.")
    
    choice = input("Do you try to STEAL the sword or FIGHT the Orc? (steal/fight): ").strip().lower()
    
    if choice == "steal":
        narrate("\nYou notice a strange mechanical canister mounted on the wall near the sword.")
        narrate("It's a sleeping gas trap! You must crack the puzzle sequence to trigger it safely.")
        

        low, high, attempts = number_guessing_game.chosee_difficulty()
        success = number_guessing_game.play_round(low, high, attempts)
    
        if success:
            narrate("\n*Psssssssshh!*")
            narrate("A thick, sweet-smelling purple gas fills the room.")
            narrate("The Orc breathes it in, falling into a deep, magical slumber.")
            narrate("You calmly step over the beast, take the glowing sword, and escape!")
            narrate("YOU WIN!")
        else:
            narrate("\n*BEEP BEEP BEEP!*")
            narrate("You entered the wrong code! An alarm sounds instead of the gas trap.")
            narrate("The Orc's eyes snap open. He roars furiously, swinging his massive club...")
            narrate("GAME OVER.")
    
    elif choice == "fight":
        fight_orc_room()
    else:
        narrate("Invalid choice. The Orc sties in his sleep...")
        left_door_room()

def fight_orc_room():
    narrate("\nYou draw your weapon and yell a battle cry!")
    narrate("The Orc wakes up instantly, his red eyes burning with rage.")
    narrate("To pierce his heavy armor, you must quickly decipher the flashing runes!")
    narrate("You have exactly 10 seconds for each round. Ready... GO!")
    
    word_pool = ["sword", "shield", "dungeon", "battle", "shadow", "strike", "potion", "victory"]
    successful_strikes = 0
    total_rounds = 3

    for round_num in range(1, total_rounds+1):
        print(f"\n--- ROUND {round_num} / {total_rounds} ---")

        secret_word = random.choice(word_pool)
        current_shift = random.randint(1, 5)
        encrypted_puzzle = encrypt(secret_word, current_shift)
        
        print(f"Encrypted Rune: {encrypted_puzzle}")
        print(f"Hint: Decrypt by shifting backward by {current_shift} positions.")

        start_time = time.time()
        player_guess = input("Your answer: ").strip().lower()
        end_time = time.time()

        time_taken = end_time - start_time

        if time_taken > 10:
            narrate(f"\nTOO SLOW! You took {time_taken:.1f} seconds. The Orc delivers a devastating blow!")
            break
        
        if player_guess == secret_word:
            successful_strikes += 1
            print(f"DIRECT HIT! Decoded perfectly in {time_taken:.1f} seconds.")
        else:
            narrate(f"\nMISSED! The rune spell broke. The correct word was '{secret_word}'.")
            break
    if successful_strikes == total_rounds:
        narrate("\nWith a final brilliant strike, you shatter the last rune!")
        narrate("The Orc crashes heavily to the ground, completely defeated.")
        narrate("You claim the glowing sword from his hoard. YOU WIN!")
    else:
        narrate("\nThe Orc overpowers your defenses. Your vision goes dark...")
        narrate("GAME OVER.")

def right_door_room():
    narrate("\nYou slide through the right door into a glittering treasure room.")
    choice = input("Do you open the CHEST or look down the WELL? (chest/well): ").strip().lower()
    
    if choice == "chest":
        narrate("\nYou approach the grand gold chest. It is locked tight with a digital combinations pad.")
        narrate("To open the lock, you need to guess the correct frequency bypass code!")
        
        
        low, high, attempts = number_guessing_game.chosee_difficulty()
        success = number_guessing_game.play_round(low, high, attempts)
        
        if success:
            narrate("\n*CLICK!*")
            narrate("The heavy golden lid slowly swings open, revealing glittering wealth.")
            narrate("Right at the top sits a large, glowing silver key labeled 'DUNGEON EXIT'.")
            narrate("You grab the key, open the back door of the chamber, and step out into the sunlight!")
            narrate("YOU WIN!")
        else:
            narrate("\n*ERRRRRRR!*")
            narrate("The keypad flashes red. Spikes suddenly shoot out from the chest handles!")
            narrate("You couldn't bypass the trap mechanism in time.")
            narrate("GAME OVER.")
            
    elif choice == "well":
        narrate("\nYou lean over the edge of the well...")
        narrate("A giant slimy tentacle reaches out and pulls you into the abyss!")
        narrate("GAME OVER.")
    else:
        narrate("Invalid choice.")
        right_door_room()

if __name__ == "__main__":
    start_game()

