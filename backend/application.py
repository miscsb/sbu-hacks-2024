import configparser
import os
from flask import Flask, abort, request, render_template, make_response, redirect, jsonify
from flask_cors import CORS, cross_origin
import joblib 
import json
import sys
from db import add_summary_to_user, create_user, create_summary, get_user, get_summary, get_summaries
from bson.objectid import ObjectId
import openai
import markdown

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

openai_key = config['KEYS']['API_KEY']
openai.api_key = openai_key

# first system message: You are a lecture summarizer. Your job is to provide short and helpful summaries of academic lectures
# first prompt: Summarize this excerpt from an academic lecture in a succinct and concise manner by highlighting the important concepts that a student would find useful when reviewing for homeworks and exams. Remember to keep the summary as short as possible without sacrificing important academic concepts
def openAI_API_Request(text):

    completion = openai.ChatCompletion.create(
        model=
            # "gpt-4-0125-preview", 
            "gpt-3.5-turbo-0125",
            # "gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a student in a lecture."},
            {"role": "user", "content": "Imagine you need to take good notes on a lecture to pass your finals. Really put yourself in the shoes of your average college student here: they don't want to write things about the specific lecture in particular, like specific info about a homework due that week, or stories that the professor tells that don't pertain to the content that may show up on the exam. Don't feel bad if you don't take notes over a long period. At the same time, don't take too many notes: limit yourself to small-medium bullet points and limit redundancy. You will be highlighting only the most crucial concepts that will be useful for studying later, or rather, only things that it would be reasonable to say might be on a final exam for the class. You will recieve the text transcript for an excerpt from a lecture. Please expect errors in the speech recoginition for the transcript: if something doesn't make sense, infer what was meant based on the context. Please take notes for the following excerpt of a lecture:"+'\n'+"~~~"+'\n'+text}
        ]
    )

    # print(completion)
    return completion.choices[0].message['content']

application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route('/summaries/<string:id>', methods=['GET'])
@cross_origin()
def get_specific_summary(id):
    result = get_summary(ObjectId(id))
    print(result)
    if isinstance(result, object):
        result['id'] = str(result['_id'])
        result.pop('_id', None)
        return jsonify(result)
    else:
        abort(404)
        
@application.route('/users/<string:id>', methods=['GET'])
@cross_origin()
def get_specific_user(id):
    result = get_user(ObjectId(id))
    print(result)
    if isinstance(result, object):
        result['id'] = str(result['_id'])
        result.pop('_id', None)
        return jsonify(result)
    else:
        abort(404)
    
@application.route('/summaries', methods=['GET', 'POST'])
@cross_origin()
def process_summary():
    result_for_sammy = ""

    if request.method == "POST":

        # payloadType = request.headers.get('Content-Type')
        # print(payloadType)
        # if (payloadType == 'multipart/form-data'):

        title = request.form['title']
        # print(title)

        inp = str(request.files.get('file').read(), "utf-8")
        data = [x.strip() for x in inp.split("\n")[:-1]]

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
            curr = ""
            while i < len(info) and eval(end)-eval(start)<300:
                curr+=info[i][1]
                i+=1
                if i!=len(info): 
                    curr+=" "
                    end = info[i][0][1]
            result_for_sammy += "# "+start+"-"+end+"\n"
            #print(curr)
            result_for_sammy += openAI_API_Request(curr)+"\n"
            #break
        
        create_summary(title, result_for_sammy)
        
        return jsonify({'result': 'success'})
        
    if request.method == "GET":
        result = get_summaries()
        if isinstance(result, list):
            for summary in result:
                summary['id'] = str(summary['_id'])
                summary.pop('_id', None)
                summary.pop('text_content', None)
        else:
            print('result is', result)
        return jsonify(result)
        
    return "NO TYPE"
    
@application.route('/users', methods=['POST'])
@cross_origin()
def process_create_user():
    result = create_user()
    print(result)
    if isinstance(result, ObjectId):
        return jsonify({'user_id': str(result)})
    else:
        return abort(401, 'Could not create user.')

@application.route('/test', methods=['POST'])
@cross_origin()
def test_thing():
    add_summary_to_user(ObjectId('65c7e44b794484671c72a08c'), ObjectId('65c7e45a794484671c72a08d'))
    return jsonify({})

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    
