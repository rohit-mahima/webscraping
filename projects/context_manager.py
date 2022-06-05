#context manager
class Conn_Open:


if __name__=='__main__':
    dbname='test.db'
    with Conn_Open(db_name) as conn:
        cursor1=conn.cursor()