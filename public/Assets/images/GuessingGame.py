# Michael Maniatis
# 100876436

# Import random to pick a random
import random

# This function allows the user to enter in a number between the min and max value
def input_range(min_range,max_range,output_string):
    # Loop so that we don't exit until we have sanitized input
    while True:
        # Have the user enter in a string
        user_input = input(output_string + f" ({min_range}-{max_range}):\n")

        # Exit conditions
        if user_input in ["stop","exit"]:
            print("Game Ends")
            exit()
        
        # If the user put in a positive integer
        if user_input.isdigit():
            # typecast the input as an int
            user_input = int(user_input)
            # If the number is in the range
            if user_input >= min_range and user_input <= max_range:
                # exit loop
                return user_input
            else:
                # since number wasn't in range, prompt user with range
                print(f"That number is not within the specified range! ({min_range}-{max_range})\n")
        else:
            # Print out that the input was wrong
            print("That is not a number!\n")
    

def output(word,letters,guesses_left,previous_guesses):
    # This checks to see which letters have been guessed that are in the word
    outputted_word = ""

    # For each letter in the word
    for i in range(len(word)):
        # Check if that letter has been guessed
        if letters[i] == True:
            # Add the letter to the output
            outputted_word += word[i]
        else:
            # Otherwise censor it
            outputted_word += "*"
    
    # Print out some output
    print(f"\nWord is: {outputted_word}")
    print(f"Guesses remaining: {guesses_left}")

    outputted_guessed_letters = ""
    # Loop through all the previous guesses
    for i in range(len(previous_guesses)):
        # Add the letters guessed
        outputted_guessed_letters += previous_guesses[i]
        # If the letter isn't the last one, then add a comma
        if i + 1 < len(previous_guesses):
            outputted_guessed_letters += ", "

    # Print output
    print(f"Previous Guesses: {outputted_guessed_letters}")

def guess(word,correct_letters,previous_guesses,guesses_left):
    # input sanitation loop
    while True:

        # Have the user enter in a letter and make it lowercase
        inputted_letter = input("Choose a letter to guess:").lower()

        # Exit conditions
        if inputted_letter in ["stop","exit"]:
            print("Game Ends")
            exit()
        
        # If the input is not a letter
        if not inputted_letter.isalpha():
            print("That is not a Letter! Please try again!")
            print(f"Guesses remaining: {guesses_left}")
        
        # If the input is longer than one char
        elif len(inputted_letter) > 1:
            print("That is more than a letter! Please try again!")
            print(f"Guesses remaining: {guesses_left}")
        
        # If the letter has been guessed before
        elif inputted_letter in previous_guesses:
            # If that guess was correct
            if inputted_letter in word:
                print("That letter has been guessed before and IS in the word! Please try again!")
            # If that guess was wrong
            else:
                print("That letter has been guessed before and IS NOT in the word! Please try again!")
            print(f"Guesses remaining: {guesses_left}")
        
        # Letter has not been guessed before
        else:
            # Add it to guesses
            previous_guesses.append(inputted_letter)

            # If the guess is correct
            if inputted_letter in word:
                
                print(f"Hooray, '{inputted_letter}' is in the word!")
                
                # Loop through each letter to make sure
                # that if the letter appears more than once,
                # We still show it in the output
                for i in range(len(word)):  
                    if word[i] == inputted_letter:
                        correct_letters[i] = True
                
            # If the letter is not in the word
            else:
                print(f"Sorry, '{inputted_letter}' is NOT in the word!")

            return correct_letters,previous_guesses

def main():
    # Word banks
    four_letter_words = ["dogs","cats","hole","book","easy","hard","dart"]
    five_letter_words = ["brick","clock","seven","wheel","darts"]

    # The letters that have been guessed
    previous_guesses = []
    
    # Prompt the user for the amount of guesses they want
    guesses = input_range(1,10,"Please Enter the amount of guesses")

    # Prompt the user for what word length they want
    minimum_word_len = input_range(4,5,"Please Enter the word length")  

    # Pick a random word using the random.choice function
    if minimum_word_len == 4:
        selected_word = random.choice(four_letter_words)
    else:
        selected_word = random.choice(five_letter_words)

    # Set all letters as not guessed, i.e. false
    correct_letters = []
    for _ in range(minimum_word_len):
        correct_letters.append(False)
    
    # While the user still has guesses and still hasn't guessed all the letters
    while guesses > 0 and (False in correct_letters):
        # Show the user the output
        output(selected_word,correct_letters,guesses,previous_guesses)

        # Prompt the user to guess
        correct_letters,previous_guesses = guess(selected_word,correct_letters,previous_guesses,guesses)

        # Remove a guess
        guesses -= 1

    # If the user didn't get all the letters
    if False in correct_letters:
        print("No more guesses left! Game Ends!")
        print(f"You lost! The word was {selected_word}! Better luck next time!")

    # If the user won
    else:
        print(f"You Won! The word was {selected_word}! Good Job!")
    
    # Basic loop bool to guaruntee input
    input_bool = True
    while input_bool:

        # Prompt user
        play_again = input("\nWould you like to play again? (Y/N)")

        # If the word starts with a y
        if play_again.lower().startswith("y"):
            input_bool = False
            # Reboot the game
            main()
        
        # If the word starts with an n
        elif play_again.lower().startswith("n"):
            input_bool = False
            print("Thank you for playing! Have a wonderful day!")
        
        # If the user put in an invalid option
        else:
            print("That is not a valid option!")
main()