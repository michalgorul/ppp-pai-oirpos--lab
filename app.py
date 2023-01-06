from re import S
from xmlrpc.server import ServerHTMLDoc
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt6 Lab')
        self.setFixedHeight(400)
        self.setFixedWidth(600)
        self.move(60, 15)

        self.create_menu()
        self.create_tabs()
        self.create_editor()
        self.create_appender()

    
    def create_menu(self):
        self.menu = self.menuBar()

        self.fileMenu = self.menu.addMenu("File")
        self.task1Menu = self.menu.addMenu("Task 1")
        self.task2Menu = self.menu.addMenu("Task 2")
        self.task3Menu = self.menu.addMenu("Task 3")

        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)


        self.actionOpenImage = QAction('Open', self)
        self.actionOpenImage.setShortcut('Ctrl+G')
        self.actionOpenImage.triggered.connect(self.openImage)
        self.task1Menu.addAction(self.actionOpenImage)
        

        self.actionClearText = QAction('Clear', self)
        self.actionClearText.setShortcut('Ctrl+W')
        self.actionClearText.triggered.connect(self.clearText)
        self.task2Menu.addAction(self.actionClearText)

        self.actionOpenText = QAction('Open', self)
        self.actionOpenText.setShortcut('Ctrl+W')
        self.actionOpenText.triggered.connect(self.openText)
        self.task2Menu.addAction(self.actionOpenText)
        
        self.actionSaveText = QAction('Save', self)
        self.actionSaveText.setShortcut('Ctrl+S')
        self.actionSaveText.triggered.connect(self.saveText)
        self.task2Menu.addAction(self.actionSaveText)

        self.actionSaveTextAs = QAction('Save as', self)
        self.actionSaveTextAs.setShortcut('Ctrl+K')
        self.actionSaveTextAs.triggered.connect(self.saveTextAs)
        self.task2Menu.addAction(self.actionSaveTextAs)


        self.actionClearInput = QAction('Clear', self)
        self.actionClearInput.setShortcut('Ctrl+Q')
        self.actionClearInput.triggered.connect(self.clearInput)
        self.task3Menu.addAction(self.actionClearInput)
    
    def create_tabs(self):
        self.tabs = QTabWidget()
        
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        
        self.tabs.addTab(self.tab_1, "Task 1")        
        self.tabs.addTab(self.tab_2, "Task 2")        
        self.tabs.addTab(self.tab_3, "Task 3")
        
        self.setCentralWidget(self.tabs)


    def create_editor(self):
        self.text = ''
        self.editedFile = None
        outerLayout = QVBoxLayout(self.tab_2)
        innerLayout = QHBoxLayout()

        saveButton = QPushButton("Zapisz")
        saveButton.clicked.connect(self.save)

        clearButton = QPushButton("Wyczyść")
        clearButton.clicked.connect(self.clearText)

        innerLayout.addWidget(saveButton)
        innerLayout.addWidget(clearButton)

        self.editor = QPlainTextEdit()
        outerLayout.addWidget(self.editor)
        outerLayout.addLayout(innerLayout)
        

    def create_appender(self):
        layout = QGridLayout(self.tab_3)


        self.textInput1 = QLineEdit()
        textInput1Label = QLabel("Pole A")
        self.textInput1.textChanged.connect(self.append)

        self.textInput2 = QLineEdit()
        textInput2Label = QLabel("Pole B")
        self.textInput2.textChanged.connect(self.append)
        
        self.numericInput = QSpinBox()
        self.numericInput.setRange(0, 9999)
        numericInputLabel = QLabel("Pole C")
        self.numericInput.clear()
        self.numericInput.textChanged.connect(self.append)

        self.resultField = QLineEdit()
        self.resultField.setEnabled(False)
        resultFieldLabel = QLabel("Pole A+B+C")

        layout.addWidget(textInput1Label, 0, 0)
        layout.addWidget(self.textInput1, 0, 1)
        layout.addWidget(textInput2Label, 1, 0)
        layout.addWidget(self.textInput2, 1, 1)
        layout.addWidget(numericInputLabel, 2, 0)
        layout.addWidget(self.numericInput, 2, 1)
        layout.addWidget(resultFieldLabel, 3, 0)
        layout.addWidget(self.resultField, 3, 1)


    def openImage(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self.tab_1, "Wybierz plik obrazu",  "", "PNG (*.png)")

        if fileName:
            label = QLabel(self.tab_1)
            pixmap = QPixmap(fileName)
            label.setPixmap(pixmap.scaled(self.tab_1.width(), self.tab_1.height(), Qt.AspectRatioMode.KeepAspectRatio))
            label.show()

    def clearText(self):
        print("clear text")
        self.text = ''
        self.editor.setPlainText(self.text)

    def openText(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self.tab_2, "Wybierz plik tekstowy",  "", "TXT (*.txt)")

        if fileName:
            self.editedFile = fileName
            with open(self.editedFile, 'r') as file:
                self.text = file.read()
                print(file.read())
                self.editor.setPlainText(self.text)
        
    def saveText(self):
        if self.editedFile:
            self.save()
        else:
            self.saveTextAs()
            
    def saveTextAs(self):
        fileName, selectedFilter = QFileDialog.getSaveFileName(self.tab_2, "Wybierz plik tekstowy",  "", "TXT (*.txt)")

        if fileName:
            self.editedFile = fileName
            self.save()

    def save(self):
        text = self.editor.toPlainText()
        with open(self.editedFile, 'w') as file:
            file.write(text)

    def clearInput(self):
        self.textInput1.clear()
        self.textInput2.clear()
        self.numericInput.clear()
        self.numericInput.v
        self.resultField.clear()

        
    def append(self):
        self.resultField.setText(self.textInput1.text() + self.textInput2.text() + str(self.numericInput.value() ))
        

app = QApplication([])
win = Window()
win.show()
app.exec()

