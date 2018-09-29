import socket
import argparse
import pickle
from packet import *
from fileio import *


def main():

    parser = argparse.ArgumentParser(description='Get server info.')
    parser.add_argument('-p', help='port to listen on', type=int)
    parser.add_argument('-a', help='hostname or ip', type=str)

    args = vars(parser.parse_args())

    if args['p']:
        port = args['p']
    else:
        port = 5001

    if args['a']:
        hostName = args['a']
    else:
        hostName = '127.0.0.1'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sAddr = (hostName, port)

    print('Starting server on: ' + hostName + ' on port: ' + str(port) + '.')
    sock.bind(sAddr)
    sock.listen(2)

    while True:
        print('Im wating here...')
        connection, cAddr = sock.accept()

        try:
            print('Connection from: ' + str(cAddr))
            request = b""

            while True:
                packet = connection.recv(516)
                if not packet: break
                request += packet

            unpickledreq = pickle.loads(request)

            if unpickledreq.read:
                sendBack = readFile(unpickledreq)
                connection.sendall(sendBack)

            elif unpickledreq.write:
                # write to file
                sendBack = writeFile(unpickledreq)
                connection.sendall(sendBack)

            else:
                print("Error: unknown request. \nExiting.")
                exit(1)

        finally:
            connection.close()


main()