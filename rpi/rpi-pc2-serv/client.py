import socket
import time
import picamera

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.connect(('192.168.0.143', 8000))

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.start_preview()
    time.sleep(2)
    camera.start_recording(connection, format='h264')
    while 1:
        continue
finally:
    camera.stop_recording()
    connection.close()
    client_socket.close()
