# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loader.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.path = QtWidgets.QLineEdit(Dialog)
        self.path.setGeometry(QtCore.QRect(40, 60, 341, 21))
        self.path.setObjectName("path")
        self.load = QtWidgets.QPushButton(Dialog)
        self.load.setGeometry(QtCore.QRect(410, 60, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.load.setFont(font)
        self.load.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.load.setObjectName("load")
        self.load.clicked.connect(self.getpath)
        self.loadingText = QtWidgets.QLabel(Dialog)
        self.loadingText.setGeometry(QtCore.QRect(50, 80, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        self.loadingText.setFont(font)
        self.loadingText.setObjectName("loadingText")
        self.loadingText.hide()
        self.table = QtWidgets.QTableView(Dialog)
        self.table.setGeometry(QtCore.QRect(35, 131, 421, 231))
        self.table.setObjectName("table")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CSV File Loader"))
        self.label.setText(_translate("Dialog", "Enter the path of file to be loaded"))
        self.load.setText(_translate("Dialog", "Load"))
        self.loadingText.setText(_translate("Dialog", "Loading..."))

    def getpath(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(caption='Open File', directory='C:\\',
                                                         filter="CSV Files(*.csv)")
        self.path.setText(filepath[0])
        self.load.setDisabled(True)
        self.loadingText.show()
        self.dataframe(filepath[0])

    def dataframe(self, file):
        df = pd.read_csv(file)
        model = PandasModel(df)
        self.table.setModel(model)
        self.loadingText.setText("Done...")
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
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

