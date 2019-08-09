import MySQLdb

### Configs
DB_HOST = "192.168.1.29"
DB_NAME = "coin_test1"


def db_connection():
    db_conn = MySQLdb.connect(
        host=DB_HOST, # your host, usually localhost
        user="pi", # your username
        passwd="raspberry", # your password
        db=DB_NAME # name of the data base
    ) 
	return db_conn


db = db_connection()
