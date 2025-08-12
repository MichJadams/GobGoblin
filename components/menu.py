from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        applications_btn = QPushButton("Applications")
        layout = QVBoxLayout()
        layout.addWidget(applications_btn)
        self.setLayout(layout)
