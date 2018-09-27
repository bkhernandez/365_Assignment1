import socket
import argparse
import pickle
from packet import *


def main():

    parser = argparse.ArgumentParser(description='Get server info.')
    parser.add_argument('-f', help='file name', type=str)
    parser.add_argument('-a', help='server ip address', type=str)
    parser.add_argument('-p', help='server port number', type=int)
    parser.add_argument('-w', action='store_true', help='write a file')
    parser.add_argument('-r', action='store_true', help='read a file')

    args = vars(parser.parse_args())

    request = Request()

    if args['f']:
        # use as file name
        request.setFileName(args['f'])

    else:
        # error out
        print("No file name provided.")
        exit(1)

    if args['w'] and args['r']:
        # error out
        print("You cannot read and write at the same time. Duh.")
        exit(1)

    elif not(args['w']) and not(args['r']):
        # error out
        print("No read or write operation chosen. Goodbye.")
        exit(1)

    elif args['w']:
        # set write flag to true
        request.setWrite()

    else:
        # set read flag to true
        request.setRead()

    if args['a']:
        # use as hostname
        request.setAddress(args['a'])

    if args['p']:
        # use as port number
        request.setPortNum(args['p'])

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sAddr = (request.address, request.portNum)

    sock.connect(sAddr)
    a = pickle.dumps(request)
    sock.send(a)

    # TODO
    # the guts of the program


main()