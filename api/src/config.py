from box import Box
from dotenv import dotenv_values

db = {}
env = Box(dotenv_values())

if env.env == "prod":
    db = Box({
        "DB_HOST": env.DB_HOST_PROD,
        "DB_PORT": env.DB_PORT_PROD,
        "DB_NAME": env.DB_NAME_PROD,
        "DB_PASSWORD": env.DB_PASSWORD_PROD,
        "DB_USER": env.DB_USER_PROD
    })
else:
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
