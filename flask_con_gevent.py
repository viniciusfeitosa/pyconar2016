from gevent.wsgi import WSGIServer
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
