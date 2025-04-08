# Configuraci�n de la app y la DB

import os
from re import S

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgresuser:postgresUser@38.242.234.236:5432/taller01_dev"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False