import random

def guess_game():
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")
    
    # Set the range of numbers and the number of attempts
    lower_bound = 1
    upper_bound = 100
    max_attempts = 10
    
    # Generate a random number for the player to guess
    secret_number = random.randint(lower_bound, upper_bound)
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used up all {max_attempts} attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_game()
