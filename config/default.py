import os
from .database import create_database_url


SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(64).hex())

PROPAGATE_EXCEPTIONS = True

# Database configuration
SQLALCHEMY_DATABASE_URI = create_database_url()
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

ERROR_404_HELP = False
