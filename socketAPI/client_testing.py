
import pickle
import client as client

from messages import Join

def main():
    cl = client.Client()

    msg = Join()

    target = '192.168.5.150'
    # target = '127.0.0.1'

    print(cl.send(msg.to_string(), target))

if __name__ == "__main__":
    main()
