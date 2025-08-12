from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from applications.database import Database


class ApplicationTable(QTableWidget):
    def __init__(self, database : Database):
        super().__init__()
        self.setRowCount(3)
        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(["Job Title", "Company", "requirments", "url", "status"])
        print("from database")
        data = database.get_applications()
        for index, item in enumerate(data):
            print(item)
            print(item[1])
            self.setItem(index,0, QTableWidgetItem(item[1]))
            self.setItem(index,1, QTableWidgetItem(item[2]))
            self.setItem(index,2, QTableWidgetItem(item[3]))
            self.setItem(index,3, QTableWidgetItem(item[4]))
            self.setItem(index,4, QTableWidgetItem(item[5]))

        # self.setItem(1,0, QTableWidgetItem("cooler job"))
        # self.setItem(1,1, QTableWidgetItem("cooler company"))
        # self.setItem(1,2, QTableWidgetItem("applied"))
