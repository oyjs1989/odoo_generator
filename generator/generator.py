# -*- coding: utf-8 -*-
#   File Name：     generator
#   Author :        lumi
#   date：          2019/7/25
#   Description :

# - Third party module of python
from jinja2 import Environment, Template, PackageLoader

# - Custom package
import os
from datetime import datetime

if __name__ == '__main__':
    PACKAGE = 'templates'
else:
    PACKAGE = 'generator.templates'

ENV = Environment(loader=PackageLoader(PACKAGE))
PATH = os.getcwd()


class PyGenerator(object):
    '''
    将json转化成code代码
    '''

    py_file = {}
    models = {}

    def __init__(self, models, file_path='%s/py_code_%s.py' % (PATH, datetime.now().strftime('%y_%m_%d_%H_%M_%S'))):
        self.file_path = file_path
        self.models = models

    def py_header_render(self, file_name: str, date_time: str):
        tmp = ENV.get_template('header.py.j2')
        py_code = tmp.render(file_name=file_name, date_time=date_time)
        return py_code

    def fields_render(self, fields: list):
        tmp = ENV.get_template('field.py.j2')
        py_code = tmp.render(fields=fields)
        return py_code

    def model_render(self, model: dict):
        tmp = ENV.get_template('model.py.j2')
        py_code = tmp.render(model=model)
        return py_code

    def function_render(self, funcs: str):
        tmp = ENV.get_template('function.py.j2')
        py_code = tmp.render(funcs=funcs)
        return py_code

    def create_py_file(self):
        '''
        文件名 文件位置
        :return:
        '''
        DIR_PATH = os.path.dirname(self.file_path)
        if not os.path.isdir(DIR_PATH) and not os.path.exists(DIR_PATH):
            os.makedirs(DIR_PATH)
        return open(self.file_path, 'w')

    def class_render(self, model: dict):
        model_code = self.model_render(model)
        field_code = self.fields_render(model.get('fields'))
        function_code = self.function_render(model.get('functions'))
        return model_code + field_code + function_code

    def py_generator(self):
        '''
        拆解 modules 数据
        :return:
        '''
        # 生成modules 文件夹
        # 生成models secuity views wizard static report i18n  __init__.py  __mainfest__.py
        f = self.create_py_file()
        codes = ''
        print(self.models)
        for model in self.models:
            print(model)
            codes += self.class_render(model)
        f.write(codes)


def manifest_render(module):
    tmp = ENV.get_template('__manifest__.py.j2')
    py_code = tmp.render(module=module)
    return py_code


if __name__ == '__main__':
    # 'models': ['module', 'name', 'table_name', 'description', 'rec_name', 'auto', 'inherit', 'orderby'],
    # 'fields': ['name', 'string', 'model_name', 'module', 'help', 'comodel_name', 'related', 'groups',
    #            'inverse', 'compute', 'is_copy', 'is_index', 'is_required', 'is_readonly', 'is_store']
    models = {'module': 'module1',
              'name': 'name2',
              'table_name': 'table_name3',
              'description': 'description4',
              'rec_name': 'rec_name5',
              'auto': 'auto6',
              'inherit': 'inherit7',
              'orderby': 'orderby8',
              'functions': [{'name':'_compute_name'}]}
    field1 = {'name': 'name',
              'string': 'string',
              'ttype': 'char',
              'model_name': 'model_name',
              'module': 'module',
              'help': 'help',
              'comodel_name': 'comodel_name',
              'related': 'related',
              'groups': 'groups',
              'inverse': 'inverse',
              'compute': 'compute',
              'is_copy': 'is_copy',
              'is_index': 'is_index',
              'is_required': 'is_required',
              'is_readonly': 'is_readonly',
              'is_store': 'is_store'}
    fields2 = {'name': 'name',
               'string': 'string',
               'model_name': 'model_name',
               'ttype': 'char',
               'module': 'module',
               'help': 'help',
               'comodel_name': 'comodel_name',
               'related': 'related',
               'groups': 'groups',
               'inverse': 'inverse',
               'compute': 'compute',
               'is_copy': 'is_copy',
               'is_index': 'is_index',
               'is_required': 'is_required',
               'is_readonly': 'is_readonly',
               'is_store': 'is_store'}
    models['fields'] = [field1, fields2]
    g = PyGenerator([models])
    g.py_generator()
