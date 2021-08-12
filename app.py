from flask import Flask
import socketio

app = Flask(__name__)
sio = socketio.Client()
sio.connect('http://127.0.0.1:8080')

@sio.event
def connect():
    print('connected to server')

@app.route('/')
def index():
    sio.emit('message', 'test')
    return 'hello world'

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)