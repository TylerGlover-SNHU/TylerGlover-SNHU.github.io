import sqlite3
# New objects defined for project to hold classification data
from classification import Classification, ClassificationData

# Database service object
class MLDatabase:
    def __init__(self):
        # Initialize connection and cursor for database transactions
        self.connection = sqlite3.connect("MLDigits.db")
        self.cursor = self.connection.cursor()

        # Create table for classification data if it does not exist yet
        self.create_tables()

    # Create table for classification data if it does not exist yet
    def create_tables(self):
        # Get tables currently in database
        tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE name='classification'")

        # Check to see if table was returned from query
        # If table does not exist, create new instance of table
        if not tables.fetchall():
            self.cursor.execute("""
                CREATE TABLE classification (
                    id INTEGER PRIMARY KEY,
                    guess INTEGER,
                    actual INTEGER,
                    confidence REAL,
                    image BLOB
                );
            """
            )
            print("Classification table added to database.")

    # Insert new classification record
    def insert_classification(self, guess, actual, confidence, image):
        try:
            # Parameterized queries used to prevent SQL injection
            query = "INSERT INTO classification (guess, actual, confidence, image) VALUES (?, ?, ?, ?)"
            values = (guess, actual, confidence, image)
            self.cursor.execute(query, values)
            self.connection.commit()
            return True # Returns true if the commit was successful
        # Rollback the insert if an error occurs
        except sqlite3.IntegrityError as e:
            print(f"Error inserting new record: {e}")
            self.connection.rollback()
            return False # Return false when query is unsuccessful

    # Get all classification from database
    def get_all_classifications(self):
        try:
            query = "SELECT * FROM classification"
            data = ClassificationData() # Create classification data object to hold query data
            classifications = self.cursor.execute(query)
            classifications = classifications.fetchall()
            # For each returned record, add it to the data object
            for classification in classifications:
                class_id = classification[0]
                class_guess = classification[1]
                class_actual = classification[2]
                class_confidence = classification[3]
                classification_data = Classification(class_id, class_guess, class_actual, class_confidence)
                data.add(classification_data)
            return data
        except sqlite3.DatabaseError:
            print('Error retrieving classification data.')

    # Close connection so that application can exit cleanly.
    def close_connection(self):
        self.cursor = None
        self.connection.close()