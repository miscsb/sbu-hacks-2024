from flask import Flask, request, render_template, make_response, redirect, jsonify
import joblib 
import json
import sys

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

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    