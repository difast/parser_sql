from pydantic import BaseModel
from typing import List, Union, Optional, ForwardRef

#Для аннотаций с циклическими ссылками
Condition = ForwardRef('Condition')

class Column(BaseModel):
    name: str
    alias: Optional[str] = None

class Literal(BaseModel):
    value: Union[str, int, float]
    type: str  # "string" | "number"

class Condition(BaseModel):
    left: Union[Column, Literal, 'Condition']
    op: str  # "=", ">", "<", "LIKE"
    right: Union[Column, Literal, 'Condition']

class SelectQuery(BaseModel):
    columns: List[Column]
    table: str
    where: Optional[List[Condition]] = None
    group_by: Optional[List[Column]] = None
    limit: Optional[int] = None

# Разрешаем циклические ссылки
Condition.update_forward_refs()