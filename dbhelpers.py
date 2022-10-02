import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("Operational Error", error)
    except Exception as error:
        print("Unexpected Error", error)    



def execute_statement(cursor, statement, list_of_args=[]):
    try:
        cursor.execute(statement, list_of_args)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError  as error:
        print('Programming Error', error)
    except mariadb.IntegrityError  as error:
        print("Integrtiy Error", error)
    except mariadb.DataError  as error:
        print("Data Error", error)
    except Exception as error:
        print("Unexpected Error", error)

    
def close_connection(cursor):
    conn = cursor.connection
    cursor.close()
    conn.close()