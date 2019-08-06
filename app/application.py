# -*- coding: utf-8 -*-
#   File Name：     application
#   Author :        lumi
#   date：          2019/7/25
#   Description :

# - import UI
from ui.module import Ui_MainWindow
from ui.fields import Ui_field
from ui.model import Ui_model
import types
# - import structure


# - Third party module of python
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot,QCoreApplication
from structure.py_structure import gModuls, gModels, gFields, Cache, _REQUIRED_TABLES

# - Custom package

class CommonWidget(object):

    table = ''
    superior = None
    cache = None
    subordinate = []

    def get_attr(self):
        return {k: getattr(self, k, None) for k in dir(self) if not k.startswith('__')}

    def qlineedit_text(self):
        return self.get_widget_fun(QtWidgets.QLineEdit, 'text')

    def qplaintextedit_text(self):
        return self.get_widget_fun(QtWidgets.QPlainTextEdit, 'toPlainText')

    def qcheckbox_text(self):
        return self.get_widget_fun(QtWidgets.QCheckBox, 'checkState')

    def get_widget_fun(self, wiget, func):
        return {k: getattr(getattr(self, k), func)() for k in dir(self) if isinstance(getattr(self, k, None), wiget)}

    def combobox(self):
        return self.get_widget_fun(QtWidgets.QComboBox, 'currentText')

    def attr_text(self):
        print(self.table)
        data = {'table': self.table}
        re_ql = self.qlineedit_text()
        re_qplt = self.qplaintextedit_text()
        re_qc = self.qcheckbox_text()
        re_cbb = self.combobox()
        data.update(re_ql)
        data.update(re_qplt)
        data.update(re_qc)
        data.update(re_cbb)
        return data

    def set_attr(self, obj):
        for k, v in self.attr_text().items():
            setattr(obj, k, v)

    def reflush_tablewidget(self, data, tablewidget):
        tablewidget.setRowCount(len(data))
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                tablewidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))

    def insert_tablewidget(self, data, tablewidget):
        row = tablewidget.rowCount()
        tablewidget.insertRow(row)
        for column, item in enumerate(data):
            tablewidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))

    def set_tablewidget_headeritem(self, fields, tablewiget):
        _translate = QCoreApplication.translate
        tablewiget.setColumnCount(len(fields))
        tablewiget.setRowCount(0)
        for column, itemname in enumerate(fields):
            item = QtWidgets.QTableWidgetItem()
            tablewiget.setHorizontalHeaderItem(column, item)
            item = tablewiget.horizontalHeaderItem(column)
            item.setText(_translate("model", itemname))

    def generate_code(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        g = self.cache.generate(directory)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, CommonWidget):
    table = 'modules'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.superior = None
        self.cache = None
        self.save.clicked.connect(self.save_cache)
        self.add_model.clicked.connect(self.create_model)
        self.generate.clicked.connect(self.create_model)

    def retranslateUi(self, Window):
        super(MainWindow, self).retranslateUi(Window)
        self.set_tablewidget_headeritem(_REQUIRED_TABLES['models'], self.tableWidget)

    def create_model(self):
        # if self.module.name == None:
        #     QtWidgets.QMessageBox.information(None, u"警告", "Module Name is Null")
        #     return
        self.m = ModelWindow(self)
        self.m.show()

    def save_cache(self):
        self.cache = Cache(**self.attr_text())
        self.cache.persistence()

    def generate_code(self):
        pass


class ModelWindow(QtWidgets.QMainWindow, Ui_model, CommonWidget):
    table = 'models'

    def __init__(self, module):
        super(ModelWindow, self).__init__()
        self.setupUi(self)
        self.add_field.clicked.connect(self.create_field)
        self.superior = module
        self.cache = None
        self.save.clicked.connect(self.save_cache)
        self.generate.clicked.connect(self.generate_code)

    def retranslateUi(self, MainWindow):
        super(ModelWindow, self).retranslateUi(MainWindow)
        self.set_tablewidget_headeritem(_REQUIRED_TABLES['fields'], self.tableWidget)

    def create_field(self):
        self.f = FieldQDialog(self)
        self.f.show()

    def save_cache(self):
        self.cache = Cache(**self.attr_text())
        self.cache.persistence()


class FieldQDialog(QtWidgets.QDialog, Ui_field, CommonWidget):

    table = 'fields'

    def __init__(self, model):
        super(FieldQDialog, self).__init__()
        self.setupUi(self)
        self.ttype.currentTextChanged.connect(self.onchange)
        self._args = {}
        self.superior = model
        self.cache = None

    # def qcheckbox_text(self):
    #     return {k: True if getattr(getattr(self, k), 'checkState')() else False for k in dir(self) if isinstance(getattr(self, k, None), QtWidgets.QCheckBox)}


    def field_set_default(self):
        pass

    def field_set_editable(self):
        pass

    def _reset(self):
        self.comodel_name.setText('')
        self.inverse.setText('')
        self.relation_table.setText('')
        self.column1.setText('')
        self.column2.setText('')
        self.domain.setText('')
        self.comodel_name.setEnabled(False)
        self.inverse.setEnabled(False)
        self.relation_table.setEnabled(False)
        self.column1.setEnabled(False)
        self.column2.setEnabled(False)
        self.domain.setEnabled(False)

    def _many2one(self):
        self.comodel_name.setEnabled(True)
        self.domain.setEnabled(True)

    def _one2many(self):
        self.comodel_name.setEnabled(True)
        self.inverse.setEnabled(True)
        self.domain.setEnabled(True)

    def _many2many(self):
        self.comodel_name.setEnabled(True)
        self.relation_table.setEnabled(True)
        self.column1.setEnabled(True)
        self.column2.setEnabled(True)
        self.domain.setEnabled(True)

    def onchange(self):
        self._reset()
        if self.ttype.currentText() == 'many2one':
            self._many2one()
        elif self.ttype.currentText() == 'one2many':
            self._one2many()
        elif self.ttype.currentText() == 'many2many':
            self._many2many()

    def _compute(self):
        # compute 字段触发
        pass

    def _related(self):
        # related 字段触发
        pass

    def _related(self):
        # related 字段触发
        pass

    def _get_args(self):
        '''
        'name', 'string', 'model_name', 'module', 'help', 'comodel_name', 'related', 'groups',
               'inverse', 'compute', 'is_copy', 'is_index', 'is_required', 'is_readonly', 'is_store'
        :return:
        '''
        self._args = {
            'table': 'fields',
            'model_name': self.model.model.name,
            'name': self.name.text(),
            'ttype': self.ttype.currentText(),
            'compute': self.compute.text(),
            'string': self.description.text(),
            'domain': self.domain.text(),
            'default': self.default_2.text(),
            'inverse': self.inverse.text(),
            'relation_table': self.relation_table.text(),
            'column1': self.column1.text(),
            'column2': self.column2.text(),
            'comodel_name': self.comodel_name.text(),
            'related': self.related.text()
        }

    @pyqtSlot()
    def accept(self):
        model_name = self.superior.attr_text().get('name')
        kwargs = self.attr_text()
        kwargs.update({model_name: model_name})
        self.cache = Cache(**kwargs)
        self.cache.persistence()
        self.superior.subordinate.append(self)
        data = self.cache.get_attrs_list()
        self.superior.insert_tablewidget(data, self.superior.tableWidget)
        self.hide()
