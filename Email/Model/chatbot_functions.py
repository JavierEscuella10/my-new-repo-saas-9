from Model.output_components import (
    chat_conversation_response,
    txt_response,
    input_config_response,
)





def generate_shallow_copy(payload):
    chat_conversation = {**chat_conversation_response}
    txt = {**txt_response}
    chat_conversation.update(
        {
            "order": payload["chatConversation"][-1]["order"] + 1,
            "data": txt,
            "inputConfig": input_config_response,
        }
    )
    return chat_conversation


def handle_success_response_text(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "txt", "content": success_message}}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_date(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "date", "content": success_message}}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload



def handle_options(text,content):
    result_array = [
        {"options": option.capitalize(), "selected": None} for option in content
    ]
    return {"text":text,"options":result_array}


def handle_success_response_button(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    input_config = {**input_config_response}
    input_config.update({"disableText": 1})
    chat_conversation.update(
        {
            "data": {"contentType": "btn", "content": handle_options(text,content)},
            "input_config": input_config,
        }
    )

    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_button(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    input_config = {**input_config_response}
    input_config.update({"disableText": 1})
    chat_conversation.update(
        {
            "data": {"contentType": "btn", "content": handle_options(text,content)},
            "input_config": input_config,
        }
    )

    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload



def handle_success_response_card(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "crd", "content": success_message}}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload




def handle_success_response_dropdown(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    input_config = {**input_config_response}
    input_config.update({"disableText": 1})
    chat_conversation.update(
        {
            "data": {"contentType": "drpdwn", "content": handle_options(text,content)},
            "input_config": input_config,
        }
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_multichoice(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    input_config = {**input_config_response}
    input_config.update({"disableText": 1})
    chat_conversation.update(
        {
            "data": {"contentType": "mulchcs", "content": handle_options(text,content)},
            "input_config": input_config,
        }
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_success_response_chcs(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    input_config = {**input_config_response}
    input_config.update({"disableText": 1})
    chat_conversation.update(
        {
            "data": {"contentType": "chcs", "content": handle_options(text,content)},
            "input_config": input_config,
        }
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_success_response_link(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "link", "content": success_message}}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_file(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "file", "content": success_message}}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload



