# This whole file is very portable! It will work in lots of situations for connecting your app to the DB
# In the real world, the error handling
import dbcreds
import mariadb

# A function that will attempt to connect to the DB
# If anything goes wrong, the error will print and None will be returned
# If everything is fine, the cursor will be returned


def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
                               host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR: ", error)
    except Exception as error:
        print("UNKNOWN ERROR: ", error)

# A function that will attempt to close a cursor and its connection
# If anything goes wrong, the error will print
# If everything is fine, all will be closed


def close_connect(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR: ", error)
    except mariadb.InternalError as error:
        print("INTERNAL ERROR: ", error)
    except Exception as error:
        print("UNKNOWN ERROR: ", error)


# A function that will attempt to run a given statement and list of arguments with a cursor
# If the calling code does not pass a list of args, it defaults to an empty list
# If anything goes wrong, the error will print and None will be retruned
# If everything is fine, all will be closed
def execute_statement(cursor, statement, list_of_args=[]):
    try:
        cursor.execute(statement, list_of_args)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as error:
        print("PROGRAMMING ERROR: ", error)
        return str(error)
    except mariadb.IntegrityError as error:
        print("INTEGRITY ERROR: ", error)
        return str(error)
    except mariadb.DataError as error:
        print("DATA ERROR: ", error)
        return str(error)
    except Exception as error:
        print("UNKNOWN ERROR: ", error)
        return str(error)


def run_statement(statement, list_of_args=[]):
    cursor = connect_db()
    if(cursor == None):
        return "Connection Error"
    results = execute_statement(cursor, statement, list_of_args)
    close_connect(cursor)
    return results
