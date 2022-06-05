#context manager
import sqlite3


class Conn_Open:
    def __init__(self,db_name):
        self.db_name=db_name

    def __enter__(self):
        self.conn=sqlite3.connect(self.db_name)
        return self.conn

    def __exit__



if __name__=='__main__':
    dbname='test.db'
    with Conn_Open(db_name) as conn:
        cursor1=conn.cursor()