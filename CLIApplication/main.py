from rich.console import Console # library used to stylize console output
from classifier import Classifier
import os

console = Console() # console object used for stylized output
classifier = Classifier() # instance of custom classifier object


# Prints menu for application
def print_menu():
    console.print("Make a selection:", style="bold blue")
    console.print("1 - Classify a digit image", style="white on black")
    console.print("2 - Classify and save data", style="white on black")
    console.print("3 - Print classification stats", style="white on black")
    console.print("4 - Exit", style="white on black")

# While loop variable to continue execution
repeat = True

while repeat:
    print_menu()

    choice = input() # get user choice from menu prompt

    match choice:
        # Classifies a digit and prints result to terminal
        case '1':
            # Get input from user for file name
            # Files restricted to those in Digits folder to prevent access of system files
            filename = input('Enter filename for digit image located in Digits folder: ')
            filename = os.path.basename(filename)
            filepath = os.path.join("Digits", filename)

            # Get image classification
            try:
                category, probability = classifier.classify(filepath)
            # Handle case where image could not be found and None is returned from classify
            except TypeError:
                continue
            print(f"The image is classified as a {category}.")

        # Classifies a digit and prints result to terminal
        # Obtains relevant metadata from user to save for later model analysis
        # Saves data to SQL database
        case '2':
            pass

        # Obtains stats from SQL database regarding model performance and prints
        # stats to the terminal
        case '3':
            pass

        # Sets loop variable to False to end execution
        case '4':
            repeat = False

        # Default case for incorrect input
        case _:
            print("Invalid input selected. Please try again.")