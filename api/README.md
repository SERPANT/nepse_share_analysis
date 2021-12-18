# Steps to run the application

* Create a virutal env inside api folder: python -m virtualenv venv

* Execute the virtual env: ./api/Scripts/activate

* Set up python packages: pip install -r requirement.txt

* Copy .env.example and create .env

* Set up .env file inside /api

* Run the app: python ./api/share/app.py or cd ./api/share & flask run


# Setup Database

* Create the database share_info

* Run migration to create the tables 

* psql -h <IP_Address> -p <port_no> -d <database_name> -U <DB_username> -W

* Set up seed data
