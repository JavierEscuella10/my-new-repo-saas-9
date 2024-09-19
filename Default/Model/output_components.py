from datetime import datetime

txt_response = {"contentType": "txt", "content": ""}

chat_conversation_response = {
    "order": 1,
    "role": "bot",
    "meta": {
        "name": "Service Help Desk AI BOT",
        "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
    },
    "data": {},
    "inputConfig": {},
}

input_config_response = {
    "hiddenText": 0,
    "disableText": 0,
    "hiddenVoice": 1,
    "disableVoice": 1,
    "hiddenEmoji": 1,
    "disableEmoji": 1,
    "hiddenAttachment": 1,
    "disableAttachment": 1,
}


metadata_response: {
    "userData": {},
    "intent": "",
    "conversationID": "",
    "entities": {},
}

choices: {
    "contentType": "choices",
    "content": "",
    "options": [],
}

choice_options: {"options": "", "selected": False}
