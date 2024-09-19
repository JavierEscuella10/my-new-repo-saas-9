#import_statements

from Services.apiCall import postRequest,getRequest,postRequestWithEncode
from Model.chatbot_functions import handle_success_response_dropdown, handle_success_response_text,handle_success_response_button,handle_success_response_card,process_functions,handle_success_response_multichoice,handle_success_response_date,handle_success_response_options
                  
from testfullnodesanddatasource.AI_helper.testfullnodesanddatasourcellm import LLM_call

from testfullnodesanddatasource.Repo.testfullnodesanddatasource_postgresVector import vector_db

from Workflows.testfullnodesanddatasource.Repo.testfullnodesanddatasource_db import DB_access
from Workflows.testfullnodesanddatasource.Repo.testfullnodesanddatasource_db import DB
#import_here



def testfullnodesanddatasource_intent(payload):
    try:
        conversationId = payload["metaData"]["conversationID"]
        #language_response = getLanguage(payload["chatConversation"][-1]["data"]["content"])
        payload["chatConversation"][-1]["data"]["content"]=language_response
        result = process_functions(
            [function_0,function_1,function_3,function_4,function_5], conversationId, payload
        )
        return result
    except Exception as e:
        return "An Unexpected error occurred. Please try again later."                    
                    
def function_0(payload):
 userPrompt=payload["Chatconversation"][-1]["data"]["content"]
 payload=handle_success_response_text("Welcome to the superdesk!", payload, 1)
 return payload

def function_2(payload):
 userPrompt=payload["Chatconversation"][-1]["data"]["content"]
 payload=handle_success_response_options("Do you want to improve the response",["yes", "no"], payload, 2)
 if(" user choice"=="yes"):
  db_query='select * from sub'
  db_variables=["user_details"]
  db_response=DB_access(db_query,db_variables)
  GET_API_body = {"fetch":fetch_value"}
  GET_API_header={'"authorization"': '"WEIFN12IN"'}
  GET_API_response = getRequest('/get_details', GET_API_header)
  fetch = GET_API_response['value']
  payload=handle_success_response_dropdown("see the listed values",values, payload, 3)
  payload=handle_success_response_date("provide your date of access", payload, 3)
 if(" user choice"=="yes"):
  payload=handle_success_response_text("Enter your requirement", payload, 2)
  llm_response = LLM_call(userPrompt)
  response = llm_response['choice']
  vb_response =vector_db(userPrompt)
  userrequest= vb_response['response']
 return payload

def function_3(payload):
 userPrompt=payload["Chatconversation"][-1]["data"]["content"]
 for k in range(len(arr)):
         print(arr)
  variables_access
   payload=handle_success_response_text("thank you for using superdesk", payload, End)
 return payload

def function_1(payload):
 userPrompt=payload["Chatconversation"][-1]["data"]["content"]
 payload=handle_success_response_text("Enter your username", payload, 1)
 payload=handle_success_response_multichoice("select any of the choice",["yes", "no", "default"], payload, 2)
 API_call_body = {"name":"usercheck"}
 API_call_header={'"authorization"': '"FINOINWDN113"'}
 API_call_response = postRequest('/insert',API_call_body, API_call_header)
 user = API_call_response['action']
 db_query='INSERT INTO sub VALUES(s_id,s_name) VALUES (%s,%s)'
 db_variables=["userdetails"]
 db_response=DB(db_query,db_variables)

  payload=handle_success_response_text("Thank you for using Superdesk!", payload, 0)
 return payload

def function_End(payload):
 userPrompt=payload["Chatconversation"][-1]["data"]["content"]
 payload=handle_success_response_button("select any of the choices",choices, payload, 3)
 payload=handle_success_response_multichoice("select any of the choices",field, payload, 1)
 return payload

