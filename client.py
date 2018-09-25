import socket
import argparse
import pickle


class TFTPPacket:

    def __init__(self):
        self.address = '127.0.0.1'c
        self.portNum = 5001
        self.read = False
        self.write = False
        self.fileName = ''

    def setAddress(self, add):
        self.address = add

    def setPortNum(self, port):
        self.portNum = port

    def setRead(self):
        self.read = True

    def setWrite(self):
        self.write = True

    def setFileName(self, name):
        self.fileName = name


def main():

    parser = argparse.ArgumentParser(description='Get server info.')
    parser.add_argument('-f', help='file name', type=str)
    parser.add_argument('-a', help='server ip address', type=str)
    parser.add_argument('-p', help='server port number', type=int)
    parser.add_argument('-w', action='store_true', help='write a file')
    parser.add_argument('-r', action='store_true', help='read a file')

    args = vars(parser.parse_args())

    packet = TFTPPacket()

    if args['f']:
        # use as file name
        packet.setFileName(args['f'])

    else:
        # error out
        print("No file name provided.")
        exit(1)

    if args['w'] and args['r']:
        # error out
        print("You cannot read and write at the same time. Duh.")
        exit(1)

    elif args['w']:
        # set write flag to true
        packet.setWrite()

    else:
        # set read flag to true
        packet.setRead()

    if args['a']:
        # use as hostname
        packet.setAddress(args['a'])

    if args['p']:
        # use as port number
        portNum = args['p']

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sAddr = (packet.address, packet.portNum)

    sock.connect(sAddr)

    # the guts of the program


main()