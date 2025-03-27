from dto import AdminSettings, MenuDTO
from src.repository.admin_repo import AdminRepo
from src.service.admin_service import AdminService
from src.service.data_service import DataService
from src.repository.data_repo import DataRepo
from src.service.connection_service import ConnectionService
from src.repository.connection_repo import ConnectionRepo
from src.models.menu_model import MenuModel
from src.repository.menu_repo import MenuRepo
from src.service.menu_processing_service import MenuProcessingService

menu_repo = MenuRepo(MenuModel, MenuDTO)
menu_service = MenuProcessingService(menu_repo)

data_repo = DataRepo()
data_service = DataService(data_repo)

connection_repo = ConnectionRepo()
connection_service = ConnectionService(connection_repo)

admin_settings = AdminSettings()
admin_repo = AdminRepo(admin_settings)
admin_service = AdminService(admin_repo)

def get_menu_service():
    return menu_service

def get_data_storage():
    return data_service

def get_websocket_manager():
    return connection_service

def get_code():
    return admin_service