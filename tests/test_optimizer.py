from core.ast_models import SelectQuery, Column, Literal, Condition
from core.optimizer import optimize_query

def test_remove_useless_conditions():
    query = SelectQuery(
        columns=[Column(name="user_id")],
        table="users",
        where=[
            Condition(
                left=Column(name="user_id"),
                op="=",
                right=Column(name="user_id")
            )
        ]
    )
    
    optimized = optimize_query(query)
    assert optimized.where is None

def test_keep_valid_conditions():
    query = SelectQuery(
        columns=[Column(name="name")],
        table="users",
        where=[
            Condition(
                left=Column(name="age"),
                op=">",
                right=Literal(value=18, type="number")
            )
        ]
    )
    
    optimized = optimize_query(query)
    assert len(optimized.where) == 1

def test_empty_where():
    query = SelectQuery(
        columns=[Column(name="*")],
        table="products",
        where=None
    )
    
    optimized = optimize_query(query)
    assert optimized.where is None

def test_multiple_conditions():
    query = SelectQuery(
        columns=[Column(name="email")],
        table="accounts",
        where=[
            Condition(
                left=Column(name="id"),
                op="=",
                right=Column(name="id")
            ),
            Condition(
                left=Column(name="status"),
                op="=",
                right=Literal(value="active", type="string")
            )
        ]
    )
    
    optimized = optimize_query(query)
    assert len(optimized.where) == 1
    assert optimized.where[0].right.value == "active"