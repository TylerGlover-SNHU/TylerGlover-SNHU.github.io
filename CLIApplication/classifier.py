from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Takes an image and returns array formatted in the mnist dataset format
def format_image_data(image):
    # mnist images are 28 x 28 pixels
    # resize the image to match
    new_size = (28, 28)
    image = image.resize(new_size)

    # mnist images stored using grayscale values
    # Convert image to grayscale
    image = image.convert('L')

    # Convert image to np array
    image_array = np.array(image)

    # Convert the 28 x 28 array to a single column vector
    RESHAPED = 784
    image_array = image_array.reshape(1, RESHAPED)
    image_array = image_array.astype('float32')

    # mnist samples are on a completely black background
    # photos taken for classification are imperfect
    # Reduce background noise by reducing the background values
    image_array -= np.min(image_array)

    # Normalize the data based on the largest value in the array
    array_max = np.max(image_array)
    image_array /= array_max

    # mnist digits are white on a black background
    # digits written on paper are on a white background
    # invert the grayscale values so the digit is white and the
    # background is black
    image_array = 1 - image_array

    # With background noise filtered out, set background values to zero
    # to match mnist format
    for i in range(len(image_array[0])):
        if image_array[0][i] < 0.1:
            image_array[0][i] = 0

    return image_array

# Class which uses a sequential neural network trained on the mnist database to classify
# handwritten digits
class Classifier:
    def __init__(self):
        # Load the trained model in safe mode which mitigates arbitrary code
        # execution concerns
        self. model = load_model('digit_classification_model.keras', safe_mode=True)

    # Uses instance model to classify a handwritten digit image
    def classify(self, filepath: str):
        try:
            image = Image.open(filepath) # obtain image
            image_array = format_image_data(image) # format image for prediction
            prob = self.model.predict(image_array) # get prediction vector from model
            return np.argmax(prob), np.max(prob) # return

        # Handle cases where user enters a filename that does not exist
        except FileNotFoundError:
            print('The file could not be located. Confirm file exists in the Digits folder.')
        # Handle operating system related file errors
        except OSError:
            print('Operating system error. Confirm that you have the proper file permissions.')