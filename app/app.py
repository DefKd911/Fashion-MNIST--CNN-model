import os
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

working_dir = os.path.dirname(os.path.abspath(__file__))
modelpath = f"{working_dir}/trained_models/model_mnist_fashion.h5"

# loading pre-trained model
model = tf.keras.models.load_model(modelpath)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

def process_image(image):
    img = Image.open(image)
    img = img.resize((28, 28))
    img = img.convert('L')
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape((1, 28, 28, 1))
    return img_array

@app.route('/')
def index():
    return render_template('index.html', class_names=class_names)

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        img_array = process_image(file)
        result = model.predict(img_array)
        predicted_class = np.argmax(result)
        prediction = class_names[predicted_class]
        confidence = float(result[0][predicted_class])
        return jsonify({'prediction': prediction, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)