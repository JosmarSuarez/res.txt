const socket = io()

//Get the html's by id
let message = document.getElementById('message');
let btn = document.getElementById('send');
let output = document.getElementById('output');
let load_img = document.getElementById('load_img');

//When click the btn send the 'text-long'
btn.addEventListener('click', function() {
    socket.emit('text-long', {
        message : message.value,
    });
    /* output.innerHTML = ''; */
    load_img.style.display='inline';
});
//Waits the 'text-short' to display in screen
socket.on('text-short', function(data) {
    load_img.style.display='none';
    console.log(data.message);
    output.innerHTML = data.message;
});