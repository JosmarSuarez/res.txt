import socketio
from transformers import pipeline

sio = socketio.Client()
#reconnection=True, reconnection_attempts=2, reconnection_delay=0, reconnection_delay_max=0,
#                        randomization_factor=0.1, logger=True
#logger=True, engineio_logger=True, ssl_verify=False

translation_pipeline = pipeline('translation_en_to_es', model='Helsinki-NLP/opus-mt-en-es')

@sio.event
def connect():
    print('connection established')

@sio.on('text-long')
def action(data):
    text = data['message']
    print(text)
    results = translation_pipeline(text)
    print(results[0]['translation_text'])
    sio.emit('text-short', {'message': results[0]['translation_text']})
 
@sio.event
def disconnect():
    print('disconnected from server')
    sio.disconnect()

sio.connect('http://localhost:3000')
sio.wait()