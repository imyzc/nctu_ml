# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'for_testUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 304)
        self.label_theta = QtWidgets.QLabel(Form)
        self.label_theta.setGeometry(QtCore.QRect(20, 50, 111, 31))
        self.label_theta.setObjectName("label_theta")
        self.label_v = QtWidgets.QLabel(Form)
        self.label_v.setGeometry(QtCore.QRect(20, 4, 111, 31))
        self.label_v.setObjectName("label_v")
        self.lineEdit_v = QtWidgets.QLineEdit(Form)
        self.lineEdit_v.setGeometry(QtCore.QRect(140, 10, 41, 31))
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.lineEdit_theta = QtWidgets.QLineEdit(Form)
        self.lineEdit_theta.setGeometry(QtCore.QRect(140, 51, 41, 31))
        self.lineEdit_theta.setObjectName("lineEdit_theta")
        self.pushButton_predict = QtWidgets.QPushButton(Form)
        self.pushButton_predict.setGeometry(QtCore.QRect(280, 30, 101, 51))
        self.pushButton_predict.setObjectName("pushButton_predict")
        self.label_h_predict = QtWidgets.QLabel(Form)
        self.label_h_predict.setGeometry(QtCore.QRect(240, 164, 91, 31))
        self.label_h_predict.setObjectName("label_h_predict")
        self.label_r_predict = QtWidgets.QLabel(Form)
        self.label_r_predict.setGeometry(QtCore.QRect(240, 210, 91, 31))
        self.label_r_predict.setObjectName("label_r_predict")
        self.label_r_real = QtWidgets.QLabel(Form)
        self.label_r_real.setGeometry(QtCore.QRect(20, 206, 91, 31))
        self.label_r_real.setObjectName("label_r_real")
        self.label_h_real = QtWidgets.QLabel(Form)
        self.label_h_real.setGeometry(QtCore.QRect(20, 160, 91, 31))
        self.label_h_real.setObjectName("label_h_real")
        self.label_true_value = QtWidgets.QLabel(Form)
        self.label_true_value.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.label_true_value.setObjectName("label_true_value")
        self.label_predict_value = QtWidgets.QLabel(Form)
        self.label_predict_value.setGeometry(QtCore.QRect(240, 120, 141, 21))
        self.label_predict_value.setObjectName("label_predict_value")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_theta.setText(_translate("Form", "theta"))
        self.label_v.setText(_translate("Form", "v"))
        self.pushButton_predict.setText(_translate("Form", "predict"))
        self.label_h_predict.setText(_translate("Form", "h"))
        self.label_r_predict.setText(_translate("Form", "r"))
        self.label_r_real.setText(_translate("Form", "r"))
        self.label_h_real.setText(_translate("Form", "h"))
        self.label_true_value.setText(_translate("Form", "True Value"))
        self.label_predict_value.setText(_translate("Form", "Predict Value"))
