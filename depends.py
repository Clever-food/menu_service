from src.client.payment_client import PaymentClient
from src.repository.admin_repo import AdminRepo
from src.service.admin_service import AdminService
from src.service.data_service import DataService
from src.repository.data_repo import DataRepo
from src.service.connection_service import ConnectionService
from src.repository.connection_repo import ConnectionRepo
from src.models.menu_model import MenuModel
from src.repository.menu_repo import MenuRepo
from src.service.menu_processing_service import MenuProcessingService

menu_repo = MenuRepo(MenuModel)
menu_service = MenuProcessingService(menu_repo)

def get_menu_service() -> MenuProcessingService:
    return menu_service


data_repo = DataRepo()
data_service = DataService(data_repo)

def get_data_storage() -> DataService:
    return data_service

connection_repo = ConnectionRepo()
connection_service = ConnectionService(connection_repo)

def get_websocket_manager() -> ConnectionService:
    return connection_service


admin_repo = AdminRepo()
admin_service = AdminService(admin_repo)

def get_code() -> AdminService:
    return admin_service


payment_client = PaymentClient()

def get_payment_client() -> PaymentClient:
    return payment_client
