import os
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

def create_connection(dbname):
    """ create a database connection to the SQLite database
        specified by the dbname
    :param dbname - name of database
    :return: Connection object or None
    """

    host = os.getenv('host')
    user = os.getenv('user')
    password = os.getenv('password')
    sslmode = "require"

    try:
        conn_string = 'postgresql+psycopg2://%s:%s@%s:5432/%s'%(user,password,host,dbname)
        engine = create_engine(conn_string,poolclass=NullPool)
        return engine.connect()
    except Exception as error:
        print("Failed to connect to %s %s due to %s"%(host,dbname,error))
