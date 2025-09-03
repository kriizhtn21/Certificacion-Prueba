"""
Configuración para Ideas Dashboard
"""

import os
from datetime import timedelta

class Config:
    """Configuración base"""
    
    # Configuración de Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_muy_segura_aqui'
    
    # Configuración de base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:emiliateamo@localhost/ideas_dashboard'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    # Configuración de sesiones
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Configuración de archivos
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Configuración de validaciones
    MIN_PASSWORD_LENGTH = 8
    MIN_IDEA_LENGTH = 5
    MIN_NAME_LENGTH = 2
    MAX_IDEA_LENGTH = 1000

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    """Configuración para pruebas"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

# Diccionario de configuraciones
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
