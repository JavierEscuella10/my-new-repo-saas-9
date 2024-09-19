
from Services.findIntent import identify_intent
from Validators.userIntentCheck import call_llm,call_get_greeting
from Services.database import log_error
from Model.chatbot_functions import handle_success_response_text
from Model.output_components import (
    chat_conversation_response,
    txt_response,
    input_config_response,
)

import json

from Workflows.testfullnodesanddatasource.testfullnodesanddatasource import testfullnodesanddatasource_intent



def append_chat_conversation(payload):
    chat_conversation = {**chat_conversation_response}
    txt = {**txt_response}
    txt.update({"content": "Please provide the intent in detail"})
    chat_conversation.update(
        {
            "order": payload["chatConversation"][-1]["order"] + 1,
            "data": txt,
            "inputConfig": input_config_response,
        }
    )

    payload["chatConversation"].append(chat_conversation)
    return payload


def process_intent(payload,intent):
    # process_intent_function
     
 


def processConversation(event):

    try:
        payload = json.loads(event["body"])
        check_user_intent=call_llm(payload["chatConversation"][-1]["data"]["content"])
        if check_user_intent=="greeting":
            greeting_message = call_get_greeting(payload["chatConversation"][-1]["data"]["content"])
            return handle_success_response_text(greeting_message,greeting_message, payload, 0)
        elif check_user_intent=="irrelevent":
            return handle_success_response_text("Sorry, I can't answer this question. Kindly ask a relevant question", payload, 0)
        else:
            if payload["metaData"]["intent"] == "":
                response = identify_intent(
                    payload["chatConversation"][-1]["data"]["content"]
                )
                print(response["sessionState"]["intent"]["name"])
                print("Lex response:", response)
                intent = response["sessionState"]["intent"]["name"]
                payload["metaData"]["intent"] = intent
                payload["metaData"]["conversationID"] = 0
                payload["metaData"]["entities"] = {}
                return process_intent(payload, intent)
            else:
                return process_intent(payload, payload["metaData"]["intent"])

    except Exception as e:
        print(str(e),"process_conversation function")
        log_error("get_intent", "connectLex", str(e))
        





