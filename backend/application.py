from flask import Flask, request, render_template, make_response, redirect, jsonify
from db import create_user, get_session

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
    
@application.route('/test', methods=['GET'])
def test_create():
    result = create_user()
    print(result)
    return jsonify({'user_id': str(result)})

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    