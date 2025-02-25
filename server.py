from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import rps 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('ping')
def handle_ping():
    emit('pong', {'data': 'Pong!'})

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/match')
def match():
    return render_template('match.html')


if __name__ == '__main__':
    socketio.run(app, port=8001)
