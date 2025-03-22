from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class DatabaseConnection:
    def __init__(self):
        pass
    
    @staticmethod
    def build_connection_string(config:dict)->str:
        db_type=config.get("db_type").lower()
        username=config.get("username")
        password=config.get("password")
        host= config.get("host")
        port= config.get("port")
        dbname= config.get("db_name")
        
        if db_type=="postgress":
            return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
        elif db_type=="mysql":
            return f"mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}"
        elif db_type == "mariadb":
            # MariaDB using the mariadbconnector
            return f"mysql+mariadbconnector://{username}:{password}@{host}:{port}/{dbname}"
        else:
            raise ValueError("Unsupported database type provided.")
    
    @staticmethod
    def connect_to_database(config:dict):
        try:
            conn_str = DatabaseConnection.build_connection_string(config)
            engine = create_engine(conn_str)
            with engine.connect() as connection:
                print("Connection Successful!")
            return engine
        except SQLAlchemyError as e:
            print(f"Failed to connect: {e}")
            return None
        
    @staticmethod 
    def get_engine(conn_str):
        try:
            engine= create_engine(conn_str)
            with engine.connect() as connection:
                print("Connection Successfull")
            return engine
        except SQLAlchemyError as e:
            print(f"Failed to connect: {e}")
            return None
            