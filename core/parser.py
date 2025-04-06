from parsimonious import Grammar, NodeVisitor
from parsimonious.nodes import Node
from .ast_models import *
from .exceptions import ParseError
from pathlib import Path

class QueryVisitor(NodeVisitor):
    def visit_query(self, node: Node, children) -> SelectQuery:
        select, from_, where, group, limit = children
        return SelectQuery(
            columns=select,
            table=from_,
            where=where[0] if where else None,
            group_by=group[0] if group else None,
            limit=int(limit[0].text) if limit else None
        )
    
    def visit_column(self, node: Node, children) -> Column:
        name, *alias = children
        return Column(name=name.text, alias=alias[0].text if alias else None)
    
    def visit_literal(self, node: Node, children) -> Literal:
        value = node.text
        return Literal(
            value=int(value) if value.isdigit() else value.strip("'"),
            type="number" if value.isdigit() else "string"
        )

class NoSQLParser:
    def __init__(self):
        grammar_path = Path(__file__).parent.parent / "grammar" / "grammar.peg"
        with open(grammar_path) as f:
            self.grammar = Grammar(f.read())

    def parse(self, sql: str) -> SelectQuery:
        try:
            tree = self.grammar.parse(sql)
            return QueryVisitor().visit(tree)
        except Exception as e:
            raise ParseError(str(e), getattr(e, "pos", None))