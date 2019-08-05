# -*- coding: utf-8 -*-


class Modules(object):
    name = ''
    version = 1.0
    category = ''
    sequence = 0
    summary = """"""
    depends = []
    description = """"""
    application = True
    license = ''
    models = []
    installable: True
    auto_install: True
    post_init_hook: 'post_init'

class Models(object):

    _auto = False  # dont create any databasebackend
    _register = False  # not visible in ORMregistry
    _abstract = True  # whether model isabstract
    _transient = False  # whether model istransient
    _name = None  # the modelname
    _description = None  # the models informalname
    _custom = False  # should be True for custom modelsonly
    _inherit = None  # Python-inherited models (model or[model])
    _inherits = {}  # inherited models {parent_model:m2o_field}
    _constraints = []  # Python constraints (oldAPI)
    _table = None  # SQL table name used bymodel
    _sequence = None  # SQL sequence to use for IDfield
    _sql_constraints = []  # SQL constraints [(name, sql_def,message)]
    _rec_name = None  # field to use for labelingrecords
    _order = id  # default order for searchingresults
    _module = None


class Fields(object):
    table = 'field'
    _module = None  # the fields module name
    _setup_done = None  # the fields setup state= None base or full
    automatic = False  # whether the field is automatically created ("magic" field)
    inherited = False  # whether the field is inherited (_inherits)
    name = None  # name of the field
    model_name = None  # name of the model of this field
    comodel_name = None  # name of the model of values (if relational)
    store = True  # whether the field is stored in database
    index = False  # whether the field is indexed in database
    manual = False  # whether the field is a custom field
    copy = True  # whether the field is copied over by BaseModel.copy()
    depends = ()  # collection of field dependencies
    recursive = False  # whether self depends on itself
    compute = None  # compute(recs) computes field on recs
    compute_sudo = False  # whether field should be recomputed as admin
    inverse = None  # inverse(recs) inverses field on recs
    search = None  # search(recs operator value) searches on self
    related = None  # sequence of field names for related fields
    related_sudo = True  # whether related fields should be read as admin
    company_dependent = False  # whether ``self`` is company-dependent (property field)
    sparse = None  # the name of the corresponding serialized field if any
    default = None  # default(recs) returns the default value
    field_description = None  # field label
    help = None  # field tooltip
    readonly = False  # whether the field is readonly
    required = False  # whether the field is required
    states = None  # set readonly and required depending on state
    groups = None  # csv list of group xml ids
    change_default = False  # whether the field may trigger a "user-onchange"
    deprecated = None  # whether the field is deprecated
    related_field = None  # corresponding related field
    group_operator = None  # operator for aggregating values
    group_expand = None  # name of method to expand groups in read_group()
    prefetch = True  # whether the field is prefetched
    ondelete = 'set null'  # what to do when value is deleted
    auto_join = False  # whether joins are generated upon search
    delegate = False  # whether self implements delegation
    inverse_name = None  # name of the inverse field
    limit = None  # optional limit to use upon read
    relation = None  # name of table
    column1 = None  # column of table referring to model
    column2 = None  # column of table referring to comodel
    track_visibility = None  # column of table referring to comodel


class Views(object):
    id = ''
    type_model = ''
    name = ''
    model = ''
    type = ''
    inherit_id = ''


class Security(object):
    id = ''
    name = ''
    model_id = ''
    group_id = ''
    perm_read = False
    perm_write = False
    perm_create = False
    perm_unlink = False

