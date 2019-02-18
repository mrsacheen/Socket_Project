from socket import *
import datetime
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
import socket



while True:
        connectionSocket, addr = serverSocket.accept()
        myHOST = socket.gethostname()
        myIP = socket.gethostbyname(myHOST)
        currentDT = datetime.datetime.now()
        time = (currentDT.strftime("%H:%M:%S"))
        date = (currentDT.strftime("%Y:%m:%d"))
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        if capitalizedSentence == 'W0674908':
            connectionSocket.send("Hi, pleased to meet you.".encode())
            connectionSocket.send(capitalizedSentence.encode())
            print('W0674908 Server: GOT', capitalizedSentence)
        elif capitalizedSentence == 'REQTIME':
                connectionSocket.send(time.encode())
                print('W0674908 Server: GOT', capitalizedSentence)
        elif capitalizedSentence == 'REQDATE':
                        connectionSocket.send(date.encode())
                        print('W0674908 Server: GOT', capitalizedSentence)
        elif capitalizedSentence == 'REQIP':
                                connectionSocket.send(myIP.encode())
                                print('W0674908 Server: GOT', capitalizedSentence)
        elif capitalizedSentence == 'ECHO README':
                                        capitalizedSentence =capitalizedSentence.replace('ECHO','')
                                        connectionSocket.send(capitalizedSentence.encode())
                                        print('W0674908 Server: GOT ECHO')
                                
        #connectionSocket.send(capitalizedSentence.encode())
        #print('W0674908 Server: GOT', capitalizedSentence)
        elif capitalizedSentence == 'BYE':
                                                print('See ya Later')
                                                connectionSocket.close()

