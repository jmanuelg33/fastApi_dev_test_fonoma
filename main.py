from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from schemas import OrdersRequest

app = FastAPI()


@app.post("/solution")
async def solution(req: OrdersRequest):
    return process_orders(req.orders, req.criterion)


def process_orders(orders, criterion) -> float:
    return sum(order.price * order.quantity
               for order in orders
               if criterion == "all" or order.status == criterion)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_messages = []

    for error in exc.errors():
        error_messages.append({error["loc"][-1]: error["msg"]})

    return JSONResponse(content={"error": error_messages}, status_code=422)
