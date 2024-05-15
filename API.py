import socket
server = "200"

def setup():

    return"Complete"

def server_program():
        # get the hostname
        host = socket.gethostname()
        port = 63254
        server_socket = socket.socket()  # get instance
        server_socket.bind((host, port))  # bind host address and port together
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection


if __name__ == '__main__':
    server_program()