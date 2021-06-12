import json
import socket
from Tools.mysql_ import *
from _thread import *

def sendToClientMatrix(connection, gt):
    data_bytes = {"status": gt.status, "data": [], "dataMatrix": gt.data, "message": gt.message }

    user_encode_data = json.dumps(data_bytes).encode('utf-8')
    connection.send(user_encode_data)  

def sendToClientData(connection, gt):
    data_bytes = {"status": gt.status, "data": gt.data, "message": gt.message }

    user_encode_data = json.dumps(data_bytes).encode('utf-8')
    connection.send(user_encode_data)


def threaded_client(connection):
    while True:         
        peticion = connection.recv(2048)

        requestClient = peticion.decode()
        my_json = json.loads(requestClient)
            
        if(my_json['action'] == "getFactura"):
            dataFromDB = getFactura()
            sendToClientData(connection, dataFromDB)

        else:
            print("\n\nERROR -----------")

    connection.close()

def server():
    ServerSocket = socket.socket()
    host = 'localhost' # localhost - 127.0.0.1
    port = 8000
    ThreadCount = 0

    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print("Server could not start" + str(e))

    print('\nWaiting for a Connection..\n')

    ServerSocket.listen(5)

    connectDB()

    while True:
        Client, address = ServerSocket.accept()
        start_new_thread(threaded_client, (Client, ))
        ThreadCount += 1
        print( "(" + str(ThreadCount) + ') - New Client - Connected to: ' + address[0] + ':' + str(address[1]))

    ServerSocket.close()
