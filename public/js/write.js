const socket = io()

//DOM elements
let message = document.getElementById('message');
let btn = document.getElementById('send');
let output = document.getElementById('output');

btn.addEventListener('click', function() {
    socket.emit('text-long', {
        message : message.value,
    });
    output.innerHTML = '';
});

socket.on('text-short', function(data) {
    console.log(data.message);
    output.innerHTML = data.message;
});