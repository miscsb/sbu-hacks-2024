from flask import Flask, abort, request, render_template, make_response, redirect, jsonify
import joblib 
import json
import sys
from db import create_user, create_session, get_user, get_session, get_sessions
from bson.objectid import ObjectId

application = Flask(__name__)

@application.route('/summaries', methods=['GET', 'POST'])
def ProcessSession():

    # print(request.headers.get('Content-Type'))
    #print(request.form['title'])
    #vtt = request.files['file'].read()
    #print(vtt[0:10])

    payloadType = request.headers.get('Content-Type')
    print(payloadType)

    #if (payloadType == 'multipart/form-data'):

    title = request.form['title']
    print(title)
    inp = request.files['file'].read()
    print(inp[0:50])

    data = inp.split("\n")[:-1]
    x=len(data)
    info = []
    for i in range(1,x,5):
        times = data[i+1].split(" --> ")
        words = data[i+2].split(">")[1]
        info.append([times,words])
    def eval(x):
        curr = [float(x) for x in x.split(":")]
        return curr[0]*3600+curr[1]*60+curr[2]
    i = 0
    while i < len(info):
        start = info[i][0][0]
        end = info[i][0][1]
        curr = info[i][1]
        while i < len(info) and eval(end)-eval(start)<300:
            i+=1
            if i!=len(info): 
                if curr[-1] in "?.": curr+=" "
                curr+=info[i][1]
                end = info[i][0][1]
        print(eval(start),eval(end))
        print(curr)

    if request.method == "POST":

        if (payloadType == 'application/json'):
            # call create_session(title, content) here
            data = request.get_json() 
            return jsonify(data)
            
        return "This is a POST request"
        
    if request.method == "GET":
<<<<<<< HEAD
        return 'This is a GET request'
=======
        # return get_session(ObjectId(session_id)) here
        return 'This is a GET request test'
>>>>>>> be476e364c4c0ebbc06974d07277f5dc5a359d0f
        
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
    