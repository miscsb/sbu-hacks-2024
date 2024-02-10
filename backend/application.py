from flask import Flask, request, render_template, make_response, redirect, jsonify
import joblib 
import json

print("hello word")

application = Flask(__name__)

@application.route('/api', methods=['POST'])
def predict():

    input_json = request.get_json(force=True) 
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    print ('data from client:', input_json)
    dictToReturn = {'answer':69}
    return jsonify(dictToReturn)

    '''payloadType = request.headers.get('Content-Type')
    if (payloadType == 'application/json'):

        data = request.get_json() 
    
    return 'TEST RETURN AMOUNT'''

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    