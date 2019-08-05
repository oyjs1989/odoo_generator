# -*- coding: utf-8 -*-
#   File Name：     odoo_generator
#   Author :        lumi
#   date：          2019/7/19
#   Description :

# - import generator package

# - Third party module of python
from PyQt5 import QtGui, QtWidgets
# - Custom package
import sys
from app.application import MainWindow



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
