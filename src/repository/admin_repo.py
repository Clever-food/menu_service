from src.config.config import settings

class AdminRepo:
    def __init__(
            self, 
        ) -> None:
        pass
    def check_code(
            self, 
            code: int
        ):
        try:
            if code == settings.ADMIN_CODE:
                return {"status": "valid", 'token': settings.ADMIN_TOKEN} 
            return {"status": "invalid"}
        except Exception as e:
            print(e)
            return {"status": "error"}