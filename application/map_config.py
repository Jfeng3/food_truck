import os
DEBUG = True
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = os.environ.get('SECRET_KEY','i_dont_know')
HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS','localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME','food_truck')
IP = os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))
PG_DB_HOST = os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST','localhost')
PG_DB_PORT = int(os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT',5432))
PG_DB_USERNAME = os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME','jiefeng')
PG_DB_PASSWORD = os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD','')
TABLE_NAME = os.environ.get('TABLE_NAME', 'truck_location')