import socket
# OpenCensus Dependencies ############################################
import flask

from opencensus.trace.exporters import stackdriver_exporter
from opencensus.trace.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace import tracer as tracer_module

tracer = tracer_module.Tracer()

app = flask.Flask(__name__)

# Enable tracing the requests
middleware = FlaskMiddleware(app)
######################################################################

@app.route('/') ## <-- ? #############################################
s = socket.socket()
host = '' #socket.gethostname()
port = 8888
s.bind((host, port))

s.listen(1)
c = None
q = ''

while True:
    c, addr = s.accept()
    print ("Connection from ", addr)
    print (c.recv(1024))
    q = raw_input("Message: ")
    c.send(q)

######################################################################
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
