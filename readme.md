# 安装环境
pip install flask
pip install aiohttp
pip install python-socketio
pip install "python-socketio[client]"

# 工程说明
- app.py: flask工程
- server.py：socket.io服务器
- client.py：子客户端，可以放在你的main函数里面

# 修改规则
- app.py：可以在app.py中自定义消息事件，如下所示：
```python
@app.route('/')
def index():
    sio.emit('message', 'test')
    return 'hello world'
```
当在浏览器输入http://localhost:8000时，flask这边会向socket.io服务器转发消息'test'到message主题上
- server.py：在这里修改主题转发规则，如下所示：
```python
@socket_io.on('message')
async def print_message(id, message):
    print("socket id is {}".format(id))
    print(message)
    #enabling two-way communication
    await socket_io.emit('messageclient', "you said {}".format(message))
```
以上代表在收到message主题消息之后，将消息转发到`messageclient`主题上

- client.py：通用客户端消息转发，代码如下
```python
@sio.on('messageclient')
def on_message(data):
    print(data)
```

