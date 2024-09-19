from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import psycopg2
import json,re
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



def get_boto3_bedrock():
    return boto3.client(
        "",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="",
    )


def get_llm(boto3_bedrock):
    #4.The user query:{query} is based on the general question about jira- give a summarised solution in the key text 
    return BedrockChat(
        model_id="",
        client=boto3_bedrock,
        region_name="",
        model_kwargs={"temperature": 0.7}
    )


def get_llm_interaction(llm, prompt):
    return LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
    )


def call_llm(userPrompt):
    try:
        boto3_bedrock = get_boto3_bedrock()
        llm = get_llm(boto3_bedrock)
        class case_creation_parser(BaseModel):
            intent: str = Field(description="gives wether the user content belong to which category")
            
        case_parser = JsonOutputParser(pydantic_object=case_creation_parser)
        prompt= get_prompt(case_parser)
        case_creation_interaction = prompt | llm | case_parser
       
        response = case_creation_interaction.invoke(
            {"query": userPrompt}
        )
        return response
    except Exception as e:
            print('inexcep',str(e))

def get_prompt():
    template = """  You role is to analyze the user input query based on the instructions mentioned below and respond back the JSON mentioned followingly
        RULE
        1.Return the response in json format {{"intent":"user intent <data type string>"}}
    
        Instructions: 
            1. If the user query is an greeting message respond back with JSON {{"intent":"greeting"}}
            2. If the user query is an general retrival/need/or requesting to fetch question respond with JSON {{"intent":"relevent"}}
            3. If the user query is an irrelevent, like "wertyui45678,dfghjrtyuioor," any unwanted JK question/about subjects it looks like criticism,insult,confrontation, if anything like movie review or cooking tips also consider to be an irrelevent conetnt or similar to this kind respond with JSON {{"intent":"irrelevent"}}
    
        Find the User Input Query: 
        {query}

        <Instruction>
            The most important thing is to check if the input is in English, if not then return intent as 'irrelevent' 
            1.Strictly Analyze the input if the input is not in english language then classify the intent as 'irrelevent' 
            2.Analyze the input if the input is a greeting message then classify the intent as greeting 
            4.Analyze the input if the input is of type general questions like "write a java code or python code" or like "who is owner of google" or like "how to cook biriyani" then classify the intent as 'irrelevnt' 
            4.Analyze the input if the input is an irrelevent, like "wertyui45678,dfghjrtyuioor" it looks like criticism,insult,confrontation or similar to this kind  then classify the intent as 'irrelvent' 
        <Instruction>

            <Examples>
            Example 1:
            Input: ஹாய் எப்படி இருக்கிறீர்கள்/హాయ్ ఎలా ఉన్నారు/हाय आप कैसे हैं/हाय आप कैसे हैंहाय आप कैसे हैं/பொதுவான பிட்லாக்கர் சிக்கல்கள் மற்றும் அவற்றின் தீர்மானங்கள் என்ன?
            Output:{{"intent":"irrelevent"}}
            Description for example 1:since the language of the input in not english so the corresponding output is {{"intent":"irrelevent"}}

            Example 2:
            Input:who is owner of google/write a java code for login/how to cook briyani/what's your favorite fictional universe and why?/how is the movie Ghilli/what are symptoms of fever/how to calculate simple interest/how to add two numbers/who is chief minister/Can you suggest me a hair cut?/ what are steps to get a loan?/how to python code for addition of two number?/code for login in java?
            Description for example 2:since the input type is of general questions so the corresponding output is{{"intent":"irrelevent"}}
            Output:{{"intent":"irrelevent"}}

            Example 3:
            Input:Hi/hello/how are you
            Output:{{"intent":"greeting"}}
            Description for example 3:since the input type is greeting so the corresponding output is {{"intent":"greeting"}}

            Example 4:
            Input:vanakkam/epdi irukinga/mani enna
            Output:{{"intent":"irrelevent"}}
            Description for example 4:since the input type is not a proper english so the corresponding output is {{"intent":"irrelevent"}}
        
        Now analyze the User Input Query and respond back with appropriate response
        Note: Only the JSON must be responded back and no more additional content
        
        RULE:** provide the json key values in double quotes.
       **Don't provide anything like "There is no data for your search/unfortunatly there where no relevant data/based on the input data/Based on the articles provided,
        /based on your query /based on the conversation/the provided information does't contain any information/Based on the provided data, ", Make sure in the summarized response you don't retuen any text 
        like this only the summary you have to return.**
        """
    return PromptTemplate(template=template, input_variables=["query"])
