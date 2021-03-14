let net = require("net")
let Client = require("./client")

class Server {

    constructor(port) {
        this.server = net.createServer()
        this.events = {
            connection: () => {}
        }
        this.server.listen(port)

        this.createListener()
    }

    createListener() {
        //监听新连接
        this.server.on("connection", (socket) => {
            this.events["connection"](Client.fromSocket(socket))
        })


    }

    on(name, executor) {
        this.events[name] = executor
    }

}

module.exports = Server

