import os
from dotenv import load_dotenv

env_file = '.env'
if os.getenv('RUN_ENV') == 'development':
    env_file = '.env.development'
elif os.getenv('RUN_ENV') == 'production':
    env_file = '.env.production'


load_dotenv(env_file)


class Config:
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
