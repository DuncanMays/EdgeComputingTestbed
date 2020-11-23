"""Worker"""

import json
import client as client

def main():
    cl = client.Client()

    cl.send('this is an arbitrary message', '192.168.2.42')

if __name__ == "__main__":
    main()
