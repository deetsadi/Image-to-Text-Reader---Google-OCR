import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = [text.description for text in response.text_annotations]
    print('Texts:\n')
    #for text in texts:
        #print('\n"{}"'.format(text.description))

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))
#detect_text("/Users/adityasridhar/Downloads/slidenote.jpg")
detect_text("/Users/adityasridhar/Downloads/letternote.jpg")
#detect_text("/Users/adityasridhar/Downloads/receipttest.jpg")