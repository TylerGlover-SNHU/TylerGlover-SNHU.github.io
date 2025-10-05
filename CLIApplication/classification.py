# Class to store classification data
class Classification:
    def __init__(self, id: int, guess: int, actual: int, confidence: float):
        self.id = id
        self. guess = guess
        self.actual = actual
        self.confidence = confidence

# Class to hold several classification data points and gives relevant statistics
class ClassificationData:
    def __init__(self):
        # Class list to hold classification data
        self.classification_list = []

    # Add a new classification data point to the class list
    def add(self, classification: Classification):
        self.classification_list.append(classification)

    # Returns total number of classification data points in class list
    def get_num_classifications(self):
        return len(self.classification_list)

    # Gets the total correct classifications stored
    def get_num_correct(self):
        count = 0
        for classification in self.classification_list:
            if classification.guess == classification.actual:
                count += 1
        return count

    # Gets percentage of correct classifications for each digit
    def get_digit_percent_correct(self):
        # Initialize lists to store classification counts
        count_right = [0 for _ in range(10)]
        total_count = [0 for _ in range(10)]

        # Initialize list to store percentage data for each digit
        percents = []

        # Increments total counts for each digit and the number of correct classifications
        for classification in self.classification_list:
            match classification.actual:
                case 0:
                    total_count[0] += 1
                    if classification.guess == 0:
                        count_right[0] += 1
                case 1:
                    total_count[1] += 1
                    if classification.guess == 1:
                        count_right[1] += 1
                case 2:
                    total_count[2] += 1
                    if classification.guess == 2:
                        count_right[2] += 1
                case 3:
                    total_count[3] += 1
                    if classification.guess == 3:
                        count_right[3] += 1
                case 4:
                    total_count[4] += 1
                    if classification.guess == 4:
                        count_right[4] += 1
                case 5:
                    total_count[5] += 1
                    if classification.guess == 5:
                        count_right[5] += 1
                case 6:
                    total_count[6] += 1
                    if classification.guess == 6:
                        count_right[6] += 1
                case 7:
                    total_count[7] += 1
                    if classification.guess == 7:
                        count_right[7] += 1
                case 8:
                    total_count[8] += 1
                    if classification.guess == 8:
                        count_right[8] += 1
                case 9:
                    total_count[9] += 1
                    if classification.guess == 9:
                        count_right[9] += 9
                case _:
                    pass

        # Calculate percent correct based on digit counts
        for i in range(10):
            if total_count[i] != 0:
                percent = (float(count_right[i]) / float(total_count[i])) * 100
            else:
                percent = 0
            percents.append(percent)

        return percents

    # Get confidence levels for each digit
    def get_average_confidence(self):
        # Initialize list to store classification confidences and counts
        avg_confidence = [0 for _ in range(10)]
        digit_count = [0 for _ in range(10)]

        # Creates sum of confidences for each digit
        for classification in self.classification_list:
            digit = classification.actual
            avg_confidence[digit] += classification.confidence
            digit_count[digit] += 1

        # Calculates average confidence level for each digit
        for i in range(10):
            avg_confidence[i] /= float(digit_count[i])
        return avg_confidence