import socket

host = 'localhost' # "127.0.0.1"
port = 14593
filename = "c:\\temp\\shortvideo.mp4";

print(f"TCP file client. Server: ({host}, {port})")

# Source https://docs.python.org/3/howto/sockets.html
# create an INET, STREAMing (TCP) socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#https://docs.python.org/3/library/io.html
file = open(filename, "rb") # rb: read binary
s.sendfile(file)
s.close()