# Written by Duncan Mays - 16djm1@queensu.ca
# created as part of the edge intelligence testbed project for the Edge Computing Research group at Queen's university

import socket
import pickle

from global_config import PROTOCOL_PORT, BYTE_ENCODING, PACKET_SIZE
from local_config import SELF_IP_ADDRESS

"""
    This server module listens on a socket and accepts a callback response_policy which it will call on
any message it receives, after parsing that message into a string.

There are two important functions in this class.

start, as the name suggests, will start a socket for any data throughput.
start is persistent, it will not stop listening after a message has completed.
start will call parse when it detects a message.

recieve will parse the packets of raw bytes in the NIC into a string representation message that was sent
parse is not persistent, ie, it will return control back to start when a message has completed
"""

class Server():
    def __init__(self, response_policy: object):
        self.response_policy = response_policy

        self.ip = SELF_IP_ADDRESS
        
        self.port = PROTOCOL_PORT
        self.encoding = BYTE_ENCODING
        self.packet_size = PACKET_SIZE

    # this method listens on a port (non-persistently) and returns any message sent there
    # non-persistent in the context of this program means that it will stop operating as soon as the message is complete
    def parse(self, conn: socket):
        msg = []
        # is there a better way to do this???
        conn.settimeout(0.5)

        # receives data 1024 bytes at a time
        while True:
            try:
                # reads the NIC's buffer into the variable data
                data = conn.recv(self.packet_size)
                # decodes data into a string and appends it to the list msg
                msg.append(data.decode(encoding=self.encoding))
            except Exception as e:
                # if there is no data in the NIC's buffer, the message is over so break the loop
                break

        # concatenates all the strings in msg into one message
        message = ''.join(msg) # concatenate string

        return message

    # this method listens on a port persistently, meaning it will keep listening after a message ends
    # should it detect anything in the NIC's buffer, it will call parse on it, which will return a string representation of whatever message was sent
    # start will the call response_policy on that string.
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(5)
        print('listening on port '+str(self.port))

        while True:
            # s.accept will return when it detects a connection
            conn, addr = s.accept()

            # parses the data in that connection
            msg = self.parse(conn)

            # calls response policy on the string representation of the message
            response = self.response_policy(msg)

            # response_policy is user-defined, so it may return None.
            # If that is the case, we want the client to still get some confirmation that their message was received
            if(response == None):
                response = '_'

            # the server will now try to send response back to the client, both as confirmation that the message was sent successfully but also to trainsmit possibly useful information
            try:
                # the resonse may not be serializable
                msg = str(pickle.dumps(response))
            except:
                # if the object returned by response policy is not serializable, send this
                print('error in serialization: ', end='')
                print(msg)

                msg = str(pickle.dumps('object returned by response policy is not serializable via pickle'))

            conn.send(msg.encode(encoding=self.encoding))

            # closes the connection
            conn.close()

            # the loop will now repeat to listen for another connection
