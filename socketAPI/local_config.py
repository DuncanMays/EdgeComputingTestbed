# this file holds configuration setting that are unique to this host

import socket

def get_own_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        print("there was an error detecting the local host's IP address")
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

SELF_IP_ADDRESS = get_own_ip()

# the socket API seems unwilling to do anything with broadcast addresses, so this might be useless
BROADCAST_ADDRESS = '.'.join(SELF_IP_ADDRESS.split('.')[0:3] + ['255'])