import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QPalette, QColor

#construtor
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

#interface gráfica da calculadora
 #titulo, posições, layout
    def initUI(self):
        self.setWindowTitle('Calculadora')
        self.setGeometry(150, 150, 300, 400)  # Aumentei a altura para acomodar mais botões

        self.layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setStyleSheet("background-color: #5B0888; color: white; font-size: 18px;")
        self.layout.addWidget(self.display)

        button_layout = self.createButtonLayout()
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)
#botões
    def createButtonLayout(self):
        button_layout = QVBoxLayout()
        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in button_grid:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                if button_text.isnumeric():
                    button.setStyleSheet("background-color: #9D76C1; color: white; font-size: 18px;")
                else:
                    button.setStyleSheet("background-color: #6A1B9A; color: white; font-size: 18px;")
                button.clicked.connect(self.buttonClicked)
                row_layout.addWidget(button)
            button_layout.addLayout(row_layout)

        return button_layout

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText('Erro')
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

def main():
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
