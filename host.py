import socket

def get_host():
    return socket.gethostname()

host = get_host()
port = 5000
