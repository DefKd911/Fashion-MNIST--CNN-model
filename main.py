import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

working_dir=os.path.dirname(os.path.abspath(__file__))
modelpath=f"{working_dir}/trained_models/model_mnist_fashion.h5"

# loading pre-trained_model
model=tf.keras.models.load_model(modelpath)

class_names=['T-shirt/top','Trouser','Pullover','Dress','Coat',
            'Sandal','Shirt','Sneaker','Bag','Ankel Bool']

def process_image(image):
    img=Image.open(image)
    img=img.resize((28,28))
    img=img.convert('L')
    img_array=np.array(img)/ 255.0
    img_array=img_array.reshape((1,28,28,1))
    return img_array
# StreamLit App
st.title('Fashion Item classifier by MNIST')

uploaded_image=st.file_uploader("Upload an Image ...",type=['jpg','png','jpeg'])

if uploaded_image is not None:
    image=Image.open(uploaded_image)
    col1,col2= st.columns(2)

    with col1:
        if st.button('Classify'):

            img_array=process_image(uploaded_image)
            result=model.predict(img_array)
            predicted_class=np.argmax(result)
            prediction=class_names[predicted_class]

            st.success(f'Prediction: {prediction}')



















            






