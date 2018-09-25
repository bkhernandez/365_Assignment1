import socket
import argparse
import pickle


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
        hostName = 'localhost'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sAddr = (hostName, port)

    print('Starting server on %s on port %s' % sAddr)
    sock.bind(sAddr)
    sock.listen(2)

    while True:
        print("Im wating here...")
        connection, cAddr = sock.accept()

        try:
            print("Connection from: %s" % cAddr)
            request = (connection.recv(1024)).decode()

            if request.read:
                # read file
                # connection.send(file.encode())
                print('on it')
                fileObject = open(file, 'rb')

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

                a = pickle.dump(fileObject)
                fileObject.close()
                connection.send(a)

                # try:
                #     byte = bytearray(fileObject.read(1))
                #     while byte != "":
                #         fileObject.write(byte)
                #     byte = bytearray(fileObject.read(1))
                #
                # finally:
                #     fileObject.close()

            else:
                print("Error: unknown request. \nExiting.")
                exit(1)

        finally:
            connection.close()


main()