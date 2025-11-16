from fastapi import APIRouter, Depends
from src.app.http_exceptions import ExternalServiceError
from src.client.payment_client import PaymentClient
from depends import get_payment_client

payment_router = APIRouter(
    prefix="/payment", 
    tags=["payment"]
)

@payment_router.post("/payment-start")
def payment_start(
    payment: PaymentClient = Depends(get_payment_client),
):
    try:
        payment.send_to_payment_start()
        return {"payment_process": "started"}
    except ExternalServiceError as e:
        raise ExternalServiceError(e.model)

@payment_router.post("/payment-end")
def payment_end(
    payment: PaymentClient = Depends(get_payment_client),
):
    try:
        payment.send_to_payment_end()
        return {"payment_process": "ended"}
    except ExternalServiceError as e:
        raise ExternalServiceError(e.model)