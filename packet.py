class Request:

    def __init__(self):
        self.address = '127.0.0.1'
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


class TFTPPacket:

    def __init__(self):
        self.packetType = ''
        self.data = ''
        self.blockNum = 1
        self.ack = True
        self.error = ''

    def setPacketType(self, type):
        """
        opcode  operation
            1     Read request (RRQ)
            2     Write request (WRQ)
            3     Data (DATA)
            4     Acknowledgment (ACK)
            5     Error (ERROR)
        """
        self.packetType = type

    def getPacketType(self):
        return self.packetType

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def incrementSeqNum(self):
        """
        Per the RFC:
        "the first data packet can be sent by Host A with a sequence number of 1."
        "block numbers are consecutive and begin with one."

        Thus  we set the original blockNum to 1 and increment from there.
        """
        self.blockNum = self.blockNum + 1

    def setACKType(self, type):
        """
        Either we get an ACK and thus have a True or we do not and it is False.
        """
        self.ack = type

    def getACKType(self):
        return self.ack

    def setErrorType(self, error):
        """
        Check the error type and set the error message accordingly.
        Implemented for Errors: 1, 5 and 6 others are undefined.
        """
        if error == 1:
            errorCode = " File not found."

        elif error == 5:
            errorCode = " Unknown transfer ID."

        elif error == 6:
            errorCode = " File already exists."

        else:
            errorCode = " Undefined error."

        self.error = str(error) + errorCode

    def getErrorType(self):
        return self.error
