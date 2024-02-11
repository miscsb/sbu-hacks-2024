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
import bionic
from gtts import gTTS

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))
openai.api_key = config['OPENAI']['API_KEY']

# first system message: You are a lecture summarizer. Your job is to provide short and helpful summaries of academic lectures
# first prompt: Summarize this excerpt from an academic lecture in a succinct and concise manner by highlighting the important concepts that a student would find useful when reviewing for homeworks and exams. Remember to keep the summary as short as possible without sacrificing important academic concepts
def openAI_API_Request(text):

    completion = openai.ChatCompletion.create(
        model=config['OPENAI']['VERSION'],
        messages=[
            {
                "role": "system", 
                "content": config['PROMPT']['USER']
            },
            {
                "role": "user", 
                "content": config['PROMPT']['SYSTEM'] + '\n~~~\n' + text
            }
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
    if isinstance(result, object):
        result['id'] = str(result['_id'])
        result.pop('_id', None)
        # result['text_content'] = bionic.make_bionic_paragraph(result['text_content'])
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
        def stuff(x):
            x = x.split(":")
            val = ""
            if int(x[0])!=0: val += x[0]+":"
            val+=x[1]+":"
            val+=x[2][:x[2].index(".")]
            return val
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
            print(eval(start),eval(end))
            a =  openAI_API_Request(curr).split("\n")
            a = [a[0]]+["## "+stuff(start)+"-"+stuff(end)+"\n"]+a[1:]
            result_for_sammy+="\n".join(a)+"\n"
            i+=1
            """
            result_for_sammy += "## "+stuff(start)+"-"+stuff(end)+"\n"
            print(eval(start),eval(end),start,end)
            #print(curr)
            result_for_sammy += openAI_API_Request(curr)+"\n"
            """
            #break
        
        '''tts = gTTS(text=result_for_sammy, lang='en', slow=False)
        tts.save("response.mp3")
        os.system("mpg123 response.mp3")'''
        summary_id = create_summary(title, result_for_sammy)
        
        return jsonify({'id': str(summary_id)})
        
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
    
