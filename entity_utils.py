from multipledispatch import dispatch
from entities import Database, Table, Column, DataType, Integer, String


# Loads Database or table
@dispatch(str, str, str)
def load_entity(name, title, entity_name):
    if entity_name == "database":
        entity = Database()
        entity.name = name
        entity.title = title
        return entity
    elif entity_name == "table":
        entity = Table()
        entity.name = name
        entity.title = title
        return entity


# Loads DataType
@dispatch(str)
def load_entity(name):
    if name == "integer":
        entity = Integer()
        entity.name = name
        return entity
    elif name == "string":
        entity = String()
        entity.name = name
        return entity


# Loads Column
@dispatch(str, str, DataType)
def load_entity(name, title, dtype):
    entity = Column()
    entity.name = name
    entity.title = title
    entity.dtype = dtype
    return entity
