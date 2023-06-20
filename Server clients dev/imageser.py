import socket

def receive_image(save_path, ip, port):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP address and port
    s.bind((ip, port))

    # Listen for incoming connections
    s.listen(1)
    print("Server is listening for incoming connections...")

    # Accept a client connection
    conn, addr = s.accept()
    print("Connected to client:", addr)

    # Receive the image size as a 4-byte length prefix
    image_size_bytes = conn.recv(4)
    image_size = int.from_bytes(image_size_bytes, 'big')

    # Receive the image data
    received_data = b''
    while len(received_data) < image_size:
        data = conn.recv(image_size - len(received_data))
        received_data += data

    # Save the received image to file
    with open(save_path, 'wb') as file:
        file.write(received_data)