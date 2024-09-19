import jwt
import json,request
from decouple import config
from psycopg2 import sql
from datetime import datetime, timedelta
from Validators.processConversation import processConversation
from flask import Flask , request
from flask_cors import CORS
from Datasource.Jira.Epic.kafka_consumer import jira_epic_consumer_message 
  from Datasource.Jira.Story.kafka_consumer import jira_story_consumer_message 
  #import

app =Flask(__name__)
CORS(app)
@app.route('/process_conversation', methods=['POST'])
def process_conversation():
    reqData = request.get_json()
    return processConversation(reqData)







    @app.route('/jira_story_consumer_message', methods=['POST'])
    def process_conversation():
        reqData = request.get_json()
        return jira_story_consumer_message()

    #add_function



    





