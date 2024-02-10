# https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb
import bson

from flask import current_app, g
from flask_pymongo import PyMongo

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient('mongodb+srv://sbuhacks:sbuhacks123@cluster0.jkkkjsb.mongodb.net/?retryWrites=true&w=majority')
db = client.notely

# create
def create_user() -> ObjectId:
    try:
        print('database is ', db.notely.users)
        result = db.users.insert_one({'sessions': []})
        return result.inserted_id
    except Exception as e:
        return e

def create_session(title : str, text_content : str) -> ObjectId:
    try:
        result = db.users.insert_one({'title': title, 'text_content': text_content})
        return result.inserted_id
    except Exception as e:
        return e

# get individual
def get_user(user_id : ObjectId) -> object:
    try:
        return list(db.users.find_one({'_id' : user_id}))
    except Exception as e:
        return e

def get_session(session_id : ObjectId) -> object:
    try:
        return db.sessions.find_one({'_id' : session_id})
    except Exception as e:
        return e

# get sessions
def get_sessions() -> list:
    try:
        return list(db.sessions.find({}))
    except Exception as e:
        return e
    
# # add session to user
# def add_session_to_user(user_id : ObjectId, session_id : ObjectId) -> None:
#     try:
#         session_ids = get_user(user_id)
#         print(session_ids.sessions)
#         return 'hi'
#         # sessions = map(get_session, session_ids)
#         # print('not implemented')
#     except Exception as e:
#         return e
