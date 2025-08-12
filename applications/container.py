from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

from applications.application_table import ApplicationTable
from applications.extension_server import ExtensionServer
from components.selected_application import SelectedApplication


class ApplicationContainer(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database

        self.server_thread = None
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.toggle_button = QPushButton("Toggle Server")
        self.toggle_button.clicked.connect(self.toggle_server)
        layout.addWidget(self.toggle_button)
        table = ApplicationTable(self.database)
        layout.addWidget(table)

        selected_application = SelectedApplication()
        table.itemPressed.connect(selected_application.set_selected_job)

        layout.addWidget(selected_application)

    def toggle_server(self):
        if self.server_thread and self.server_thread.is_running():
            self.server_thread.stop()
            self.server_thread.join(timeout=2)
            self.server_thread = None
        else:
            self.server_thread = ExtensionServer(self.database)
            print("starting server")
            self.server_thread.start()
