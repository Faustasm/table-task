import pytest
import sys

sys.path.append("..")  # Adds higher directory to python modules path.

from entity_utils import load_entity
from transform_table import read_table_data
from entities import Database, Table, Column, Integer, String


def test_wrong_data_type_in_load_function():
    with pytest.raises(NotImplementedError):
        load_entity(1, 2, 3)

def test_database_type_assignment_in_load_function():
    entity = load_entity('db name', 'db title', 'database')
    assert isinstance(entity, Database)

def test_table_type_assignment_in_load_function():
    entity = load_entity('table name', 'table title', 'table')
    assert isinstance(entity, Table)

def test_datatype_type_assignment_in_load_function():
    entity = load_entity('integer')
    assert isinstance(entity, Integer)
    entity = load_entity('string')
    assert isinstance(entity, String)

def test_column_type_assignment_in_load_function():
    data_type = load_entity('integer')
    entity = load_entity('column name', 'column type', data_type)
    assert isinstance(entity, Column)

def test_trailing_and_leading_whitespace_removal():
    table_data = read_table_data('table.txt')
    for header_column in table_data[0]:
        assert header_column.strip() == header_column
    for entity in table_data[1:]:
        if isinstance(entity, Database | Table | Column):
            assert entity.name == entity.name.strip()
            assert entity.title == entity.title.strip()
        if isinstance(entity, Column):
            assert entity.dtype.name == entity.dtype.name.strip()
