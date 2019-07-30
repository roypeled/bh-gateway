import SimpleHTTPServer
import SocketServer
import sys

PORT = 9090

if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1], 10)
    except:
        print "Supplied port is not a number:", sys.argv[1]



Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Serving at port", PORT

httpd.serve_forever()
