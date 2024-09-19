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








@app.route('/jira_epic_consumer_message', methods=['POST'])
def process_conversation():
    reqData = request.get_json()
    return jira_epic_consumer_message()




    @app.route('/jira_story_consumer_message', methods=['POST'])
    def process_conversation():
        reqData = request.get_json()
        return jira_story_consumer_message()

    #add_function



    






























































# event_body = {
#     "chatConversation": [
#         {
#             "order": 1,
#             "role": "bot",
#             "meta": {
#                 "name": "Service Help Desk AI BOT",
#                 "timeStamp": "2024-01-08 11:33:21.759713",
#             },
#             "data": {"contentType": "txt", "content": "Hi Esakki Rajan G"},
#             "inputConfig": {
#                 "hiddenText": 0,
#                 "disableText": 0,
#                 "hiddenVoice": 1,
#                 "disableVoice": 1,
#                 "hiddenEmoji": 1,
#                 "disableEmoji": 1,
#                 "hiddenAttachment": 1,
#                 "disableAttachment": 1,
#             },
#         },
#         {
#             "order": 2,
#             "role": "bot",
#             "meta": {
#                 "name": "Service Help Desk AI BOT",
#                 "timeStamp": "2024-01-08 11:33:21.759713",
#             },
#             "data": {"contentType": "txt", "content": "How can i help you?"},
#             "inputConfig": {
#                 "hiddenText": 0,
#                 "disableText": 0,
#                 "hiddenVoice": 1,
#                 "disableVoice": 1,
#                 "hiddenEmoji": 1,
#                 "disableEmoji": 1,
#                 "hiddenAttachment": 1,
#                 "disableAttachment": 1,
#             },
#         },
#         {
#             "order": 3,
#             "role": "user",
#             "meta": {"timeStamp": "2024-01-08T12:12:36.875Z"},
#             "data": {
#                 "contentType": "txt",
#                 "content": "password reset for JamesAnderson@avatest.in",
#             },
#             "inputConfig": {
#                 "hiddenText": 0,
#                 "disableText": 1,
#                 "hiddenVoice": 1,
#                 "disableVoice": 1,
#                 "hiddenEmoji": 1,
#                 "disableEmoji": 1,
#                 "hiddenAttachment": 1,
#                 "disableAttachment": 1,
#             },
#         },
#         {
#             "order": 4,
#             "role": "bot",
#             "meta": {
#                 "name": "Service Help Desk AI BOT",
#                 "timeStamp": "2024-01-08 12:04:29.030210",
#             },
#             "data": {
#                 "contentType": "txt",
#                 "content": "Enter Otp sent to your mobile number",
#             },
#             "inputConfig": {
#                 "hiddenText": 0,
#                 "disableText": 0,
#                 "hiddenVoice": 1,
#                 "disableVoice": 1,
#                 "hiddenEmoji": 1,
#                 "disableEmoji": 1,
#                 "hiddenAttachment": 1,
#                 "disableAttachment": 1,
#             },
#         },
#         {
#             "order": 5,
#             "role": "user",
#             "meta": {
#                 "name": "Service Help Desk AI BOT",
#                 "timeStamp": "2024-01-08 12:04:29.030210",
#             },
#             "data": {"contentType": "txt", "content": "095224"},
#             "inputConfig": {
#                 "hiddenText": 0,
#                 "disableText": 0,
#                 "hiddenVoice": 1,
#                 "disableVoice": 1,
#                 "hiddenEmoji": 1,
#                 "disableEmoji": 1,
#                 "hiddenAttachment": 1,
#                 "disableAttachment": 1,
#             },
#         },
#     ],
#     "metaData": {
#         "userData": {
#             "user_name": "Esakki Rajan G",
#             "userEmail": "JamesAnderson@avatest.in",
#             "organization_id": "577d3e38-3c68-4537-836f-0396b9991e3f",
#             "bot_id": "36e42932-40f7-49b9-b9b6-edd8fa8daca7",
#             "phoneNo": "+916383197783",
#         },
#         "intent": "password_reset",
#         "conversationID": 1,
#         "entities": {"EmailId": "JamesAnderson@avatest.in", "Otp": ""},
#     },
# }
# event = {
#     "resource": "/process_conversation",
#     "headers": {
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyRGV0YWlscyI6IHsiYm90X2lkIjogIjM2ZTQyOTMyLTQwZjctNDliOS1iOWI2LWVkZDhmYThkYWNhNyJ9fQ.Rot0CcsUAj8aYDfKbszCl4YhZhSAcdAVW0pG5zLUPaM",
#         "api-key": "91f3997c2ec2e452",
#     },
#     "body": json.dumps(event_body),
# }



