from dto import AdminSettings
import os

class AdminRepo:
    def __init__(
            self, 
            admin_settings: AdminSettings
        ):
        self.admin_settings = admin_settings
    def check_code(
            self, 
            code: int
        ):
        try:
            if code == self.admin_settings.ADMIN_CODE:
                return {"status": "valid", 'token': self.admin_settings.ADMIN_TOKEN} 
            return {"status": "invalid"}
        except Exception as e:
            print(e)
            return {"status": "error"}