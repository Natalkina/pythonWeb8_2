import configparser
from mongoengine import *


config = configparser.ConfigParser()
config.read('config.ini')

mongo_url = config.get('DB', 'URI')
connect(host=mongo_url, ssl=True)


class Contact(Document):
    fullname = StringField(max_length=150, required=True)
    email = StringField(max_length=150)
    delivered = BooleanField(default=False)
