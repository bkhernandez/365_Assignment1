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