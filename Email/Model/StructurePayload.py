import json, boto3
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from decouple import config
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from decouple import config
from email.mime.multipart import MIMEMultipart

def structurePayload(event):
    # previous_conversation_str = event["Body"]["chatConversation"][-1]["data"]["content"]
    previous_conversation_str = event["Body"].get("previousConversation")
    
    # Check if previous conversation exists
    if previous_conversation_str == "":
       print("=======================================================")
       conversation = {
            "chatConversation": [
            {
                "order": 1,
                "role": "user",
                "meta": {
                    "name": "Service Help Desk AI BOT",
                    "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                },
                "data": {
                    "contentType": "txt",
                    "content":  format_message(event["Body"].get("body"))
                },
                
            }
        ],
        "metaData": {
            "userData": {
                "userEmail":  event["Body"].get("from"),
                "user_name" : event["Body"].get("userName")
            },
            "intent": "",
            "conversationID": 0,
            "entities": {}
        }
    }
       return conversation
    
    try:
        # previous_conversation =previous_conversation_str.json()
        # previous_conversation = previous_conversation_str
        previous_conversation = json.loads(previous_conversation_str)
    except Exception as e:
        print("Error: Unable to parse previous conversation as JSON." , str(e))
        return False
    
    chat_conversation = previous_conversation.get("chatConversation", [])
    last_message = chat_conversation[-1]
    print(last_message, "lastammmm")
    
    duplicated_message = {
        "order": last_message["order"] + 1,
        "role": "user",
        "meta": {
            **last_message["meta"],
            "timeStamp": datetime.now().isoformat(),
        },
        
        "data": {
            **last_message["data"],
            "content": event["Body"].get("body"),
            "contentType": "txt",
        },
    }
    
    if duplicated_message["data"]["contentType"] in ["chcs", "multchcs", "dropdwn", "btn"]:
        for choice in duplicated_message["data"]["content"]:
            choice["selected"] = choice["options"] == event["Body"].get("body")
    
    chat_conversation.append(duplicated_message)
    
    print(previous_conversation, "message")
    return previous_conversation








def format_message(message):
    # message = "i need to change the value now\r\n . This is very important now\r\n________________________________\r\nFrom: lumirasupport@avatest.in <lumirasupport@avatest.in>\r\nSent: 03 April 2024 22:31\r\nTo: Nikil Edwin <nikiledwin@avatest.in>\r\nSubject: Re:regarding issues\r\n\r\nThanks for reaching Lumira sup"
    
    # Check if "\r\n" exists in the string
    if "\r\n" in message:
        # Split the string based on "\r\n" and take the substring before the first occurrence
        message = message.split("\r\n____", 1)[0]
        final = message.replace("\r\n", "")
        return final
    else:
        return message
    
def send_mail(response , event):
    print("came here i think so" , response)
    email_event = event
    
    chat_conversation = response.get("chatConversation", [])
    message_contents = []
    prev_role = None
    user_role_found = False

    # Iterate from the end of the list
    for message in reversed(chat_conversation):
        role = message['role']
        content = message['data']['content']
        content_type = message['data']['contentType']

        if role == 'bot':
            if prev_role == 'bot' or prev_role is None:
                if content_type == 'txt':
                    message_contents.append(content)
                if content_type == 'btn':
                    message = content[0]['options'] + " or " + content[1]['options']
                    message_contents.append(message)
                if content_type == 'crd':
                    print("\n\n\n\n\n\n\n valeu" , content[0]['number'])
                    value = format_incident_message(content[0]['number'])
                    message_contents.append(value)
            else:
                # When the role changes from 'user' to 'bot', break the loop
                break
        elif role == 'user':
            user_role_found = True
            # When the role is 'user', break the loop
            break
        prev_role = role

    # Reverse the list to get the contents in the correct order
    message_contents.reverse()

    if user_role_found:
        user_content = " ".join(message_contents)
        print("User Content:", user_content)

    
    
    output = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Thanks for reaching Lumira support</title>
        </head>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0;">
            <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td style="padding: 20px 0; text-align: center; background-color: #87CEEB;">
                        <h1>Thanks for reaching Lumira support</h1>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 20px;">
                        <p>Hi,</p>
                        <p>{user_content}</p>
                        <p>Thanks & Regards,</p>
                        <p>Team Lumira</p>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
    
      
    
    try :
        
        smtp_username = "AKIATCKAO2OVEZVYXKUR"
        smtp_password = "BO8EvtrxIunFxoAEnXmShhPc8mSjkbJLNvg0ZoG2iAFK"
        recipient_email = email_event['body']['from']
        # recipient_email = "lumirasupport@avatest.in"
        recipient_email_CC = ''
        subject = f"Re:{email_event['body']['subject']}" # Include "Re:" to indicate it's a reply
        body = output
        smtp_server = "email-smtp.us-east-1.amazonaws.com"
        smtp_port = 587

        # Assuming you have received an email and extracted the conversation ID
        # received_conversation_id = "AAQkADk2NmJmZDY0LWEzN2ItNGFmNy1hZDg3LTAzNTBjMWQxN2Y5MgAQAO9R0pS2PGxAmxm52eNoKzo="  # Replace with the actual conversation ID
        received_conversation_id=email_event['body']['threadID']

        # Create a reply message
        reply_message = MIMEMultipart()
        sender_email = email_event['body']['to']
        reply_message["From"] = sender_email
        reply_message["To"] = recipient_email
        reply_message['CC'] = recipient_email_CC
        
        metadata = {
            "X-previous-conversation-Metadata": response,
        }
        for key, value in metadata.items():
            reply_message[key] = str(value)
        reply_message["Subject"] = subject
        reply_message["X-Conversation-ID"] = received_conversation_id
        reply_message["In-Reply-To"] = f"<{received_conversation_id}@example.com>"  # Use a unique identifier

        reply_message.attach(MIMEText(body, 'html'))

        # Connect to the SMTP server and send the reply
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email.split(',') + [recipient_email_CC], reply_message.as_string())
        server.quit()
        print("Email sent successfully")

    except Exception as e:
        print(e,"error")
        
        
        
def findIntentofSuccess(payload):
    print(payload,"ulla vanthuten")
    print( payload['chatConversation'][-1]['data']['content']," payload['chatConversation'][-1]['content']")
    input_value = payload['chatConversation'][-1]['data']['content']
    print(input_value,"inputvauee")
    boto3_bedrock = boto3.client(
                'bedrock-runtime',
                aws_access_key_id=config("ACCESS_KEY_ID"),
                aws_secret_access_key=config("SECRET_ACCESS_KEY"),
                region_name = 'us-east-1'
            )
    
    
    Reponse_llm = Bedrock(
    model_id="anthropic.claude-v2:1",
    client=boto3_bedrock,
)
    
    template = """ """
    prompt = PromptTemplate(template=template , input_variables=["input_value"])

    llm = LLMChain(
        llm=Reponse_llm,    
        prompt=prompt,
    )


    response = llm({"input_value": input_value})
    print(json.loads(response['text']),"resss")
    return json.loads(response['text'])


def format_incident_message(incident_data):
    message = "<html><body>"
    for key, value in incident_data.items():
        if key == 'caller_id':
            message += "<p><strong>{}</strong>: {}</p>".format(key.capitalize().replace('_', ' '), value['value'])
            if 'link' in value:
                message += "<p><strong>Link</strong>: {}</p>".format(value['link'])
        else:
            message += "<p><strong>{}</strong>: {}</p>".format(key.capitalize().replace('_', ' '), value)
    message += "</body></html>"
    return message