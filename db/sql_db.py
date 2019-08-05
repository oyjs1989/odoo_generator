# -*- coding: utf-8 -*-
#   File Name：     sql_db
#   Author :        lumi
#   date：          2019/7/25
#   Description :


# - Third party module of python
from sqlite3 import connect, Connection




# - Custom package

class Sqlite(object):

    _required_tables = {
        'modules': ['name', 'website', 'data', 'summary', 'author', 'version', 'category_id', 'description',
                    'application', 'installable', 'license', 'sequence', 'auto_install'],
        'models': ['module', 'name', 'table_name', 'description', 'rec_name', 'auto', 'inherit', 'orderby'],
        'fields': ['name', 'string', 'model_name', 'module', 'help', 'comodel_name', 'related', 'groups',
                   'inverse', 'compute', 'is_copy', 'is_index', 'is_required', 'is_readonly', 'is_store']}

    _init_table = {
        'modules': ['name CHAR(100) UNIQUE', 'website CHAR(100)', 'data TEXT', 'summary TEXT', 'author CHAR(100)',
                    'version CHAR(100)', 'category_id int', 'description TEXT',
                    'application BOOLEAN', 'installable BOOLEAN', 'license CHAR(100)', 'sequence int',
                    'auto_install BOOLEAN'],
        'models': ['module CHAR(100)', 'name CHAR(100) UNIQUE', 'table_name CHAR(100)', 'description TEXT',
                   'rec_name CHAR(100)', 'auto BOOLEAN', 'inherit CHAR(255)', 'orderby  CHAR(255)'],
        'fields': ['name CHAR(100) UNIQUE', 'string CHAR(100)', 'model_name CHAR(100)', 'module CHAR(100)', 'help TEXT',
                   'comodel_name CHAR(100)', 'related CHAR(100)', 'groups CHAR(100)',
                   'inverse CHAR(100)', 'compute CHAR(100)', 'is_copy BOOLEAN', 'is_index BOOLEAN',
                   'is_required BOOLEAN', 'is_readonly BOOLEAN', 'is_store BOOLEAN']}

    def __init__(self):
        self.con = connect('local.db')
        self.cursor = self.con.cursor()
        self.init_required_tables()


    def get_existence_table(self):
        all_tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [name[0] for name in all_tables]

    def init_required_tables(self):
        all_tables = self.get_existence_table()
        for table, fields in self._init_table.items():
            if table not in all_tables:
                sql = '''CREATE TABLE %s (%s);''' % (table, ','.join(fields))
                self.cursor.execute(sql)
        self.con.commit()

    def create_table(self, table, values):
        pass

    def delete_table(self, table):
        pass

    def update_talbe(self, table, name, values):
        pass

    def select_table(self, table):
        pass


sql_db = Sqlite()

class Table(object):
    _table_name = ''

    def __init__(self):
        pass

    def save(self, table):
        pass


class Fields(Table):
    pass


if __name__ == '__main__':
    sql = Sqlite()
