from venv import create
from sqlalchemy import create_engine
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'school'


def get_connection():
    return create_engine('mysql+pymysql://%s:%s@%s:%s/%s' % (user, password, host, port, database))