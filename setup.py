import socket
import threading
import time
import sys

tello_address = ('192.168.10.1', 8889)
local_address = ('', 9000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)
