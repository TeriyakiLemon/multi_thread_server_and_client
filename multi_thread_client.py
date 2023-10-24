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
    # Keep prompting the user for input until they decide to quit.
    while True:
        query = input("Please type in the words you want search(type quit for quit)：")
        # If the user types in "quit" (case-insensitive), exit the loop.
        if query.lower() == "quit":
            break

            # Call the 'query_client' function with the user's input and store the response.
            # Note: 'query_client' seems to be a function that hasn't been provided, but it likely
            # sends the query to a server and gets a response.
        response = query_client(query)
        # If the response is not empty or None, display the found results.
        if response:
            print("Result found:", response)
        # If the response is empty or None, inform the user that no results were found.
        else:
            print("result not found")