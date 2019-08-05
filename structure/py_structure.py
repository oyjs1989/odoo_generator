#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Default = object()  # default value for __init__() methods
from common.common import gModuls, gModels, gFields, sql_db
_required_tables = {
    'modules': ['name', 'website', 'data', 'summary', 'author', 'version', 'category_id', 'description',
                'application', 'installable', 'license', 'sequence', 'auto_install'],
    'models': ['module', 'name', 'table_name', 'description', 'rec_name', 'auto', 'inherit', 'orderby'],
    'fields': ['name', 'string', 'model_name', 'module', 'help', 'comodel_name', 'related', 'groups',
               'inverse', 'compute', 'is_copy', 'is_index', 'is_required', 'is_readonly', 'is_store']}


class Structure(object):
    _required = []
    _attr = []
    Env = sql_db
    domain = []
    table = ''

    def _check_required(self):
        for required in self._required:
            if not hasattr(self, required):
                raise ValueError("%s is required,plz check data" % required)

    def insert_sql(self):
        return ('INSERT into %s (' % self.table + ','.join(
            [i[0] for i in self.serialization_tuple()]) + ') VALUES (' + ','.join(
            repr(i[1]) for i in self.serialization_tuple()) + ');'.replace('None', 'null')).replace('None', 'null')

    def update_sql(self):
        return 'UPDATE %s SET %s WHERE %s;'(self.table,
                                            ','.join(['='.join(values) for values in self.serialization_tuple()]),
                                            self.serialization_domain()).replace('None', 'null')

    def delete_sql(self):
        return 'delete from %s' % self.table + 'where' + ','.join([' '.join(operating) for operating in self.domain])

    def select_sql(self):
        return 'select * from %s' % self.table

    def serialization_domain(self):
        return ','.join([' '.join(operating) for operating in self.domain])

    def serialization_tuple(self):
        return [(attr, getattr(self, attr)) for attr in self._required]

    def serialization_dict(self):
        return {attr: getattr(self, attr) for attr in self._required}

    def execute(self, sql):
        try:
            self.Env.cursor.execute(sql)
            self.Env.con.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def create(self):
        print(self.serialization_dict())
        ret = self.execute(self.insert_sql())
        return ret

    def update(self):
        ret = self.execute(self.update_sql())
        return ret

    def delete(self):
        ret = self.execute(self.delete_sql())
        return ret


class Module(Structure):
    _models = []
    table = 'modules'
    _required = ['name', 'summary', 'author', 'website', 'version', 'data', 'sequence', 'category_id', 'license',
                 'application', 'installable', 'description', 'auto_install']

    def __init__(self, name, summary="", author="My Company", website="http://www.yourcompany.com", version='1.0',
                 data='', sequence=0, category_id=0, license='LGPL-3', application=False, installable=False,
                 description="", auto_install=False):
        self.website = website
        self.data = data
        self.summary = summary
        self.name = name
        self.author = author
        self.version = version
        self.category_id = category_id
        self.description = description
        self.application = application
        self.installable = installable
        self.license = license
        self.sequence = sequence
        self.auto_install = auto_install
        super(Module, self).__init__()


class Model(Structure):
    _fields = []
    table = 'models'
    _required = ['module', 'name', 'table_name', 'description', 'rec_name', 'auto', 'inherit', 'orderby']

    def __init__(self, module, name, inherit=None, table_name=None, orderby='id', rec_name="id", description="",
                 auto=True):
        self.module = module
        self.name = name
        self.table_name = table_name
        self.description = description
        self.rec_name = rec_name
        self.auto = auto
        self.inherit = inherit
        self.orderby = orderby
        super(Model, self).__init__()

    def _get_function(self):
        fun = []
        for field in self._fields:
            fun.append(field.get('compute'))
        return list(set(fun))


class Field(Structure):
    table = 'fields'
    ttype = 'field'
    _required = ['name', 'string', 'model_name', 'module', 'help', 'comodel_name', 'related', 'groups',
                 'inverse', 'compute', 'is_copy', 'is_index', 'is_required', 'is_readonly', 'is_store']
    _ttype_required = []
    _default = {
        'is_copy': True,
        'is_index': False,
        'is_required': False,
        'is_readonly': False,
        'is_store': True
    }

    def __init__(self, module, model_name, name, string, help=None, comodel_name=None, related=None, groups=None,
                 inverse=None, compute=None, is_copy=True, is_index=False, is_readonly=False, is_required=False,
                 is_store=True):
        self.name = name
        self.string = string
        self.model_name = model_name
        self.module = module
        self.help = help
        self.comodel_name = comodel_name
        self.related = related
        self.groups = groups
        self.inverse = inverse
        self.compute = compute
        self.is_copy = is_copy
        self.is_index = is_index
        self.is_required = is_required
        self.is_readonly = is_readonly
        self.is_store = is_store
        super(Field, self).__init__()

    def _check_required(self, args):
        super(Field, self)._check_required()
        for t_required in self._ttype_required:
            if t_required not in args:
                raise ValueError('%s is needed in %s' % (t_required, self.ttype))

    def serialization(self):
        return {
            'name': self.name,
            'string': self.string,
            'model_name': self.model_name,
            'module': self.module,
            'help': self.help,
            'comodel_name': self.comodel_name,
            'related': self.related,
            'groups': self.groups,
            'inverse': self.inverse,
            'compute': self.compute,
            'is_copy': self.is_copy,
            'is_index': self.is_index,
            'is_required': self.is_required,
            'is_readonly': self.is_readonly,
            'is_store': self.is_store,
        }


class Boolean(Field):
    ttype = 'boolean'


class Integer(Field):
    ttype = 'integer'


class Float(Field):
    ttype = 'float'


class Monetary(Field):
    ttype = 'monetary'


class Char(Field):
    ttype = 'char'


class Text(Field):
    ttype = 'text'


class Html(Field):
    ttype = 'html'


class Date(Field):
    ttype = 'date'


class Datetime(Field):
    ttype = 'datetime'


class Binary(Field):
    ttype = 'binary'


class Selection(Field):
    ttype = 'selection'


class Reference(Field):
    ttype = 'reference'


class Many2one(Field):
    ttype = 'many2one'
    _ttype_required = ['comodel_name']


class One2many(Field):
    ttype = 'one2many'
    _ttype_required = ['comodel_name', 'inverse_name']


class Many2many(Field):
    ttype = 'many2many'
    _ttype_required = ['comodel_name', 'inverse_name', 'relation', 'column1', 'column2']


class Access(object):

    def __init__(self):
        self.name = ''
        self.perm_write = ''
        self.perm_unlink = ''
        self.perm_create = ''
        self.perm_read = ''
        self.group_id = ''
        self.model_id = ''


class Constraint(object):

    def __init__(self):
        self.module = ''
        self.model = ''
        self.type = ''
        self.definition = ''  # unique(model) check(size>=0) check(mode != 'extension' or inherit_id is not null)
        self.name = ''  # ir_model_obj_name_uniq


class Cache(object):
    '''
    工厂类 根据入参创建模型
    '''
    _table_model = {
        'modules': Module,
        'models': Model,
        'fields': {'boolean': Boolean,
                   'integer': Integer,
                   'float': Float,
                   'monetary': Monetary,
                   'char': Char,
                   'text': Text,
                   'html': Html,
                   'datetime': Datetime,
                   'date': Date,
                   'binary': Binary,
                   'selection': Selection,
                   'reference': Reference,
                   'many2one': Many2one,
                   'many2many': Many2many,
                   'one2many': One2many
                   },
    }
    _requierd = []
    _default = ()

    _tables = {
        'modules': {},
        'models': {},
        'fields': {}
    }

    def __new__(cls, *args, **kwargs):
        table = kwargs.get('table')
        name = kwargs.get('name')
        if name not in cls._tables[table]:
            cls._tables[table][name] = object.__new__(cls)
        return cls._tables[table][name]

    def __init__(self, **kwargs):
        self.save(**kwargs)

    def save(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_attrs(self):
        return {field: getattr(self, field, None) for field in _required_tables[self.table]}


    def get_attrs_list(self):
        for table, fields in _required_tables.items():
            if table == self.table:
                return [getattr(self, field, None) for field in fields]

    def to_object(self):
        print(self.get_attrs())
        if not self.table:
            raise ValueError('Need table')
        if type(self._table_model[self.table]) == dict:
            return self._table_model[self.table][self.ttype](**self.get_attrs())
        return self._table_model[self.table](**self.get_attrs())


    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor < len(_required_tables[self.table]):
            self.cursor += 1
            return _required_tables[self.table][self.cursor], getattr(self, _required_tables[self.table][self.cursor], None)
        else:
            raise StopIteration


def initialize_all_data():
    for table, fields in _required_tables.items():
        sql = "select %s from %s" % (','.join(fields), table)
        sql_db.cursor.execute(sql)
        sql_data = sql_db.cursor.fetchall()
        allocating_data(table, sql_data)


def allocating_data(table, records):
    if table == 'modules':
        for record in records:
            name, website, data, summary, author, version, category_id, description, application, installable, license, sequence, auto_install = record
            gModuls[name] = Module(name=name, website=website, data=data, summary=summary, author=author,
                                   version=version,
                                   category_id=category_id, description=description, application=application,
                                   installable=installable, license=license, sequence=sequence,
                                   auto_install=auto_install)
    elif table == 'models':
        for record in records:
            module, name, table_name, description, rec_name, auto, inherit, orderby = record
            gModels[name] = Model(module=module, name=name, table_name=table_name, description=description,
                                  rec_name=rec_name, auto=auto, inherit=inherit, orderby=orderby)
            gModuls[module]._models.append(gModels[name])
    elif table == 'fields':
        for record in records:
            name, string, model_name, module, help, comodel_name, related, groups, inverse, compute, copy, index, required, readonly, store = record
            gFields[name] = Field(name=name, string=string, model_name=model_name, module=module, help=help,
                                  comodel_name=comodel_name, related=related, groups=groups, inverse=inverse,
                                  compute=compute, is_copy=copy, is_index=index, is_required=required,
                                  is_readonly=readonly, is_store=store)
            gModels[model_name]._fields.append(gFields[name])
    else:
        raise ValueError('Not expected table')


initialize_all_data()

if __name__ == '__main__':
    s = Field(**{'name': '1', 'compute': '-', 'inverse': '5', 'string': 'string', 'module': 'module',
                 'model_name': 'model_name'})
    print(s.serialization_dict)
