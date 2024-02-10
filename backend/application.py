from flask import Flask, abort, request, render_template, make_response, redirect, jsonify
import joblib 
import json
import sys
from db import create_user, create_summary, get_user, get_summary, get_summaries
from bson.objectid import ObjectId

application = Flask(__name__)

@application.route('/summaries/<string:id>', methods=['GET'])
def get_specific_summary(id):
    result = get_summary(ObjectId(id))
    print(result)
    if isinstance(result, object):
        result['id'] = str(result['_id'])
        del result['_id']
        return jsonify(result)
    else:
        abort(404)
    
@application.route('/summaries', methods=['GET', 'POST'])
def process_summary():

    if request.method == "POST":

        payloadType = request.headers.get('Content-Type')
        print(payloadType)

        #if (payloadType == 'multipart/form-data'):

        title = request.form['title']
        print(title)
        inp = str(request.files.get('file').read(), "utf-8")
        # print(inp[0:200])

        data = [x.strip() for x in inp.split("\n")[:-1]]
        # print(data[0:30])

        x=len(data)
        # print(x)
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
            # print(eval(start),eval(end))
            # print(curr)
        
        summary = "summary"

        print('loop ended')
        print(create_summary(title, summary))
        print('hi')

        return jsonify({'result': 'success'})
        
    if request.method == "GET":
        result = get_summaries()
        for summary in result:
            summary['id'] = str(summary['_id'])
            del summary['_id']
            del summary['text_content']
        return result
        
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
# bence can you create a POST /users/<userid>/summaries route
# where POST with payload summary_id calls `add_summary_to_user(ObjectId(user_id), ObjectId(summary_id))`
# and   GET returns `get_user_summaries(ObjectId(user_id))`

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    