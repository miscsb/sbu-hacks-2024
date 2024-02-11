# https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb
import configparser
import datetime
import os
import ssl
import bson

from flask import current_app, g
from flask_pymongo import PyMongo

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))
client = MongoClient(config['DB']['CONNECTION_STRING'])
db = client.notely

# create
def create_user() -> ObjectId:
    try:
        result = db.users.insert_one({
            'summaries': [], 
            'created_at': datetime.datetime.now()
        })
        return result.inserted_id
    except Exception as e:
        return e

def create_summary(title : str, text_content : str) -> ObjectId:
    try:
        result = db.summaries.insert_one({
            'title': title, 
            'text_content': text_content, 
            'created_at': datetime.datetime.now()
        })
        return result.inserted_id
    except Exception as e:
        return e

# get individual
def get_user(user_id : ObjectId) -> object:
    try:
        user = db.users.find_one({'_id' : user_id})
        user.pop('created_at', None)
        return user
    except Exception as e:
        return e

def get_summary(summary_id : ObjectId) -> object:
    try:
        summary = db.summaries.find_one({'_id' : summary_id})
        summary.pop('created_at', None)
        return summary
    except Exception as e:
        return e

# get summaries
def get_summaries() -> list:
    try:
        summaries = list(db.summaries.find({}))
        for summary in summaries:
            summary.pop('created_at', None)
        return summaries
    except Exception as e:
        return e
    
def add_summary_to_user(user_id : ObjectId, summary_id : ObjectId):
    try:
        user = get_user(user_id)
        if str(summary_id) not in user['summaries']:
            user['summaries'] += [str(summary_id)]
        db.users.update_one({'_id': user_id}, {'$set': {'summaries': user['summaries']}})
    except Exception as e:
        return e

# update summary
def update_summary(summary_id : ObjectId, text_content : str):
    try:
        print(db.summaries.update_one({'_id': summary_id}, {'$set': {'text_content': text_content}}))
    except Exception as e:
        return e
