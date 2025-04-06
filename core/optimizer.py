from .ast_models import Column, Literal, Condition
from typing import List, Optional

def optimize_query(query: 'SelectQuery') -> 'SelectQuery':
    if query.where:
        query.where = [cond for cond in query.where if not _is_useless_condition(cond)]
        if not query.where:
            query.where = None
    return query

def _is_useless_condition(cond: Condition) -> bool:
    return (
        isinstance(cond.left, Column) 
        and isinstance(cond.right, Column)
        and cond.left.name == cond.right.name
        and cond.op == "="
    )