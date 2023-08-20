import random

#colors used in passcode | The number of tries/ lives a person has 
COLORS = ["R","G","B","Y","W","O",]
TRIES = 10
remaining_attempts = 10
CODE_LENGTH = 4 

#generate code function
def generate_code():
    code = []

    #insert random colors into list
    for instance in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

#generating code
code = generate_code()

#user code guess function 
def guess_code():
    while True:
        guess = input("Enter Code: ").upper().split(" ")
        

        if len(guess) != CODE_LENGTH:
            print(f"The Passcode Contains {CODE_LENGTH} Characters.")
            continue

        #checking user guess against available characters
        for color in guess:
            if color not in COLORS:
                print(f"Wrong Character: {color}. Try Again.")
                break
            else:
                break

        return guess
    
    #checking user guess against actual passcode
def check_code(guess, actual):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    #establishing a count for colors
    for color in actual:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    
    #matching guess and actual for correct position
    for guess_color, actual_color in zip(guess, actual):
        if guess_color == actual_color:
            correct_position += 1
            color_counts[guess_color] -= 1

    #matching guess and actual for incorrect position
    for guess_color, actual_color in zip(guess, actual):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position += 1
            color_counts[guess_color] -= 1
    
    return correct_position, incorrect_position

#Game Logic

def game():
    print("System Was Powered On")
    print(f"Please Enter Your Four Character Passcode In No More Than {TRIES} Attempts")
    print("Valid Characters Must Be Seperated With A Space And They Are:", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_position, incorrect_position =  check_code(guess, code)

        if correct_position != CODE_LENGTH:
            global remaining_attempts
            remaining_attempts  -=  1

        if correct_position == CODE_LENGTH:
            print(f"You guessed the code in {attempts} attempts")
            break
        
        print(f"Correct Positions: {correct_position} | Incorrect Position: {incorrect_position}")
        print(f"You Have {remaining_attempts} Attempts Remaining.")

    else:
            print("Attempts Exausted. The System Was Locked.")
            print("The Code Was: " *code)

if __name__ == "__main__":
    game()