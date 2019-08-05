# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camErrorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_camerrorwindow(object):
    def setupUi(self, camerrorwindow):
        camerrorwindow.setObjectName("camerrorwindow")
        camerrorwindow.resize(400, 139)
        self.okcancelBox = QtWidgets.QDialogButtonBox(camerrorwindow)
        self.okcancelBox.setGeometry(QtCore.QRect(10, 80, 381, 31))
        self.okcancelBox.setOrientation(QtCore.Qt.Horizontal)
        self.okcancelBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okcancelBox.setCenterButtons(True)
        self.okcancelBox.setObjectName("okcancelBox")
        self.checkcamText = QtWidgets.QLabel(camerrorwindow)
        self.checkcamText.setGeometry(QtCore.QRect(20, 30, 371, 31))
        self.checkcamText.setObjectName("checkcamText")

        self.retranslateUi(camerrorwindow)
        self.okcancelBox.accepted.connect(camerrorwindow.accept)
        self.okcancelBox.rejected.connect(camerrorwindow.reject)
        QtCore.QMetaObject.connectSlotsByName(camerrorwindow)

    def retranslateUi(self, camerrorwindow):
        _translate = QtCore.QCoreApplication.translate
        camerrorwindow.setWindowTitle(_translate("camerrorwindow", "Camera Error"))
        self.checkcamText.setText(_translate("camerrorwindow", "Please check if your cameras are properly connected."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    camerrorwindow = QtWidgets.QDialog()
    ui = Ui_camerrorwindow()
    ui.setupUi(camerrorwindow)
    camerrorwindow.show()
    sys.exit(app.exec_())

