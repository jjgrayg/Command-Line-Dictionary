import json
from difflib import SequenceMatcher as sq
from difflib import get_close_matches

# Load in the dictionary data
data = json.load(open("C:\\Users\\jjgra\\OneDrive\\Desktop\\Code Repos\\Python Repos\\10_realworld_apps\\Dictionary\\data.json"))

### Define necessary functions

# Returns the defintions of the word
def returnDef(word):
    if word in data:                                                                # If the input is valid and found simply return the definitions
        return data[word]
    elif word.lower() in data:                                                      # If the input isn't initally found, check for an accidental capital letter
        return data[word.lower()]
    elif word.lower().title() in data:                                              # If it still is not found check for a proper title
        return data[word.lower().title()]
    elif word.upper() in data:                                                      # Check if it is an acronym
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), n = 3, cutoff = .6)) > 0:         # If the word is not found but there are close matches check if the word they mean is present
        close_matches = get_close_matches(word, data.keys(), n = 3, cutoff = .6)
        for i in range(len(close_matches)):                                         # Iterate through each close match
            misspellCheck = input('Did you mean "' + (close_matches[i]) + '"? Enter Y for yes and N for no: ')
            while (misspellCheck.lower() != 'y') & (misspellCheck.lower() != 'n'):  # Loop until a valid answer is given
                misspellCheck = input('I do not understand. Please enter Y or N: ')
            if misspellCheck.lower() == 'y':                                        # If the word they mean is found return that word
                return data[close_matches[i]]
        return ['ERROR: That word does not exist in this dictionary.']              # If the word is not found return an error
    else:
        return ['ERROR: That word does not exist in this dictionary.']              # If there are no close matches and the word does not exist in the dictionary return an error message


# Prints the definitions neatly
def printDef(deflist):
    print('\n')
    index = 1;                                                                     
    for i in deflist:                                                               # Iterate through the whole definition list printing each possible definition
        print(('{}.) ' + i).format(index))
        index += 1
    print('\n')

# Create a loop to run the program until the user types 0
def start():                                                            # Initialize the userInput var so the while loop can be executed
    while True:
        userInput = input('Enter a word you would like the definition of (Type 0 to exit): ')
        if userInput != '0':                                                        # If the user enters anything other than 0 run the program
            printDef(returnDef(userInput))
        elif userInput == '0':                                                      # If 0 is entered exit
            print("Exiting...")
            break

# Start the program
start()