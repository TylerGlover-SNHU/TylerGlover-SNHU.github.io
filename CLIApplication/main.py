from rich.console import Console # library used to stylize console output
from classifier import Classifier
from database import MLDatabase
import io
import os

console = Console() # console object used for stylized output
classifier = Classifier() # instance of custom classifier object
db = MLDatabase()  # Instance of database service


# Prints menu for application
def print_menu():
    console.print("Make a selection:", style="bold blue")
    console.print("1 - Classify a digit image", style="white on black")
    console.print("2 - Classify and save data", style="white on black")
    console.print("3 - Print classification stats", style="white on black")
    console.print("4 - Exit", style="white on black")

def get_file():
    # Get input from user for file name
    # Files restricted to those in Digits folder to prevent access of system files
    filename = input('Enter filename for digit image located in Digits folder: ')
    filename = os.path.basename(filename)
    filepath = os.path.join("Digits", filename)
    return filepath

# While loop variable to continue execution
repeat = True

while repeat:
    print_menu()

    choice = input() # get user choice from menu prompt

    match choice:
        # Classifies a digit and prints result to terminal
        case '1':
            # Get filepath from user
            image_path = get_file()

            # Get image classification
            try:
                category, probability, image = classifier.classify(image_path)
            # Handle case where image could not be found and None is returned from classify
            except TypeError:
                continue
            print(f"The image is classified as a {category}.\n")

        # Classifies a digit and prints result to terminal
        # Obtains relevant metadata from user to save for later model analysis
        # Saves data to SQL database
        case '2':
            # Get input from user for file name
            image_path = get_file()

            # Get image classification
            try:
                category, probability, image = classifier.classify(image_path)
            # Handle case where image could not be found and None is returned from classify
            except TypeError:
                continue
            print(f"The image is classified as a {category}.\n")

            # Get actual classification from user
            digit_type = input("Enter the true category for the digit: ")

            # Convert image to bytes to save as blob
            image_bytes = io.BytesIO()
            image.save(image_bytes, format='PNG')
            image_bytes = image_bytes.getvalue()

            # Add classification example to database
            db.insert_classification(int(category), int(digit_type), float(probability), image_bytes)

        # Obtains stats from SQL database regarding model performance and prints
        # stats to the terminal
        case '3':
            # Get stats from classification data object
            data = db.get_all_classifications()
            percents = data.get_digit_percent_correct()
            total_right = data.get_num_correct()
            total_classified = data.get_num_classifications()
            avg_confidence = data.get_average_confidence()

            # Print classification stats to terminal
            console.print("Image classification stats:", style="bold blue")
            console.print("---------------------------", style="black bold")
            console.print(f"Correct classifications: {total_right}", style="bold green")
            console.print(f"Total classifications: {total_classified}", style="bold green")
            console.print(f"Percent correct overall: {float(total_right) / total_classified}\n", style="bold green")
            console.print("Percent correct by digit", style="bold blue")
            console.print("---------------------------", style="black bold")
            for i in range(10):
                console.print(f"{i}: {percents[i]}", style="bold green")
            print('\n')
            console.print("Average confidence by digit", style="bold blue")
            console.print("---------------------------", style="black bold")
            for i in range(10):
                console.print(f"{i}: {avg_confidence[i]}", style="bold green")
            print('\n')

        # Sets loop variable to False to end execution
        case '4':
            repeat = False
            db.close_connection() # Close database connection

        # Default case for incorrect input
        case _:
            print("Invalid input selected. Please try again.")