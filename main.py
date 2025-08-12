import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gob Goblin")

        button = QPushButton("Feed!")

        button.setCheckable(True)
        button.clicked.connect(self.feed_me)
        self.setCentralWidget(button)
    def feed_me(self):
        print("clicked")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()