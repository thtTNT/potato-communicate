let fromPCO = function (pco) {
    return JSON.parse(pco)
}

let toPCO = function (object) {
    return JSON.stringify(object)
}

module.exports = {
    fromPCO,
    toPCO
}
