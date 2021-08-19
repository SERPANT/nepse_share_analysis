import os
from box import Box
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

db = Box({
    "DB_HOST":  "sh-database.postgres.database.azure.com",
    "DB_PORT": "5432",
    "DB_NAME": "share_info",
    "DB_PASSWORD": "123456798rockoN.",
    "DB_USER": "shreejit@sh-database"
    })

print("====================================")
print(db)
    
CONFIG = Box({
    "db": db
})
