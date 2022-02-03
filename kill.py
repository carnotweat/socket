import socket
import SimpleHTTPServer
import SocketServer
# import os # uncomment if you want to change directories within the program

PORT = 8000

# Absolutely essential!  This ensures that socket resuse is setup BEFORE
# it is bound.  Will avoid the TIME_WAIT issue

class MyTCPServer(SocketServer.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = MyTCPServer(("", PORT), Handler)

# os.chdir("/My/Webpages/Live/here.html")

httpd.serve_forever()

# httpd.shutdown() # If you want to programmatically shut off the server
