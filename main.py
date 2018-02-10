# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowLoader.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setObjectName("path")
        self.horizontalLayout.addWidget(self.path)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setObjectName("load")
        self.load.clicked.connect(self.getpath)
        self.horizontalLayout.addWidget(self.load)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setObjectName("loading")
        self.gridLayout.addWidget(self.loading, 2, 0, 1, 1)
        self.loading.hide()
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setObjectName("table")
        self.gridLayout.addWidget(self.table, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSV Loader"))
        self.label.setText(_translate("MainWindow", "Enter the file path to be loaded"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.loading.setText(_translate("MainWindow", "Loading..."))

    def getpath(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(caption='Open File', directory='C:\\',
                                                         filter="CSV Files(*.csv)")
        self.path.setText(filepath[0])
        self.load.setDisabled(True)
        self.loading.show()
        self.dataframe(filepath[0])

    def dataframe(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df)
        self.table.setModel(model)
        self.loading.setText("Done...")
        self.load.setDisabled(False)


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

