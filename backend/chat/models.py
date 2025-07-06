from django.db import models

# Create your models here.




# chat/models.py
from mongoengine import Document, StringField, DateTimeField




from datetime import datetime




class Message(Document):
    sender = StringField(required=True)  # username ou 'bot'
    content = StringField(required=True)
    role = StringField(choices=['user', 'assistant'], required=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'messages'  # nom de la collection Mongo
    }
