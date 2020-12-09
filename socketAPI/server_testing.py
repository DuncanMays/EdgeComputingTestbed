"""Manager. Manager policy is defined by the build_response method."""

import pickle
import server as srvr

def response_policy(msg_json: str):
    print(msg_json)

def main():
    server = srvr.Server(response_policy)
    server.start()

if __name__ == "__main__":
    main()
