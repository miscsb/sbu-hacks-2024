from flask import Flask, abort, request, render_template, make_response, redirect, jsonify
import joblib 
import json
import sys
from db import create_user, create_session, get_user, get_session, get_sessions
from bson.objectid import ObjectId

application = Flask(__name__)

@application.route('/sessions', methods=['GET', 'POST'])
def process_session():

    if request.method == "POST":
        
        payloadType = request.headers.get('Content-Type')
        if (payloadType == 'application/json'):
            # call create_session(title, content) here
            data = request.get_json() 
            return jsonify(data)

    if request.method == "GET":
        # return get_session(ObjectId(session_id)) here
        return 'This is a GET request test'
        
    return "none"
    
@application.route('/users', methods=['POST'])
def process_create_user():
    result = create_user()
    print(result)
    if isinstance(result, ObjectId):
        return jsonify({'user_id': str(result)})
    else:
        return abort(401, 'Could not create user.')
    
# [when we add users]
# bence can you create a POST /users/<userid>/sessions route
# where POST with payload session_id calls `add_session_to_user(ObjectId(user_id), ObjectId(session_id))`
# and   GET returns `get_user_sessions(ObjectId(user_id))`

@application.route('/test', methods=['POST'])
def test_thing():
    result = get_sessions()
    print(result)
    return jsonify({})

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    