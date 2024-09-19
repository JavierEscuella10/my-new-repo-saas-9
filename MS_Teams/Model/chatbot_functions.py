from Model.output_components import (
    chat_conversation_response,
    txt_response,
    adaptive_card,radio_obj
)





def generate_shallow_copy(payload):
    chat_conversation = {**chat_conversation_response}
    text = {**txt_response}
    chat_conversation.update(
        {
            "order": payload["chatConversation"][-1]["order"] + 1,
            "data": text,
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


def handle_success_response_card(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    adapt_crd={**adaptive_card}
    adapt_crd["body"]=[success_message]
    chat_conversation.update(
        {"data": {"contentType": "crd", "content":adapt_crd }}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_buttons(content):
    result_array = [
        {"type":"Action.Submit","title": option.capitalize(),  "data": {
                                "action": option.capitalize()
                            }} for option in content
    ]
    return result_array

def handle_success_response_button(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    adapt_crd={**adaptive_card}
    adapt_crd["body"]=[{ 

"type": "TextBlock", 

"text": text, 

"wrap": True, 

"style": "heading" 

} ]
    adaptive_card["actions"]=handle_buttons(content)
    chat_conversation.update(
        {
            "data": {"contentType": "btn", "content": adapt_crd},
        }
    )


    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_success_response_chcs(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)

    chat_conversation.update(
        {
            "data": {"contentType": "chcs", "content": handle_options(content,text)},
            
        }
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_options(content,text):
    body={**radio_obj}
    adapt_crd={**adaptive_card}
    body["choices"] = [
        {"title": option.capitalize(), "value":  option.capitalize()} for option in content
    ]
    body["label"]=text
    return adapt_crd.update(body)

