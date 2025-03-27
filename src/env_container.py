
class EnvContainer():
    def __init__(self) -> None:

        self.__postgres_db_name: str = "CleverBistro_menu_service_db"
        self.__postgres_user_name: str = "postgres"
        self.__postgres_password: str = "root"
        self.__postgres_host: str = "127.0.0.1"
        self.__postgres_port: str = 5432

    def postgres_db_name(self):
        return self.__get_from_env(self.__postgres_db_name)
    
    def postgres_user_name(self):
        return self.__get_from_env(self.__postgres_user_name)
    
    def postgres_password(self):
        return self.__get_from_env(self.__postgres_password)
    
    def postgres_host(self):
        return self.__get_from_env(self.__postgres_host)
    
    def postgres_port(self):
        return int(self.__get_from_env(self.__postgres_port))

env_container = EnvContainer()
