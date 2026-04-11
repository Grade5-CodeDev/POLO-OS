!pip install flask flask_socketio flask_wtf flask_sqlalchemy gevent geventwebsocket
from gevent import monkey
monkey.patch_all()
from flask import *
from flask_socketio import *
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
app = Flask(__name__)
socketio = socketIO(app)
db = SQLAlchemy(app)
CSRFProtect(app)

@app.route()
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    server = WSGIServer(("0.0.0.0", 80), app, handler_class=WebSocketHandler)