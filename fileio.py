from packet import *
import pickle

# if request.read:
#
#     itemRecv = sock.recv(516)
#     file = request.fileName
#     fileObject = open(file, 'rb')
#     item = b''
#
#     while byte:
#         item += byte
#         byte = fileObject.read(1)
#
#     response = pickle.loads(item)
#
#     print(response)


def readFile(file):
    """
    Broke this out of client and server due to the DRY principle. I had essientally the same code being done in both.  
    """""

    print('Starting to read...')
    toReadFile = file.fileName
    fileObject = open(toReadFile, 'rb')

    try:
        item = b''
        byte = fileObject.read(1)
        while byte:
            item += byte
            byte = fileObject.read(1)

        itemToSend = pickle.dumps(item)

        return itemToSend

    finally:
        fileObject.close()

def writeFile(file):

    print('Starting to write...')
    toWriteFile = file.fileName
    fileObject = open("new" + file, 'wb')

    try:
        byte = bytearray(fileObject.read(1))
        while byte != "":
            fileObject.write(byte)
            byte = bytearray(fileObject.read(1))
# if request.write:
#     # dooo stuff
#     pass
