from flask import Flask
import pymongo
import os

mongodb_uri = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(mongodb_uri)
db = client.get_default_database()

app = Flask(__name__)
