# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servoErrorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_servoErrorWindow(object):
    def setupUi(self, servoErrorWindow):
        servoErrorWindow.setObjectName("servoErrorWindow")
        servoErrorWindow.resize(400, 138)
        self.okcancelBox = QtWidgets.QDialogButtonBox(servoErrorWindow)
        self.okcancelBox.setGeometry(QtCore.QRect(100, 60, 181, 71))
        self.okcancelBox.setOrientation(QtCore.Qt.Horizontal)
        self.okcancelBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okcancelBox.setCenterButtons(True)
        self.okcancelBox.setObjectName("okcancelBox")
        self.checkservoText = QtWidgets.QLabel(servoErrorWindow)
        self.checkservoText.setGeometry(QtCore.QRect(30, 30, 371, 31))
        self.checkservoText.setObjectName("checkservoText")

        self.retranslateUi(servoErrorWindow)
        self.okcancelBox.accepted.connect(servoErrorWindow.accept)
        self.okcancelBox.rejected.connect(servoErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(servoErrorWindow)

    def retranslateUi(self, servoErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        servoErrorWindow.setWindowTitle(_translate("servoErrorWindow", "Servo Error"))
        self.checkservoText.setText(_translate("servoErrorWindow", "Please check if your servos are properly connected."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    servoErrorWindow = QtWidgets.QDialog()
    ui = Ui_servoErrorWindow()
    ui.setupUi(servoErrorWindow)
    servoErrorWindow.show()
    sys.exit(app.exec_())

