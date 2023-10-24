import re
import time
from socket import *

"""
   Finds and returns words from a given list that match a query string.
   The query can contain '?' characters that act as wildcards, matching any single character.

   Parameters:
   - query (str): The search string which can contain '?' as wildcards.
   - words (list): A list of words to be searched.

   Returns:
   - str: A comma-separated string of matching words.
   """
def find_matching_words(query,words):
    # Replace any '?' in the query with '.' to convert it to a regex pattern.
    # In regex, '.' matches any single character.
    pattern = query.replace('?','.')

    matching_words =[]

    for word in words:
        # Check if the word's length is the same as the query's length
        # and if it matches the regex pattern.
        # If both conditions are true, add the word to the matching_words list.
        if len(word) == len(query) and re.match(pattern,word):
            matching_words.append(word)

    return ",".join(matching_words)

if __name__ == "__main__":
    # Open 'wordlist.txt' file for reading.
    with open("wordlist.txt",'r') as f:
        # Read each line in the file, strip whitespace, and store in a list.
        words = [line.strip() for line in f]

    # Define the server's address and port.
    server_address =("localhost",12000)

    # Create a new socket using the Internet address family and TCP socket type.
    serverSocket = socket(AF_INET,SOCK_STREAM)

    # Bind the socket to the specified address and port.
    serverSocket.bind(server_address)

    # Allow the server to listen for incoming connections.
    serverSocket.listen()

    # Print a message indicating that the server is ready to receive connections.
    print("server is ready to receive from ", server_address)

    # Wait for a client to connect. Once a connection is established,
    # 'accept' returns a new socket and the address of the client.
    connection, client_address = serverSocket.accept()

    # Manage the established connection.
    with connection:
        # Print a message indicating the details of the connection.
        print("Server connected to",client_address,"on",time.ctime(time.time()))

        # Receive data from the client. We expect up to 1024 bytes.
        data = connection.recv(1024)
        # Decode the received bytes to a string format.
        query = data.decode()
        # Use the previously defined 'find_matching_words' function to find matching words.
        response = find_matching_words(query,words)
        # Send the response back to the client after encoding it to bytes.
        connection.sendall(response.encode())


