import socketio
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

#Start the conection as a Client
sio = socketio.Client()

#Use the hugging models
translation_pipeline = pipeline('translation_en_to_es', model='Helsinki-NLP/opus-mt-en-es')
summarization_pipeline = pipeline('summarization', model='Josmar/BART_Finetuned_CNN_dailymail')

@sio.event
def connect():
    print('connection established')

@sio.on('text-long')
def action(data):
    text = data['message']
    #Set the parameters min and max length to make the summarize
    summarize = summarization_pipeline(text, min_length=40, max_length=80)
    print(summarize[0]['summary_text'])
    #Make the traduction
    results = translation_pipeline(summarize[0]['summary_text'])
    print(results[0]['translation_text'])
    #Emit with the topic 'text-short' the result
    sio.emit('text-short', {'message': results[0]['translation_text']})
    
@sio.event
def disconnect():
    print('disconnected from server')
    sio.disconnect()

#Connected to the port 3000
sio.connect('http://localhost:3000')
sio.wait()