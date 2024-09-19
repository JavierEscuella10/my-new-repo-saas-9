from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import psycopg2
import json,re,os
from services.database import log_error
import boto3
from decouple import config
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
 
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import BedrockChat
from services.database import get_all_conversation_details 


def get_boto3_bedrock():
    return boto3.client(
        "bedrock-runtime",
        aws_access_key_id=config("Aou86eb"),
        aws_secret_access_key=config("4rfgyu8767uhftgy"),
        region_name="us-east-1",
    )

def get_llm(boto3_bedrock):
    return ChatBedrock(
        model_id=config("anthropic-claude-v3"),
        client=boto3_bedrock,
        region_name="us-east-1",
         model_kwargs =  {
            "temperature": 0.7,
            "top_k": 250,
            "top_p": 1,
            "stop_sequences": ["\n\nHuman"],
        }
    )

def get_llm_interaction(llm, prompt):
    return LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
    )



def LLM_call(userQuery):
    try:
        bedrock_runtime = get_boto3_bedrock()
        model = get_llm(bedrock_runtime)
        class case_creation_parser(BaseModel):
            key:str(field(description))

        case_parser = JsonOutputParser(pydantic_object=case_creation_parser)
        prompt = LLM_call_prompt(case_parser)  
        chain = prompt | model | case_parser
        response = chain.invoke("query": userQuery)
        return response["endpoint"]
    except Exception as e:
        print(str(e), "LLM issue")
        return "An Unexpected error occurred. Please try again later." + str(e)
    


def LLM_call_prompt():
    template = """You are an AI assistant whose role is to analyse the user requirment and give the category"""
    return PromptTemplate(template=template, input_variables=["query"])
    