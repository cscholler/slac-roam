# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ir_post_v2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1153, 762)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectFileBut = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileBut.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.selectFileBut.setFont(font)
        self.selectFileBut.setObjectName("selectFileBut")
        self.verticalLayout.addWidget(self.selectFileBut)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmIronBut = QtWidgets.QPushButton(self.centralwidget)
        self.cmIronBut.setObjectName("cmIronBut")
        self.horizontalLayout_4.addWidget(self.cmIronBut)
        self.cmGrayBut = QtWidgets.QPushButton(self.centralwidget)
        self.cmGrayBut.setObjectName("cmGrayBut")
        self.horizontalLayout_4.addWidget(self.cmGrayBut)
        self.cmRainBut = QtWidgets.QPushButton(self.centralwidget)
        self.cmRainBut.setObjectName("cmRainBut")
        self.horizontalLayout_4.addWidget(self.cmRainBut)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.playVidBut = QtWidgets.QPushButton(self.centralwidget)
        self.playVidBut.setEnabled(False)
        self.playVidBut.setObjectName("playVidBut")
        self.verticalLayout.addWidget(self.playVidBut)
        self.pauseVidBut = QtWidgets.QPushButton(self.centralwidget)
        self.pauseVidBut.setEnabled(False)
        self.pauseVidBut.setObjectName("pauseVidBut")
        self.verticalLayout.addWidget(self.pauseVidBut)
        self.nextFrame = QtWidgets.QPushButton(self.centralwidget)
        self.nextFrame.setEnabled(False)
        self.nextFrame.setObjectName("nextFrame")
        self.verticalLayout.addWidget(self.nextFrame)
        self.prevFrame = QtWidgets.QPushButton(self.centralwidget)
        self.prevFrame.setEnabled(False)
        self.prevFrame.setObjectName("prevFrame")
        self.verticalLayout.addWidget(self.prevFrame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.startEdit.setEnabled(False)
        self.startEdit.setText("")
        self.startEdit.setObjectName("startEdit")
        self.horizontalLayout.addWidget(self.startEdit)
        self.stopEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stopEdit.setEnabled(False)
        self.stopEdit.setText("")
        self.stopEdit.setObjectName("stopEdit")
        self.horizontalLayout.addWidget(self.stopEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.saveAsVideoSS = QtWidgets.QPushButton(self.centralwidget)
        self.saveAsVideoSS.setEnabled(False)
        self.saveAsVideoSS.setObjectName("saveAsVideoSS")
        self.verticalLayout.addWidget(self.saveAsVideoSS)
        self.tempScaleBut = QtWidgets.QPushButton(self.centralwidget)
        self.tempScaleBut.setEnabled(False)
        self.tempScaleBut.setObjectName("tempScaleBut")
        self.verticalLayout.addWidget(self.tempScaleBut)
        self.saveCvImageBut = QtWidgets.QPushButton(self.centralwidget)
        self.saveCvImageBut.setEnabled(False)
        self.saveCvImageBut.setObjectName("saveCvImageBut")
        self.verticalLayout.addWidget(self.saveCvImageBut)
        self.makeTiffBut = QtWidgets.QPushButton(self.centralwidget)
        self.makeTiffBut.setEnabled(False)
        self.makeTiffBut.setObjectName("makeTiffBut")
        self.verticalLayout.addWidget(self.makeTiffBut)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.displayC = QtWidgets.QPushButton(self.centralwidget)
        self.displayC.setEnabled(False)
        self.displayC.setObjectName("displayC")
        self.horizontalLayout_7.addWidget(self.displayC)
        self.displayF = QtWidgets.QPushButton(self.centralwidget)
        self.displayF.setEnabled(False)
        self.displayF.setObjectName("displayF")
        self.horizontalLayout_7.addWidget(self.displayF)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.cursorTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.cursorTempLabel.setObjectName("cursorTempLabel")
        self.verticalLayout.addWidget(self.cursorTempLabel)
        self.maxTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxTempLabel.setObjectName("maxTempLabel")
        self.verticalLayout.addWidget(self.maxTempLabel)
        self.maxTempLocLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxTempLocLabel.setObjectName("maxTempLocLabel")
        self.verticalLayout.addWidget(self.maxTempLocLabel)
        self.minTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.minTempLabel.setObjectName("minTempLabel")
        self.verticalLayout.addWidget(self.minTempLabel)
        self.minTempLocLabel = QtWidgets.QLabel(self.centralwidget)
        self.minTempLocLabel.setObjectName("minTempLocLabel")
        self.verticalLayout.addWidget(self.minTempLocLabel)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.currentFrameDisp = QtWidgets.QLabel(self.centralwidget)
        self.currentFrameDisp.setObjectName("currentFrameDisp")
        self.verticalLayout.addWidget(self.currentFrameDisp)
        self.currentTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.verticalLayout.addWidget(self.currentTimeLabel)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 17))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)
        self.dispSelectedFile = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispSelectedFile.sizePolicy().hasHeightForWidth())
        self.dispSelectedFile.setSizePolicy(sizePolicy)
        self.dispSelectedFile.setMinimumSize(QtCore.QSize(601, 17))
        self.dispSelectedFile.setMaximumSize(QtCore.QSize(16777215, 17))
        self.dispSelectedFile.setObjectName("dispSelectedFile")
        self.gridLayout.addWidget(self.dispSelectedFile, 0, 2, 1, 1)
        self.dispLayout = QtWidgets.QVBoxLayout()
        self.dispLayout.setObjectName("dispLayout")
        self.gridLayout.addLayout(self.dispLayout, 1, 1, 2, 2)
        self.history = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.history.setObjectName("history")
        self.gridLayout.addWidget(self.history, 2, 0, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sl = QtWidgets.QSlider(self.centralwidget)
        self.sl.setEnabled(False)
        self.sl.setMinimumSize(QtCore.QSize(739, 0))
        self.sl.setOrientation(QtCore.Qt.Horizontal)
        self.sl.setObjectName("sl")
        self.verticalLayout_3.addWidget(self.sl)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.slStartF = QtWidgets.QLabel(self.centralwidget)
        self.slStartF.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.slStartF.setObjectName("slStartF")
        self.horizontalLayout_5.addWidget(self.slStartF)
        self.slMidF = QtWidgets.QLabel(self.centralwidget)
        self.slMidF.setAlignment(QtCore.Qt.AlignCenter)
        self.slMidF.setObjectName("slMidF")
        self.horizontalLayout_5.addWidget(self.slMidF)
        self.slEndF = QtWidgets.QLabel(self.centralwidget)
        self.slEndF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slEndF.setObjectName("slEndF")
        self.horizontalLayout_5.addWidget(self.slEndF)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.slStartT = QtWidgets.QLabel(self.centralwidget)
        self.slStartT.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.slStartT.setObjectName("slStartT")
        self.horizontalLayout_3.addWidget(self.slStartT)
        self.slMidT = QtWidgets.QLabel(self.centralwidget)
        self.slMidT.setAlignment(QtCore.Qt.AlignCenter)
        self.slMidT.setObjectName("slMidT")
        self.horizontalLayout_3.addWidget(self.slMidT)
        self.slEndT = QtWidgets.QLabel(self.centralwidget)
        self.slEndT.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slEndT.setObjectName("slEndT")
        self.horizontalLayout_3.addWidget(self.slEndT)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 1, 1, 2)
        # Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Post Process IR"))
        self.selectFileBut.setText(_translate("Form", "Select HDF5 File"))
        self.cmIronBut.setText(_translate("Form", "Ironblack"))
        self.cmGrayBut.setText(_translate("Form", "Grayscale"))
        self.cmRainBut.setText(_translate("Form", "Rainbow"))
        self.playVidBut.setText(_translate("Form", "Play Video"))
        self.pauseVidBut.setText(_translate("Form", "Pause Video"))
        self.nextFrame.setText(_translate("Form", "Next Frame"))
        self.prevFrame.setText(_translate("Form", "Previous Frame"))
        self.label_10.setText(_translate("Form", "Start Frame:"))
        self.label_11.setText(_translate("Form", "Stop Frame:"))
        self.saveAsVideoSS.setText(_translate("Form", "Save AVI Video from Start to Stop Frame"))
        self.tempScaleBut.setText(_translate("Form", "Generate Figure with Temp Scale"))
        self.saveCvImageBut.setText(_translate("Form", "Save PNG Image (Without Axes)"))
        self.makeTiffBut.setText(_translate("Form", "Generate Tiff File (Full Duration)"))
        self.displayC.setText(_translate("Form", "Display Celsius"))
        self.displayF.setText(_translate("Form", "Display Fahrenheit"))
        self.cursorTempLabel.setText(_translate("Form", "Cursor Temp:"))
        self.maxTempLabel.setText(_translate("Form", "Current Max Temp:"))
        self.maxTempLocLabel.setText(_translate("Form", "Max Temp Loc:"))
        self.minTempLabel.setText(_translate("Form", "Current Min Temp: "))
        self.minTempLocLabel.setText(_translate("Form", "Min Temp Loc:"))
        self.currentFrameDisp.setText(_translate("Form", "Current Frame:"))
        self.currentTimeLabel.setText(_translate("Form", "Current Time:"))
        self.label.setText(_translate("Form", "Command Log:"))
        self.label_14.setText(_translate("Form", "File Selected: "))
        self.dispSelectedFile.setText(_translate("Form", "Use Select File Button"))
        self.slStartF.setText(_translate("Form", "Please Select File"))
        self.slMidF.setText(_translate("Form", "Please Select File"))
        self.slEndF.setText(_translate("Form", "Please Select File"))
        self.slStartT.setText(_translate("Form", "Please Select File"))
        self.slMidT.setText(_translate("Form", "Please Select File"))
        self.slEndT.setText(_translate("Form", "Please Select File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

