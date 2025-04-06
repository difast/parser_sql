import pytest
from core.parser import NoSQLParser
from core.ast_models import SelectQuery, Column, Literal

@pytest.fixture
def parser():
    return NoSQLParser()

def test_simple_select(parser):
    query = parser.parse("SELECT id, name FROM users")
    assert query.table == "users"
    assert len(query.columns) == 2
    assert query.columns[0].name == "id"

def test_where_condition(parser):
    query = parser.parse("SELECT * FROM orders WHERE amount > 100")
    assert query.where[0].op == ">"
    assert query.where[0].right.value == 100

def test_invalid_syntax(parser):
    with pytest.raises(Exception):
        parser.parse("SELECT FROM")