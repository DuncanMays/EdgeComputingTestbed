
import socket
from global_config import PROTOCOL_PORT, BYTE_ENCODING, PACKET_SIZE

class Client():
    def __init__(self):
        self.port = PROTOCOL_PORT

    # this method simply sends a given string to a given ip address
    def send(self, msg: str, ip_address: str, depth=5):

        # should this method fail to send the data, it will retry at most 5 times
        # this if block stops the method from executing if its depth is less than or equal 0
        if (depth <= 0):
            return 'no connection'

        # establishes a connection with the socket at the opther IP address
        channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        channel.connect((ip_address, self.port))
        
        # sensd the message
        channel.send(msg.encode(encoding=BYTE_ENCODING))

        # now waits for the response
        resp = []
        # is there a better way to do this???
        channel.settimeout(5.0)
        while True: 
            # pulls teh data out of the NIC buffer and decodes it
            data = channel.recv(PACKET_SIZE).decode(encoding=BYTE_ENCODING)

            # if there is no data, the message is complete so stop reading
            if data == '':
                break

            # adds the decoded string to the list resp
            resp.append(data)
        
        # closes the connection
        channel.close()

        # if there was no response, then the message was not sent successfully, and we should retry
        if resp is None:
            return send(msg, ip_address, depth-1)

        # joins the peices of the message together
        response = ''.join(resp)

        return response