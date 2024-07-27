# -*- coding: utf-8 -*-
"""FashionMNIST.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16UyTzz30UiDsScmW3MkX2U-daaxtEnmk

**Setting Seed**
"""

# set random seeds for reproducablity
import random
random.seed(177)

import numpy as np
np.random.seed(177)

import tensorflow as tf
tf.random.set_seed(177)

import matplotlib.pyplot as plt

"""**dependencies**"""

from tensorflow import keras
fashion_mnist_data=keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=fashion_mnist_data.load_data()
# fashion mnist datset has 2 tuples
# trainimage->trainimagelabels,
# test_image &test_imagelabels

type(train_images)

train_images.shape
# 60,000 images :Grey Scaled

train_images[0].shape
# each of dim : 28*28

train_labels

type(train_images[0])

plt.imshow(train_images[0],cmap='gray')

train_labels[0]

"""**class_name=['Tshirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','SNeaker','Bag','Ankle Boot']**"""

train_images,test_images=train_images/255,test_images/255

train_images[0]

# reshaping to (4) sized (batch_size,dim1,dim2,type)
train_images=train_images.reshape(train_images.shape[0],28,28,1)
test_images=test_images.reshape(test_images.shape[0],28,28,1)

from keras.models import Sequential
from keras.layers import Dense,BatchNormalization,MaxPooling2D,Conv2D,Dropout,Flatten
from keras.losses import SparseCategoricalCrossentropy

train_images.shape

test_images.shape

model=Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(28,28,1)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='adam',loss=SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])

model.summary()

history=model.fit(train_images,train_labels,epochs=10,validation_data=(test_images,test_labels))

test_loss,test_acc=model.evaluate(test_images,test_labels,verbose=2)
print(test_acc)

plt.plot(history.history['val_accuracy'])
plt.plot(history.history['accuracy'])

plt.plot(history.history['val_loss'])
plt.plot(history.history['loss'])

model.save('model_mnist_fashion.h5')

tf.__version__

