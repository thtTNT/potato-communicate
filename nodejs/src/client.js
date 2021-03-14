let net = require("net")
let converter = require("./converter")

class Client {

    static connect(address, port) {
        let client = new Client()
        client.socket = new net.Socket()
        client.socket.connect(port, address)
        client.socket.setEncoding("utf-8")

        client.init()
        return client;
    }

    static fromSocket(socket) {
        let client = new Client()
        client.socket = socket

        client.init()
        return client
    }

    cache = ""

    init() {
        this.events = {
            "data": (object) => {
            }
        }

        this.socket.on("data", (chunk) => {
            let data = chunk.toString();
            for (let chr of data) {
                if (chr === "\n") {
                    let object = converter.fromPCO(this.cache)
                    this.events["data"](object)
                    this.cache = ""
                }
                this.cache += chr;
            }
        })
    }

    on(name, executor) {
        this.events[name] = executor
    }

    write(object) {
        this.socket.write(converter.toPCO(object))
    }

}

module.exports = Client
