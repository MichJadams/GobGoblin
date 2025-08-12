from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QTableWidgetItem


class SelectedApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_job = None
        layout = QHBoxLayout()
        column_one = QVBoxLayout()

        column_two = QVBoxLayout()
        layout.addLayout(column_one)
        layout.addLayout(column_two)

        self.job_title = QLabel("-")
        self.company = QLabel("-")
        self.status = QLabel("-")

        column_one.addWidget(QLabel("Job Title"))
        column_two.addWidget(self.job_title)

        column_one.addWidget(QLabel("Company"))
        column_two.addWidget(self.company)

        column_one.addWidget(QLabel("Status"))
        column_two.addWidget(self.status)


        self.setLayout(layout)


    def set_selected_job(self, data: QTableWidgetItem):
        table = data.tableWidget()
        self.job_title.setText(table.item(data.row(), 0).text())
        self.company.setText(table.item(data.row(), 1).text())
        self.status.setText(table.item(data.row(), 2).text())

