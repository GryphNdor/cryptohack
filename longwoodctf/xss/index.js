const http = require('http')

http.createServer((req,res) => {
  res.writeHead(200)
  res.end('test')
}).listen(3000)