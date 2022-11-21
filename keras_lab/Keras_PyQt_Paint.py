import sys
from typing import Callable
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QImage, QPainter, QPen, QBrush, QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton, \
    QLineEdit, QPlainTextEdit, QSpinBox
from PyQt6.QtGui import QPainter, QColor, QFont, QColorConstants

### Implementacja "Paint'a"


# Wielkością oraz kolorem pisaka
PEN_WIDTH = 16
PEN_COLOR = QColorConstants.White

# Wielkość pola do rysowania PIXMAP_SIZE x PIXMAP_SIZE
PIXMAP_SIZE = 256


# Prosta implementacja Painta
class Paint(QtWidgets.QMainWindow):

    def __init__(self, predict_function: Callable = None):
        """
        predict_function - funkcja wywoływana po zakończeniu rysowania.
        Powinna zwracać wartość (liczbę), która została zwrócona przez sieć neuronową
        """
        super().__init__()

        # Główny widżet przechowujący layout
        self.window = QWidget()

        # Tworzenie okna w którym będzie możliwość rysownia
        self.paint = QtWidgets.QLabel()
        self.paint.setFixedWidth(PIXMAP_SIZE)
        self.paint.setFixedHeight(PIXMAP_SIZE)
        self.image = QImage(PIXMAP_SIZE, PIXMAP_SIZE, QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.black)

        # Tworzenie layout'u przechowującego:
        # - okno do rysowania
        # - przycisk do wyczyszczenia obrazu
        # - okno wyświetlające odpowiedź sieci neuronowej
        self.layout = QGridLayout()
        self.prediction = QLineEdit()
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)

        self.layout.addWidget(self.prediction, 1, 0)
        self.layout.addWidget(self.clear_button, 1, 1)
        self.layout.addWidget(self.paint, 0, 0)

        self.prediction.setDisabled(1)
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)

        # Zmienne przechowujące ostatnią pozycję myszy
        self.lastPoint = QPoint()

        self.predict_function = predict_function

    def mousePressEvent(self, event: QMouseEvent):
        """
        Funkcja wywoływana, podczas naciśnięcia przycisku myszy.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(QPen(PEN_COLOR, PEN_WIDTH))
            painter.drawPoint(event.pos())
            self.drawing = True
            self.lastPoint = event.pos()
            self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        Funkcja wywoływana, podczas poruszania wskaźnikiem myszy z wciśniętym przyciskiem myszy.
        """
        if (event.buttons() & Qt.MouseButton.LeftButton) == Qt.MouseButton.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(PEN_COLOR, PEN_WIDTH))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        Funkcja wywoływana, podczas puszczenia przycisku myszy.
        """
        if event.button == Qt.MouseButton.LeftButton:
            self.drawing = False

        if self.predict_function:
            self.prediction.setText(str(self.predict_function(self.image)))

    def paintEvent(self, event: QtGui.QPaintEvent):
        """
        Funkcja wywoływana podczas rysowania okna
        """
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.paint.rect(), self.image, self.image.rect())

    def clear(self):
        """
        Funkcja czyszcząca pole rysowania
        """
        self.image.fill(QColorConstants.Black)
        self.update()


import Keras_PyQt_Paint_Model as kppm

model = kppm.get_model()

app = QtWidgets.QApplication(sys.argv)
window = Paint(lambda x: kppm.predict(x, model))
window.show()
app.exec()
