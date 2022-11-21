import numpy as np
from keras.models import load_model
from keras.utils import load_img


# PATH
# 'my_model.h5'
# TODO ZADANIE 2
# creates a HDF5 file 'my_model.h5'
def save(model, path):
    model.save(path)


# returns a compiled model
# identical to the previous one
def load(path):
    return load_model(path)


# TODO ZADANIE 3
def predict(img_path, model):
    image = load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1, 784).astype('float32')
    prediction = model.predict(img)
    print("Number", "\tPrediction")
    for i, value in enumerate(prediction[0]):
        print(i, "\t\t", round(value, 3)*100, "%")

