import socketio
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

sio = socketio.Client()

mod_path = #If you have locate the model folder
tokenizer_pre = AutoTokenizer.from_pretrained(mod_path)
model_pre = AutoModelForSeq2SeqLM.from_pretrained(mod_path)

translation_pipeline = pipeline('translation_en_to_es', model='Helsinki-NLP/opus-mt-en-es')
summarization_pipeline = pipeline('summarization', model=model_pre, tokenizer=tokenizer_pre)

@sio.event
def connect():
    print('connection established')

@sio.on('text-long')
def action(data):
    text = data['message']
    summarize = summarization_pipeline(text, min_length=40, max_length=80)
    print(summarize[0]['summary_text'])
    results = translation_pipeline(summarize[0]['summary_text'])
    print(results[0]['translation_text'])
    sio.emit('text-short', {'message': results[0]['translation_text']})
    
@sio.event
def disconnect():
    print('disconnected from server')
    sio.disconnect()

sio.connect('http://localhost:3000')
sio.wait()