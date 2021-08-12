import socketio

sio = socketio.Client()


@sio.on('rev_message')
def on_message(data):
    print(data)

@sio.event
def connect():
    print('connected to server')
    # send_ping()

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')
    
    # sio.wait()
# sio.connect('http://127.0.0.1:8080')
