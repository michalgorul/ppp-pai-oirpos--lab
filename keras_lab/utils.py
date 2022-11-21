import operator

import numpy as np
from keras import Sequential
from keras.datasets import mnist
from keras.layers import Dense
from keras.models import load_model
from keras.utils import load_img, np_utils
from matplotlib import pyplot as plt


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


def load_data():
    # Wczytywanie danych
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Splaszczenie obrazów z28 * 28 pikseli do 784 elementowego vector'a
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape((X_train.shape[0], num_pixels)).astype('float32')
    X_test = X_test.reshape((X_test.shape[0], num_pixels)).astype('float32')

    # Normalizacja danych o wartosciach od 0 do 255 do wartości od 0 do 1
    X_train = X_train / 255
    X_test = X_test / 255

    # Pobranie i stworzenie listy klas dla danych
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)

    # Wyciągniecie liczby klas
    num_classes = y_test.shape[1]

    return num_pixels, num_classes, X_train, y_train, X_test, y_test


def get_model():
    model = None
    try:
        model = load_model('model_dense.h5')
        print(model)
        return model
    except Exception:
        pass

    if not model:
        # Tworzenie modelu sieci

        num_pixels, num_classes, X_train, y_train, X_test, y_test = load_data()

        model = Sequential()

        # Dodanie pierwszej warstwy odpowiedzialnej za odebranie danych obrazu - liczba neuronow = liczbie pikseli
        model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))

        # TODO ZADANIE 1
        model.add(Dense(num_pixels, activation='relu'))
        model.add(Dense(num_pixels, activation='relu'))

        # Dodanie drugiej warstwy odpowiedzialnej za klasę - liczbla neuronow = liczba klas
        model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))

        # Kompilacja modelu
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Uczenie modelu danymi
        # epoch - liczba iteracji
        # batch_size - liczba elemenów z danych treningowych branych podczas pojedyńczego przejścia funkcji uczącej
        history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=1)

        # wyświetlenie wykresu przedstawiającego historię uczenia sieci
        plt.subplot(2, 1, 1)
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'val'], loc='upper left')

        plt.subplot(2, 1, 2)
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'val'], loc='upper left')
        plt.show()

        save(model, 'model_dense.h5')
        return model


def load_image(path):
    image = load_img(path, target_size=(28, 28), color_mode="grayscale")
    img = np.array(image)
    img = img / 255.0
    return img.reshape(1, 784).astype('float32')


# TODO ZADANIE 3
def predict(model):
    img = load_image("test3.png")
    prediction = model.predict(img)
    print("Number", "\tPrediction")
    for i, value in enumerate(prediction[0]):
        print(i, "\t\t", round(value, 3)*100, "%")


# TODO ZADANIE 4
def predict_pyqt(model, numpy_arr):
    img = numpy_arr / 255.0
    img = img.reshape(1, 784).astype('float32')
    prediction = model.predict(img)
    print("Number", "\tPrediction")
    for i, value in enumerate(prediction[0]):
        print(i, "\t\t", round(value, 2) * 100, "%")
    max_index, max_value = max(enumerate(prediction[0]), key=operator.itemgetter(1))
    return str(max_index)
