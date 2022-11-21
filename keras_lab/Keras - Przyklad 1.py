# Ładowanie potrzebych modułów
# MNIST - zbiór obrazów z odręcznie pisanymi cyframi od 0 do 9
# Sequential- model sekwencyjny sieci neuronowej
# Dense - warsta gęsta sieci

from keras_lab.utils import predict, get_model, load_data

model = get_model()
data = load_data()
# Testowanie modelu
scores = model.evaluate(data[4], data[5], verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))
print("Accuracy:", scores[1]*100, '%')

print(predict(model))



