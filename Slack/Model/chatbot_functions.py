from Model.output_components import (
    chat_conversation_response,
    txt_response,date_picker,button_obj,
    dropdown

)





def generate_shallow_copy(payload):
    chat_conversation = {**chat_conversation_response}
    txt = {**txt_response}
    chat_conversation.update(
        {
            "order": payload["chatConversation"][-1]["order"] + 1,
            "data": txt,
        }
    )
    return chat_conversation


def handle_success_response_text(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "txt", "content": 
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": success_message,
				"emoji": False
			}
		}
	}}
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_date(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    date_pkr={**date_picker}
    date_pkr["blocks"][0]["text"]["text"]=success_message
    chat_conversation.update(
        {"data": {"contentType": "date", "content": date_pkr}}
    )

    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload






def handle_options(content,text):
    btn_obj={**button_obj}
    btn_obj["blocks"][0]["text"]["text"]=text
    

    result_array = [
    {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": options
        },
        "style": "primary",
        "value": f"{options.lower()}_value"
    }
    for options in content
]
    btn_obj["blocks"][1]["elements"]=result_array
    return btn_obj


def handle_success_response_button(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {
            "data": {"contentType": "btn", "content": handle_options(content,text)},
        }
    )
    payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload



def handle_dropdown_options(content,text):
     drpdwn = {**dropdown}
     dropdown_array= [
    {
        "text": {
            "type": "plain_text",
            "text": f"*plain_text {text}*",
            "emoji": False
        },
        "value": f"value-{index}"
    }
    for index, text in enumerate(content)
]
     drpdwn['blocks'][0]['accessory']['options'] =dropdown_array
     drpdwn['blocks'][0]['text']['text'] =text
     return drpdwn
def handle_success_response_dropdown(text,content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
   
   
    chat_conversation.update(
        {
            "data": {"contentType": "drpdwn", "content": handle_dropdown_options(content,text)},
          
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
    if conversationID:
        payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_multichoice(content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)

    chat_conversation.update(
        {
            "data": {"contentType": "mulchcs", "content": handle_options(content)},

        }
    )
    if conversationID:
        payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_success_response_chcs(content, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)

    chat_conversation.update(
        {
            "data": {"contentType": "chcs", "content": handle_options(content)},
         
        }
    )
    if conversationID:
        payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

def handle_success_response_link(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "link", "content": success_message}}
    )
    if conversationID:
        payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload


def handle_success_response_file(success_message, payload, conversationID=0):
    chat_conversation = generate_shallow_copy(payload)
    chat_conversation.update(
        {"data": {"contentType": "file", "content": success_message}}
    )
    if conversationID:
        payload["metaData"]["conversationID"] = conversationID
    payload["chatConversation"].append(chat_conversation)
    return payload

