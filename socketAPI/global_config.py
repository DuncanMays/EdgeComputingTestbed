# this file holds configuration settings for that are common accross all hosts on the network

# the port that this protocol will operate on
PROTOCOL_PORT = 12345

# the byte encoding that the system will use to turn strings into buffers that can be sent over a network and vice versa
BYTE_ENCODING = 'UTF-8'

# the size of the chunks the system will split messages up into before sending them accross the wire
PACKET_SIZE = 1024