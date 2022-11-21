# Ładowanie potrzebych modułów
# MNIST - zbiór obrazów z odręcznie pisanymi cyframi od 0 do 9
# Sequential- model sekwencyjny sieci neuronowej
# Dense - warsta gęsta sieci
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from matplotlib import pyplot as plt

from keras_lab.utils import save, load, predict

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

model = None
try:
    model = load('model.h5')
except Exception:
    pass

if not model:
    # Tworzenie modelu sieci
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

# Testowanie modelu
scores = model.evaluate(X_test, y_test, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))
print("Accuracy:", scores[1]*100, '%')

save(model, 'model.h5')

print(predict("test3.png", model))



