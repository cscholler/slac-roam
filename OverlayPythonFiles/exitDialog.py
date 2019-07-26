# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 182)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(150, 130, 151, 31))
        self.exitButton.setObjectName("exitButton")
        self.warningText = QtWidgets.QLabel(Dialog)
        self.warningText.setGeometry(QtCore.QRect(10, 10, 431, 111))
        self.warningText.setObjectName("warningText")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def exitProgram(self):
        os.excel(sys.executable, os.path.abspath(__file__), *sys.argv) # When restart button is pressed program will close and restart


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.exitButton.setText(_translate("Dialog", "Restart"))
        self.warningText.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#cc0000;\">Warning</span>: The camera(s) is disconnected!</p><p align=\"center\">The program will exit now.</p><p align=\"center\">Please restart the program to avoid errors and crashing.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

