from box import Box
from dotenv import dotenv_values

# env = Box(dotenv_values("../.env.production"))
env = Box(dotenv_values())

db = Box({
    "DB_HOST": env.DB_HOST,
    "DB_PORT": env.DB_PORT,
    "DB_NAME": env.DB_NAME,
    "DB_PASSWORD": env.DB_PASSWORD,
    "DB_USER": env.DB_USER
    })

CONFIG = Box({
    "db": db
})
