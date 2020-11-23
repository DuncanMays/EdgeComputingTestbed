"""Worker"""

import json
import client as client
from local_config import SELF_IP_ADDRESS

def main():
    cl = client.Client()

    cl.send('hi', SELF_IP_ADDRESS)

if __name__ == "__main__":
    main()
