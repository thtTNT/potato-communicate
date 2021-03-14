## 安装

```
npm install potato-communicate
```

## 使用

客户端

```javascript
let pc = require("potato-communicate")
let server = new pc.Server(8080) //监听8080端口

//接入客户端
server.on("connection", (client) => {
    
    //接收客户端数据
    client.on("data", (data) => {
        //数据处理
    })

    //发送数据
    client.write({some : "thing"})
})
```

服务端

```javascript
let pc = require("potato-commnunicate")
let client = pc.Client.connect("127.0.0.1", 8080)
client.on("data",(data) => console.log(data)) //接收数据
client.write({some : "thing"}) //使用
```
