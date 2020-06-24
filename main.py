# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import myRedis


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(260, 150, 160, 88))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.ipLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ipLabel.setObjectName("ipLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ipLabel)
        self.ipLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ipLineEdit)
        self.portLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.portLabel.setObjectName("portLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.portLabel)
        self.portLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.portLineEdit.setObjectName("portLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.portLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.main_button_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ipLabel.setText(_translate("MainWindow", "ip"))
        self.portLabel.setText(_translate("MainWindow", "port"))
        self.pushButton.setText(_translate("MainWindow", "测试"))
        self.menu.setTitle(_translate("MainWindow", "新建连接"))

    def main_button_click(self):
        redis = myRedis.myRedis()
        ip = self.ipLineEdit.text()
        port = self.portLineEdit.text()
        r = redis.testConnect(ip, port)
        QtWidgets.QMessageBox.information(self.pushButton, '标题', r)