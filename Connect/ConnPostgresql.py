import psycopg2 # type: ignore
import os
from psycopg2 import OperationalError # pyright: ignore[reportMissingModuleSource]
from dotenv import load_dotenv

load_dotenv()
 

def crear_conexion():
    try:
        conexion = psycopg2.connect(
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            host=os.getenv('host'),
            port=os.getenv('port'),
        )
        print("Its connected!")
        return conexion
    except OperationalError as e:
        print(f"Error'{e}'.")
        return None

