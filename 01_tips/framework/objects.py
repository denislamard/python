'''
@author: denis Lamard
'''

from enum import Enum, unique

@unique
class DataType(Enum):
    dt_unknown = 0
    dt_integer = 1
    dt_float = 2
    dt_boolean = 3
    dt_string = 4
    dt_list = 5
    dt_array = 6

@unique
class InputType(Enum):
    ip_unknown = 0
    ip_standard = 1
    ip_list = 2
    ip_array = 3
    ip_form = 4

class Property(object):
    
    def renderStandard(self):
        pass
    
    def renderList(self):
        pass
    
    def renderArray(self):
        pass
    
    def renderForm(self):
        pass
    
    
    options = {
        InputType.ip_standard : renderStandard,
        InputType.ip_list : renderList,
        InputType.ip_array : renderArray,
        InputType.ip_form : renderForm,
    }    
        
    
    def __init__(self):
        self.name = 'name'
        self.datatype = DataType.dt_unknown
        self.require = True
        self.default = {'value' : ''}
        self.min = {'value' : ''}
        self.max = {'value' : ''}
        self.input = InputType.ip_unknown
        self.urlform = None
        self.value = {'value' : ''}

    def render(self):
        return self.options[self.input]()

class Properties(object):
    
    def __init__(self):
        pass
    
    def addProperty(self, property):
        pass
    
    def deleteProperty(self, property):
        pass
    
    def __iter__(self):
        return self
    
    def _next(self):
        pass
    
    __next__ = _next     
    

class Objects(object):
    def __init__(self, name, typeobject, level, parent):
        self.id = 0
        self.name = name
        self.level = level
        self.parent = parent
        self.typeobject = typeobject
        self.children = []
        self._childIndex = 0
        self.properties = Properties()
    
    def addChild(self, child):
        pass
    
    def deleteChild(self, child):
        pass
    
    def __iter__(self):
        return self
    
    def _next(self):
        pass
    
    def __repr__(self):
        return self.name
    
    __next__ = _next 