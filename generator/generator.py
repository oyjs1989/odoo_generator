# -*- coding: utf-8 -*-
#   File Name：     generator
#   Author :        lumi
#   date：          2019/7/25
#   Description :

# - Third party module of python
from jinja2 import Environment, Template, PackageLoader
# - Custom package
import os
import autopep8
from datetime import datetime

if __name__ == '__main__':
    PACKAGE = 'templates'
else:
    PACKAGE = 'generator.templates'

ENV = Environment(loader=PackageLoader(PACKAGE))
PATH = os.getcwd()
MODULE_INIT = '# -*- coding: utf-8 -*-\n# Part of Odoo. See LICENSE file for full copyright and licensing details.\nimport models\nimport wizard\nimport controllers'


class Generator(object):
    '''
    将json转化成python代码
    '''

    def __init__(self, dir_path='%s/%s' % (PATH, datetime.now().strftime('%y_%m_%d_%H_%M_%S'))):
        self.dir_path = dir_path

    def generate_all(self, module: dict):
        # 生成文件夹结构
        module_name = module.get('name')
        self.generate_structure(self, module_name)
        # 外部文件__mainfest__.py
        self.generate_mainfest(module)
        self.generate_models(module.get('generate_models'))
        self.generate_data(module.get('data'))
        self.generate_security(module.get('security'))
        self.generate_views(module.get('views'))
        self.generate_report(module.get('report'))
        self.generate_wizard(module.get('wizard'))
        self.generate_controllers(module.get('controllers'))
        return True

    def generate_data(self, data):
        pass

    def generate_security(self, security):
        pass

    def generate_views(self, views):
        pass

    def generate_report(self, report):
        pass

    def generate_wizard(self, wizard):
        pass

    def generate_controllers(self, controllers):
        pass

    def py_header_render(self, file_name=None, date_time=datetime.today().strftime('%y%m%d')):
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

    def open_file(self, type_dir, file_name):
        '''
        文件名 文件位置
        :return:
        '''
        DIR_PATH = os.path.join(self.dir_path, type_dir, file_name)
        if not os.path.exists(DIR_PATH):
            os.makedirs(DIR_PATH)
        return open(DIR_PATH, 'w')

    def class_render(self, model: dict):
        model_code = self.model_render(model)
        field_code = self.fields_render(model.get('fields'))
        function_code = self.function_render(model.get('functions'))
        return model_code + field_code + function_code

    def generate_models(self, models: list):
        '''
        拆解 modules 数据
        :return:
        '''
        for model in models:
            f = self.open_file('models', file_name=model.get('file_name'))
            if f.tell() == 0:
                codes = self.py_header_render()
            else:
                codes = ""
            codes += self.class_render(model)
            f.write(codes)
            f.close()
            autopep8.main(('autopep8', "--in-place", "--aggressive", "--aggressive",
                           os.path.join(self.file_path, 'models', model.get('file_name'))))

    def generate_structure(self, module_name):
        _dir_list = ['controllers', 'data', 'i18n', 'models', 'report', 'security', 'static', 'views', 'wizard']
        _py_dir = ['controllers', 'models', 'wizard', 'report']
        if not os.path.exists(os.path.join(self.dir_path, module_name)):
            os.mkdir(os.path.join(self.dir_path, module_name))

        if not os.path.exists(os.path.join(self.dir_path, module_name,'__init__.py')):
            open(os.path.join(self.dir_path, module_name, '__init__.py'), 'w').write(MODULE_INIT)

        for dir_name in _dir_list:
            if not os.path.exists(os.path.join(self.dir_path, module_name, dir_name)):
                os.mkdir(os.path.join(self.dir_path, module_name, dir_name))

            if dir_name in _py_dir:
                open(os.path.join(self.dir_path, module_name, dir_name, '__init__.py'), 'w')

    def model_access_render(self, model_name: str, group_id='', read=1, write=1, create=1, unlink=1):
        id = 'access_%s' % model_name
        name = 'access_%s' % model_name
        model_id = 'model_%s' % model_name
        group_id = group_id
        perm_read = read
        perm_write = write
        perm_create = create
        perm_unlink = unlink
        return '%s,%s,%s,%s,%s,%s,%s,%s\n' % (
            id, name, model_id, group_id, perm_read, perm_write, perm_create, perm_unlink)

    def view_render(self, model):
        pass

    def tree_render(self, model):
        pass

    def manifest_render(self, module):
        tmp = ENV.get_template('__manifest__.py.j2')
        py_code = tmp.render(module=module)
        return py_code

    def generate_mainfest(self, module):
        code = self.manifest_render(module)
        open(os.path.join(self.dir_path, module.get('name'), '__init__.py'), 'w').write(code)


if __name__ == '__main__':
    pass
    # models = {'module': 'module1',
    #           'name': 'name2',
    #           'table_name': 'table_name3',
    #           'description': 'description4',
    #           'rec_name': 'rec_name5',
    #           'auto': 'auto6',
    #           'inherit': 'inherit7',
    #           'orderby': 'orderby8',
    #           'functions': [{'name': '_compute_name'}]}
    # field1 = {'name': 'name',
    #           'string': 'string',
    #           'ttype': 'char',
    #           'model_name': 'model_name',
    #           'module': 'module',
    #           'help': 'help',
    #           'comodel_name': 'comodel_name',
    #           'related': 'related',
    #           'groups': 'groups',
    #           'inverse': 'inverse',
    #           'compute': 'compute',
    #           'is_copy': True,
    #           'is_index': True,
    #           'is_required': True,
    #           'is_readonly': True,
    #           'is_store': True}
    # fields2 = {'name': 'name',
    #            'string': 'string',
    #            'model_name': 'model_name',
    #            'ttype': 'char',
    #            'module': 'module',
    #            'help': 'help',
    #            'comodel_name': 'comodel_name',
    #            'related': 'related',
    #            'groups': 'groups',
    #            'inverse': 'inverse',
    #            'compute': 'compute',
    #            'is_copy': True,
    #            'is_index': True,
    #            'is_required': True,
    #            'is_readonly': True,
    #            'is_store': True}
    # models['fields'] = [field1, fields2]
    # g = Generator([models])
    # g.py_generator()
    g = Generator(r'C:\Users\lumi\Desktop\fsdownload')
    g.structure_render('test')
