# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ir_v11.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.displayFrame = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayFrame.sizePolicy().hasHeightForWidth())
        self.displayFrame.setSizePolicy(sizePolicy)
        self.displayFrame.setMinimumSize(QtCore.QSize(640, 480))
        self.displayFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.displayFrame.setObjectName("displayFrame")
        self.gridLayout.addWidget(self.displayFrame, 0, 0, 2, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pantiltcontroller = QtWidgets.QGroupBox(self.centralwidget)
        self.pantiltcontroller.setObjectName("pantiltcontroller")
        self.LEDSlider = QtWidgets.QSlider(self.pantiltcontroller)
        self.LEDSlider.setGeometry(QtCore.QRect(20, 50, 311, 21))
        self.LEDSlider.setMaximum(255)
        self.LEDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.LEDSlider.setObjectName("LEDSlider")
        self.upButton = QtWidgets.QPushButton(self.pantiltcontroller)
        self.upButton.setGeometry(QtCore.QRect(130, 74, 89, 31))
        self.upButton.setCheckable(False)
        self.upButton.setAutoRepeat(True)
        self.upButton.setAutoRepeatDelay(25)
        self.upButton.setAutoRepeatInterval(25)
        self.upButton.setObjectName("upButton")
        self.downButton = QtWidgets.QPushButton(self.pantiltcontroller)
        self.downButton.setGeometry(QtCore.QRect(130, 134, 89, 31))
        self.downButton.setAutoRepeat(True)
        self.downButton.setAutoRepeatDelay(25)
        self.downButton.setAutoRepeatInterval(25)
        self.downButton.setObjectName("downButton")
        self.rightButton = QtWidgets.QPushButton(self.pantiltcontroller)
        self.rightButton.setGeometry(QtCore.QRect(220, 104, 89, 31))
        self.rightButton.setAutoRepeat(True)
        self.rightButton.setAutoRepeatDelay(25)
        self.rightButton.setAutoRepeatInterval(25)
        self.rightButton.setObjectName("rightButton")
        self.leftButton = QtWidgets.QPushButton(self.pantiltcontroller)
        self.leftButton.setGeometry(QtCore.QRect(40, 104, 89, 31))
        self.leftButton.setAutoRepeat(True)
        self.leftButton.setAutoRepeatDelay(25)
        self.leftButton.setAutoRepeatInterval(25)
        self.leftButton.setObjectName("leftButton")
        self.adjustbrightness = QtWidgets.QLabel(self.pantiltcontroller)
        self.adjustbrightness.setGeometry(QtCore.QRect(0, 26, 355, 21))
        self.adjustbrightness.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.adjustbrightness.setObjectName("adjustbrightness")
        self.servoerror = QtWidgets.QPushButton(self.pantiltcontroller)
        self.servoerror.setGeometry(QtCore.QRect(60, 180, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.servoerror.setPalette(palette)
        self.servoerror.setObjectName("servoerror")
        self.camerror = QtWidgets.QPushButton(self.pantiltcontroller)
        self.camerror.setGeometry(QtCore.QRect(60, 210, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.camerror.setPalette(palette)
        self.camerror.setObjectName("camerror")
        self.gridLayout_3.addWidget(self.pantiltcontroller, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 2, 1, 1)
        self.history = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history.sizePolicy().hasHeightForWidth())
        self.history.setSizePolicy(sizePolicy)
        self.history.setMaximumSize(QtCore.QSize(16777215, 87))
        self.history.setObjectName("history")
        self.gridLayout.addWidget(self.history, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelForLocation = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelForLocation.sizePolicy().hasHeightForWidth())
        self.labelForLocation.setSizePolicy(sizePolicy)
        self.labelForLocation.setMinimumSize(QtCore.QSize(0, 0))
        self.labelForLocation.setMaximumSize(QtCore.QSize(175, 16777215))
        self.labelForLocation.setObjectName("labelForLocation")
        self.horizontalLayout_7.addWidget(self.labelForLocation)
        self.filePathDisp = QtWidgets.QLabel(self.centralwidget)
        self.filePathDisp.setObjectName("filePathDisp")
        self.horizontalLayout_7.addWidget(self.filePathDisp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 17, 0, 1, 1)
        self.storageLabel = QtWidgets.QLabel(self.centralwidget)
        self.storageLabel.setObjectName("storageLabel")
        self.gridLayout_2.addWidget(self.storageLabel, 15, 0, 1, 1)
        self.minTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.minTempLabel.setObjectName("minTempLabel")
        self.gridLayout_2.addWidget(self.minTempLabel, 14, 0, 1, 1)
        self.vidBalance = QtWidgets.QLabel(self.centralwidget)
        self.vidBalance.setObjectName("vidBalance")
        self.gridLayout_2.addWidget(self.vidBalance, 3, 0, 1, 1)
        self.maxTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxTempLabel.setObjectName("maxTempLabel")
        self.gridLayout_2.addWidget(self.maxTempLabel, 13, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.displayC = QtWidgets.QPushButton(self.centralwidget)
        self.displayC.setObjectName("displayC")
        self.horizontalLayout_2.addWidget(self.displayC)
        self.displayF = QtWidgets.QPushButton(self.centralwidget)
        self.displayF.setObjectName("displayF")
        self.horizontalLayout_2.addWidget(self.displayF)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 10, 0, 1, 1)
        self.cursorTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.cursorTempLabel.setObjectName("cursorTempLabel")
        self.gridLayout_2.addWidget(self.cursorTempLabel, 12, 0, 1, 1)
        self.balancer = QtWidgets.QSlider(self.centralwidget)
        self.balancer.setMaximum(10)
        self.balancer.setSingleStep(1)
        self.balancer.setPageStep(1)
        self.balancer.setProperty("value", 5)
        self.balancer.setSliderPosition(5)
        self.balancer.setOrientation(QtCore.Qt.Horizontal)
        self.balancer.setObjectName("balancer")
        self.gridLayout_2.addWidget(self.balancer, 4, 0, 1, 1)
        self.filePathBut = QtWidgets.QPushButton(self.centralwidget)
        self.filePathBut.setObjectName("filePathBut")
        self.gridLayout_2.addWidget(self.filePathBut, 7, 0, 1, 1)
        self.runPost = QtWidgets.QPushButton(self.centralwidget)
        self.runPost.setObjectName("runPost")
        self.gridLayout_2.addWidget(self.runPost, 16, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startRec = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.startRec.setFont(font)
        self.startRec.setObjectName("startRec")
        self.verticalLayout_2.addWidget(self.startRec)
        self.stopRec = QtWidgets.QPushButton(self.centralwidget)
        self.stopRec.setObjectName("stopRec")
        self.verticalLayout_2.addWidget(self.stopRec)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.recLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.recLabel.setFont(font)
        self.recLabel.setObjectName("recLabel")
        self.horizontalLayout.addWidget(self.recLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 8, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)
        self.timeStatus = QtWidgets.QLabel(self.centralwidget)
        self.timeStatus.setObjectName("timeStatus")
        self.gridLayout_2.addWidget(self.timeStatus, 11, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.comboFFCmode = QtWidgets.QComboBox(self.centralwidget)
        self.comboFFCmode.setEnabled(True)
        self.comboFFCmode.setObjectName("comboFFCmode")
        self.comboFFCmode.addItem("")
        self.comboFFCmode.addItem("")
        self.comboFFCmode.addItem("")
        self.horizontalLayout_6.addWidget(self.comboFFCmode)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.startStreamBut = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.startStreamBut.setFont(font)
        self.startStreamBut.setObjectName("startStreamBut")
        self.horizontalLayout_5.addWidget(self.startStreamBut)
        self.ffcBut = QtWidgets.QPushButton(self.centralwidget)
        self.ffcBut.setEnabled(True)
        self.ffcBut.setObjectName("ffcBut")
        self.horizontalLayout_5.addWidget(self.ffcBut)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboGain = QtWidgets.QComboBox(self.centralwidget)
        self.comboGain.setEnabled(True)
        self.comboGain.setObjectName("comboGain")
        self.comboGain.addItem("")
        self.comboGain.addItem("")
        self.comboGain.addItem("")
        self.horizontalLayout_3.addWidget(self.comboGain)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.rotateBut = QtWidgets.QPushButton(self.centralwidget)
        self.rotateBut.setObjectName("rotateBut")
        self.gridLayout_2.addWidget(self.rotateBut, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Record IR"))
        self.displayFrame.setText(_translate("MainWindow", "Click \"Start IR Camera Feed\" once camera ready."))
        self.pantiltcontroller.setTitle(_translate("MainWindow", "Pan-tilt Servo Controller"))
        self.upButton.setText(_translate("MainWindow", "Up"))
        self.downButton.setText(_translate("MainWindow", "Down"))
        self.rightButton.setText(_translate("MainWindow", "Right"))
        self.leftButton.setText(_translate("MainWindow", "Left"))
        self.adjustbrightness.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Light Intensity</p></body></html>"))
        self.servoerror.setText(_translate("MainWindow", "My Pantil Servo does not work!"))
        self.camerror.setText(_translate("MainWindow", "My camera(s) does not work!"))
        self.labelForLocation.setText(_translate("MainWindow", "File Save Location:"))
        self.filePathDisp.setText(_translate("MainWindow", "Please Specify Using the Select File Path Button to the Right"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Notes/Comment Area"))
        self.label.setText(_translate("MainWindow", "Command Log:"))
        self.storageLabel.setText(_translate("MainWindow", "Storage"))
        self.minTempLabel.setText(_translate("MainWindow", "Min Temperature"))
        self.vidBalance.setText(_translate("MainWindow", "IR                               Video Balance                     Webcam"))
        self.maxTempLabel.setText(_translate("MainWindow", "Max Temperature"))
        self.displayC.setText(_translate("MainWindow", "Display Celsius"))
        self.displayF.setText(_translate("MainWindow", "Display Fahrenheit"))
        self.cursorTempLabel.setText(_translate("MainWindow", "Cursor Temp (On Mouse Click)"))
        self.filePathBut.setText(_translate("MainWindow", "Select File Path"))
        self.runPost.setText(_translate("MainWindow", "Run Post Processing Script"))
        self.startRec.setText(_translate("MainWindow", "Start Recording Data"))
        self.stopRec.setText(_translate("MainWindow", "Stop Recording/Save"))
        self.recLabel.setText(_translate("MainWindow", "Not Recording"))
        self.label_3.setText(_translate("MainWindow", "Begin Filename With:"))
        self.timeStatus.setText(_translate("MainWindow", "Time/Date"))
        self.label_4.setText(_translate("MainWindow", "Set FFC Mode:"))
        self.comboFFCmode.setItemText(0, _translate("MainWindow", "AUTO"))
        self.comboFFCmode.setItemText(1, _translate("MainWindow", "MANUAL"))
        self.comboFFCmode.setItemText(2, _translate("MainWindow", "EXTERNAL"))
        self.startStreamBut.setText(_translate("MainWindow", "Start IR Camera Feed"))
        self.ffcBut.setText(_translate("MainWindow", "Perform FFC"))
        self.label_2.setText(_translate("MainWindow", "Set Gain State:"))
        self.comboGain.setItemText(0, _translate("MainWindow", "HIGH"))
        self.comboGain.setItemText(1, _translate("MainWindow", "LOW"))
        self.comboGain.setItemText(2, _translate("MainWindow", "AUTO"))
        self.rotateBut.setText(_translate("MainWindow", "Rotate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

