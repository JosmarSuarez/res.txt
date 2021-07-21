const  path = require('path')
const express = require('express');
const app = express();

//sett
app.set('port', process.env.PORT || 3000)

//static files
app.use(express.static(path.join(__dirname, 'public')));

//start the server
const server = app.listen(app.get('port'), () => {
    console.log('server on port', app.get('port'));
})

//Socket.io
const SocketIO = require('socket.io');
const io = SocketIO(server);