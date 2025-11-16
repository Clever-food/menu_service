import requests
from src.app.http_exceptions import ExternalServiceError
from src.config.config import settings

class PaymentClient:
    _payment_url = f"http://{settings.CORE_URL}"
    
    def __init__(self) -> None:
        pass

    def send_to_payment_start(
        self, 
    ):
        
        print("Запускаем Pipeline", self._payment_url)
        response = requests.post(f"{self._payment_url}/core/payment-start")
        
        print("Payment status_code = ", response.status_code)
        if response.status_code != 200:
            raise ExternalServiceError(response.json())
            
        print("Pipeline начал работу")
    
    def send_to_payment_end(
        self, 
    ):
        
        print("Останавливаем Pipeline", self._payment_url)
        response = requests.post(f"{self._payment_url}/core/payment-end")
        
        print("Payment status_code = ", response.status_code)
        if response.status_code != 200:
            raise ExternalServiceError(response.json())
            
        print("Pipeline закончил работу")
