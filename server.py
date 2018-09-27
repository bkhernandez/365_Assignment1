import socket
import argparse
from packet import *

# import pickle
# import os
#
#
# def getFileSize(file):
#     return os.stat(file).st_size


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
            request = (connection.recv(516))
            file = 'new' + request.fileName

            if request.read:
                # read file
                # connection.send(file.encode())
                print('on it')

                fileObject = open(file, 'rb')
                newtempfile = pickle.load(fileObject)

                try:
                    byte = fileObject.read(1)
                    while byte != "":
                        connection.send(byte.encode())
                        byte = fileObject.read(1)

                finally:
                    fileObject.close()

            elif request.write:
                # write to file
                print('umm sure man')
                fileObject = open(file + "new", 'wb')

                # a = pickle.dump(fileObject)
                # fileObject.close()
                # connection.send(a)

                try:
                    byte = bytearray(fileObject.read(1))
                    while byte != "":
                        fileObject.write(byte)
                        byte = bytearray(fileObject.read(1))

                finally:
                    fileObject.close()

            else:
                print("Error: unknown request. \nExiting.")
                exit(1)

        finally:
            connection.close()


main()