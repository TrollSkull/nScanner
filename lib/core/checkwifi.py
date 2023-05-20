from socket import gethostbyname, create_connection, error
from lib.core.exceptions import MyExceptions

def checkwifi(host, port):
    try:
        gethostbyname(host)
        conn = create_connection((host, port), 1)
        conn.close()

    except Exception as error:
        raise MyExceptions(str(error))