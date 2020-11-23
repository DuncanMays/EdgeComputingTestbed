"""Manager. Manager policy is defined by the build_response method."""

import json
from messages import Init, Init_Response, Fetch, Fetch_Response, Push, Terminate, Message
import server as srvr

def response_policy(msg_json: str):
    print(msg_json)

def main():
    server = srvr.Server(response_policy)
    server.run()

    """server.run() activates the workflow, and should probably be defined in the manager module.
    We could develop a class for different ML jobs. This would let us provide the job type (specify
    model specs like loss function, model type, optimizer, etc.) and the job structure for workers."""

if __name__ == "__main__":
    main()
