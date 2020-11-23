
import json
import client as client

from messages import Join

def main():
    cl = client.Client()

    msg = Join()

    cl.send(json.dumps(msg.__dict__), '192.168.2.42')

if __name__ == "__main__":
    main()
