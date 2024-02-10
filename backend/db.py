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

        result = db.users.insert_one({'summaries': []})
        return result.inserted_id
    except Exception as e:
        return e

def create_summary(title : str, text_content : str) -> ObjectId:
    try:
        print(title, text_content)
        print("70")
        result = db.users.insert_one({'title': title, 'text_content': text_content})
        print(result)
        return result.inserted_id
    except Exception as e:
        print(e)
        return e

# get individual
def get_user(user_id : ObjectId) -> object:
    try:
        return list(db.users.find_one({'_id' : user_id}))
    except Exception as e:
        return e

def get_summary(summary_id : ObjectId) -> object:
    try:
        return db.summaries.find_one({'_id' : summary_id})
    except Exception as e:
        return e

# get summaries
def get_summaries() -> list:
    try:
        return list(db.summaries.find({}))
    except Exception as e:
        return e
    
# # add summary to user
# def add_summary_to_user(user_id : ObjectId, summary_id : ObjectId) -> None:
#     try:
#         summary_ids = get_user(user_id)
#         print(summary_ids.summaries)
#         return 'hi'
#         # summaries = map(get_summary, summary_ids)
#         # print('not implemented')
#     except Exception as e:
#         return e
