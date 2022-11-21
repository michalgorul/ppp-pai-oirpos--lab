
# Implementacja obsługi ładowania i predykcji modelu

import cv2
import numpy as np
from PyQt6.QtGui import QImage

from keras_lab.utils import get_model as model, predict_pyqt


def qimage_to_array(image: QImage):
    """
    Funkcja konwertująca obiekt QImage do numpy array
    """
    image = image.convertToFormat(QImage.Format.Format_Grayscale8)
    ptr = image.bits()
    ptr.setsize(image.sizeInBytes())
    numpy_array = np.array(ptr).reshape(image.height(), image.width(), 1)

    # wykorzystanie bibloteki OpenCV do wyświetlenia obrazu po konwersji
    cv2.imshow('Check if the function works!', numpy_array)
    return numpy_array


def predict(image: QImage, m):
    """
    Funkcja wykorzystująca załadowany model sieci neuronowej do predykcji znaku na obrazie

    Należy dodać w niej odpowiedni kod do obsługi załadowanego modelu
    """
    numpy_array = qimage_to_array(image)

    # wykorzystanie bibloteki OpenCV do zmiany wielkości obrazu do wielkości obrazów używanych w zbiorze MNIST
    numpy_array = cv2.resize(numpy_array, (28, 28))

    # wykorzystanie bibloteki OpenCV do wyświetlenia obrazu po konwersji
    cv2.imshow('Check if the function works!!', numpy_array)

    return predict_pyqt(m, numpy_array)
    # return 3


def get_model():
    """
    Funkcja wczytująca nauczony model sieci neuronowej

    Należy dodać w niej odpowiedni kod do wczytywania na modelu oraz wag
    """
    return model()
