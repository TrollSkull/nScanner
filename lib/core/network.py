from socket import gethostbyname, create_connection

def has_internet_connection(host: str, port: int) -> bool:
    try:
        gethostbyname(host)
        conn = create_connection((host, port), 1)
        conn.close()

    except Exception as _:
        return False
    
    return True