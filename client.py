from socket import *

def query_client(query):
    #define the server address and port
    server_address = ("localhost",12000)

    #create socket
    clientSocket = socket(AF_INET,SOCK_STREAM)

    #connet server

    clientSocket.connect(server_address)

    #send data to server via TCP
    clientSocket.sendall(query.encode())

    #recieve data from server
    data = clientSocket.recv(1024)

    return data.decode()


if __name__ == '__main__':
    #input query
    query = input("Please type in the word you want search：")


    response = query_client(query)

    # if found response print the response
    if response:
        print("Result found:", response)
    # if not response result not found
    else:
        print("result not found")




