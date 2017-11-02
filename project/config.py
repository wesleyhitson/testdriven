class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = True

class DevelopmentConfig:
    """Development configuration"""
    DEBUG = True

class TestingConfig:
    """Testing configuration"""
    DEBUG = True
    TESTING = True

class ProductionConfig:
    """Production configuration"""
    DEBUG = False
     
