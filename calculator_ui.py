# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 357)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 110, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 110, 51, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 110, 51, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 160, 51, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 160, 51, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 160, 51, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 160, 51, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 210, 51, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 210, 51, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 210, 51, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(220, 210, 51, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 260, 51, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 260, 51, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 260, 51, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(220, 260, 51, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 310, 51, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(80, 310, 51, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(150, 310, 121, 31))
        self.pushButton_20.setObjectName("pushButton_20")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CALCULATOR.."))
        self.pushButton.setText(_translate("Dialog", "C"))
        self.pushButton_2.setText(_translate("Dialog", "%"))
        self.pushButton_3.setText(_translate("Dialog", "Clear"))
        self.pushButton_4.setText(_translate("Dialog", "/"))
        self.pushButton_5.setText(_translate("Dialog", "7"))
        self.pushButton_6.setText(_translate("Dialog", "8"))
        self.pushButton_7.setText(_translate("Dialog", "9"))
        self.pushButton_8.setText(_translate("Dialog", "*"))
        self.pushButton_9.setText(_translate("Dialog", "4"))
        self.pushButton_10.setText(_translate("Dialog", "5"))
        self.pushButton_11.setText(_translate("Dialog", "6"))
        self.pushButton_12.setText(_translate("Dialog", "-"))
        self.pushButton_13.setText(_translate("Dialog", "1"))
        self.pushButton_14.setText(_translate("Dialog", "2"))
        self.pushButton_15.setText(_translate("Dialog", "3"))
        self.pushButton_16.setText(_translate("Dialog", "+"))
        self.pushButton_17.setText(_translate("Dialog", "0"))
        self.pushButton_18.setText(_translate("Dialog", "."))
        self.pushButton_20.setText(_translate("Dialog", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

