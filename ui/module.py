# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.summary = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.summary.setObjectName("summary")
        self.gridLayout.addWidget(self.summary, 5, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.category_id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.category_id.setEnabled(True)
        self.category_id.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.category_id.setObjectName("category_id")
        self.gridLayout.addWidget(self.category_id, 3, 1, 1, 1)
        self.license = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.license.setObjectName("license")
        self.gridLayout.addWidget(self.license, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.sequence = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sequence.setObjectName("sequence")
        self.gridLayout.addWidget(self.sequence, 6, 1, 1, 1)
        self.author = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.author.setEnabled(True)
        self.author.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.version = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.version.setEnabled(True)
        self.version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version.setObjectName("version")
        self.gridLayout.addWidget(self.version, 2, 1, 1, 1)
        self.description = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 7, 1, 1, 1)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(610, 10, 163, 120))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.application = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.application.setObjectName("application")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.application)
        self.installable = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.installable.setObjectName("installable")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.installable)
        self.auto_install = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.auto_install.setObjectName("auto_install")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.auto_install)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 390, 711, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(730, 390, 91, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_model = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_model.setObjectName("add_model")
        self.verticalLayout.addWidget(self.add_model)
        self.delete_model = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_model.setObjectName("delete_model")
        self.verticalLayout.addWidget(self.delete_model)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(1040, 10, 79, 23))
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 23))
        self.menubar.setObjectName("menubar")
        self.menuModule = QtWidgets.QMenu(self.menubar)
        self.menuModule.setObjectName("menuModule")
        self.menuModel = QtWidgets.QMenu(self.menubar)
        self.menuModel.setObjectName("menuModel")
        self.menuOpEN = QtWidgets.QMenu(self.menubar)
        self.menuOpEN.setObjectName("menuOpEN")
        self.menufield = QtWidgets.QMenu(self.menubar)
        self.menufield.setObjectName("menufield")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnection = QtWidgets.QAction(MainWindow)
        self.actionConnection.setObjectName("actionConnection")
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionSelect = QtWidgets.QAction(MainWindow)
        self.actionSelect.setObjectName("actionSelect")
        self.menuOpEN.addAction(self.actionConnection)
        self.menubar.addAction(self.menuOpEN.menuAction())
        self.menubar.addAction(self.menuModule.menuAction())
        self.menubar.addAction(self.menuModel.menuAction())
        self.menubar.addAction(self.menufield.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.name, self.author)
        MainWindow.setTabOrder(self.author, self.version)
        MainWindow.setTabOrder(self.version, self.category_id)
        MainWindow.setTabOrder(self.category_id, self.license)
        MainWindow.setTabOrder(self.license, self.summary)
        MainWindow.setTabOrder(self.summary, self.sequence)
        MainWindow.setTabOrder(self.sequence, self.application)
        MainWindow.setTabOrder(self.application, self.installable)
        MainWindow.setTabOrder(self.installable, self.auto_install)
        MainWindow.setTabOrder(self.auto_install, self.add_model)
        MainWindow.setTabOrder(self.add_model, self.delete_model)
        MainWindow.setTabOrder(self.delete_model, self.tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "summary"))
        self.label_6.setText(_translate("MainWindow", "sequence"))
        self.label_5.setText(_translate("MainWindow", "description"))
        self.label_3.setText(_translate("MainWindow", "license"))
        self.label.setText(_translate("MainWindow", "module_name"))
        self.label_2.setText(_translate("MainWindow", "category_id"))
        self.label_7.setText(_translate("MainWindow", "author"))
        self.label_8.setText(_translate("MainWindow", "version"))
        self.application.setText(_translate("MainWindow", "application"))
        self.installable.setText(_translate("MainWindow", "installable"))
        self.auto_install.setText(_translate("MainWindow", "auto_install"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "table_name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "rec_name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "auto"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "inherit"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "order"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "order"))
        self.add_model.setText(_translate("MainWindow", "add model"))
        self.delete_model.setText(_translate("MainWindow", "delete model"))
        self.save.setText(_translate("MainWindow", "save"))
        self.menuModule.setTitle(_translate("MainWindow", "Module"))
        self.menuModel.setTitle(_translate("MainWindow", "Model"))
        self.menuOpEN.setTitle(_translate("MainWindow", "Edit"))
        self.menufield.setTitle(_translate("MainWindow", "Field"))
        self.actionConnection.setText(_translate("MainWindow", "Connection"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionSelect.setText(_translate("MainWindow", "Select"))
