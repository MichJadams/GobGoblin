import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import QSize

from applications.container import ApplicationContainer
from applications.database import Database
from components.menu import Menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gob Goblin")
        self.database = Database()
        self.menu = Menu()
        self.main_content = ApplicationContainer(self.database)

        layout = QHBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.main_content)

        container = QWidget()
        container.setLayout(layout)
        self.setWindowIcon(QIcon("resources/gob_goblin.png"))
        self.setCentralWidget(container)
        self.setFixedSize(800, 600)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())