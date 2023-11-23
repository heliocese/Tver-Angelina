import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.initUI()

    def initUI(self):
        result = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(len(result[i])):
                if j == 2:
                    item = QTableWidgetItem(self.cur.execute(f"""SELECT roasting 
                    FROM roasting WHERE id={result[i][2]}""").fetchall()[0][0])
                    self.tableWidget.setItem(i, j, item)
                elif j == 3:
                    print(result[j][2])
                    item = QTableWidgetItem(self.cur.execute(f"""SELECT type 
                    FROM type WHERE id={result[i][3]}""").fetchall()[0][0])
                    self.tableWidget.setItem(i, j, item)
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())