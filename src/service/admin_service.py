from src.repository.admin_repo import AdminRepo


class AdminService:
    
    def __init__(self, admin_repo: AdminRepo):
        self.admin_repo = admin_repo

    def check_code(self, code):
        return self.admin_repo.check_code(code)
