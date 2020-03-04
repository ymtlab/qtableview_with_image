# -*- coding: utf-8 -*-
import sys
from mainwindow import Ui_MainWindow
from model import Model, Delegate
from item import Item
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = Model(self, Item())
        self.model.insertColumns(0, ['File name','Image'])
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setItemDelegate(Delegate())

        for filename in ['green.png', 'blue.png', 'yellow.png']:
            self.model.insertRows(self.model.rowCount(), 1)
            item = self.model.root_item.children()[-1]
            pixmap = QtGui.QPixmap(filename)
            item.set_data('Image', pixmap)
            item.set_data('File name', filename)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
 
if __name__ == '__main__':
    main()