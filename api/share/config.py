import os
from box import Box
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

db = Box({
    "DB_HOST": os.environ.get("DB_HOST"),
    "DB_PORT": os.environ.get("DB_PORT"),
    "DB_NAME": os.environ.get("DB_NAME"),
    "DB_PASSWORD": os.environ.get("DB_PASSWORD"),
    "DB_USER": os.environ.get("DB_USER")
    })
    
CONFIG = Box({
    "db": db
})
