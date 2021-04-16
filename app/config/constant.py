import os

APP_NAME = os.getenv('APP_NAME', '')
APP_KEY = os.getenv('APP_KEY', '')
APP_SECRET = os.getenv('APP_SECRET', '')

DATABASE_USERS = os.getenv('DATABASE_USERS', 'pix_users')
DATABASE_RESOURCES = os.getenv('DATABASE_RESOURCES', 'pix_resources')
DATABASE_TRANSACTIONS = os.getenv('DATABASE_TRANSACTIONS', 'pix_transactions')
DATABASE_SETTINGS = os.getenv('DATABASE_SETTINGS', 'pix_settings')
DATABASE_LOGS = os.getenv('DATABASE_LOGS', 'pix_logs')

DATABASE_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
DATABASE_PORT = int(os.getenv('DATABASE_PORT', 27017))
