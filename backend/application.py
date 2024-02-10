from flask import Flask, abort, request, render_template, make_response, redirect, jsonify
import joblib 
import json
import sys
from db import create_user, get_session
from bson.objectid import ObjectId

application = Flask(__name__)

@application.route('/sessions', methods=['GET', 'POST'])
def processSession():
    if request.method == "POST":
        
        payloadType = request.headers.get('Content-Type')
        if (payloadType == 'application/json'):

            data = request.get_json() 
            return jsonify(data)

    if request.method == "GET":
        return 'This is a GET request test'
        data = request.get_json() 
    return 'TEST RETURN AMOUNT'''
    
@application.route('/users', methods=['POST'])
def prcoess_create_user():
    result = create_user()
    print(result)
    if isinstance(result, ObjectId):
        return jsonify({'user_id': str(result)})
    else:
        return abort(401, 'Could not create user.')

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    