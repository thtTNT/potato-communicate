let pc = require("potato-communicate")

let server = new pc.Server(8080)
// server.on("connection", (client) => {
//     client.write({a:"b"})
// })

let client = pc.Client.connect("127.0.0.1", 2121)
client.on("data",(data) => console.log(data))
