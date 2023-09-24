from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"


class Criterion(str, Enum):
    all = "all"
    completed = "completed"
    pending = "pending"
    canceled = "canceled"


class Order(BaseModel):
    id: int
    item: str
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0.0)
    status: OrderStatus


class OrdersRequest(BaseModel):
    orders: List[Order]
    criterion: Criterion
