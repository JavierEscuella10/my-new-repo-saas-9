from datetime import datetime

txt_response = {"contentType": "txt", "content": ""}

chat_conversation_response = {
    "order": 1,
    "role": "bot",
    "meta": {
        "name": "Superdesk Bot",
        "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
    },
    "data": {},
    
}


adaptive_card={
                    "type": "AdaptiveCard",
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.5",
                    "body": [
                        
                    ]
                },

radio_obj=[
                        {
                            "type": "Input.ChoiceSet",
                            "id": "Confirmation",
                            "label": "",
                            "isRequired": True,
                            "errorMessage": "Please let us know if you are sure",
                            "style": "expanded",
                            "choices": []
                        }
                    ]