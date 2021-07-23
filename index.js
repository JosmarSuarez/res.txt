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

io.on('connection', (socket) => {
    console.log('New conection: ', socket.id);
    
    socket.on('text-long', (data) => {
        io.sockets.emit('text-long', data);
        console.log(data);
    });

    socket.on('text-short', (data) => {
        io.sockets.emit('text-short', data);
        console.log(data);
    })

});