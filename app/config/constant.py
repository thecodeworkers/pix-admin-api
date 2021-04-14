import os

APP_NAME = os.getenv('APP_NAME', '')
APP_KEY = os.getenv('APP_KEY', '')

DATABASE_NAME = os.getenv('DATABASE_NAME', 'pix')
DATABASE_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
DATABASE_PORT = int(os.getenv('DATABASE_PORT', 27017))
