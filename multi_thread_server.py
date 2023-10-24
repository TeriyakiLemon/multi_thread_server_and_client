import re
import time, _thread as thread
from socket import *

def find_matching_words(query,words):
#same as the single_thread_server
    pattern = query.replace('?','.')

    matching_words =[]

    for word in words:
        if len(word) == len(query) and re.match(pattern,word):
            matching_words.append(word)

    return ",".join(matching_words)

def now():
    return time.ctime(time.time())
    """
    Returns the current time as a formatted string.

    Returns:
    - str: Current time.
    """
def handleClient(connection):
    # Wait for 5 seconds before processing.
    # This could be simulating a delay or making sure that the client's data is fully sent.
    time.sleep(5)
    # Manage the established connection.
    with connection:
        data = connection.recv(1024)
        query = data.decode()
        response = find_matching_words(query,words)
        connection.sendall(response.encode())
    """
    Handle the client's request by waiting for 5 seconds,
    then receiving the query, finding matching words, and sending back the response.

    Parameters:
    - connection (socket): The socket connection to the client.
    """

def dispatcher():
    """
       Initialize a server that listens for incoming connections.
       When a connection is made, it spawns a new thread to handle the client's request.
    """

# Open the 'wordlist.txt' file for reading.
with open("wordlist.txt","r") as f:
    # Declare the 'words' variable as global so it can be accessed outside this function.
       global words
       words = [line.strip() for line in f]

       server_address =("localhost",12000)

       serverSocket = socket(AF_INET, SOCK_STREAM)

       serverSocket.bind(server_address)

       serverSocket.listen()

    # Print a message indicating that the server is ready to receive connections.
       print("server is ready to receive from ", server_address)

    # Keep listening for client connections.
       while True:

           # Wait for a client to connect. Once a connection is established,
           # 'accept' returns a new socket and the address of the client.
           connection, address = serverSocket.accept()

           # Print the details of the connection.
           print('Server connected by', address, end=' ')
           print('at', now())

           # Spawn a new thread to handle the client's request.
           # The 'handleClient' function is passed to the new thread along with the connection object.
           thread.start_new_thread(handleClient, (connection,))

if __name__ == "__main__":
    # Start the server dispatcher.
    dispatcher()


