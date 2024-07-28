import os

# Get the base directory
basedir = os.path.abspath(os.path.dirname(__file__))


# Default configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    DATABASE = os.path.join(basedir, 'flaskr.sqlite')
    DEBUG = False
    TESTING = False


# Development configuration
class DevelopmentConfig(Config):
    DEBUG = True


# Testing configuration
# class TestingConfig(Config):
#     TESTING = True
#     DATABASE = os.path.join(basedir, 'flaskr-test.sqlite')
#

# Production configuration
class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False


# Set the configuration
config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
