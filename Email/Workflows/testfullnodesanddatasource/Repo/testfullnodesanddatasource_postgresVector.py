from langchain.embeddings import BedrockEmbeddings
from langchain_aws import ChatBedrock
from langchain.chains import RetrievalQA
import  psycopg2, boto3
from langchain_aws import ChatBedrock
from decouple import config
import numpy as np
from pgvector.psycopg2 import register_vector
from langchain_community.chat_models import BedrockChat
from services.database import db_connect



def get_boto3_bedrock():
    return boto3.client(
        "bedrock-runtime",
        aws_access_key_id="AKIAD4TUHE2IIN",
        aws_secret_access_key="OFIEWH9I21IOKF",
        region_name="us-east-1",
    )

# def get_llm(boto3_bedrock):
#     return ChatBedrock(
#         model_id="OIOIHDII9W9",
#         client=boto3_bedrock,
#         region_name="us-east-1",
#     )


def get_embeddings_model(boto3_bedrock):
    return BedrockEmbeddings(
        model_id="INOIHEFPMKSD",
        client=boto3_bedrock,
        region_name="us-east-1",
    )


def get_vector_store(embeddings_model,query):

    try:
        embeddedQuery = embeddings_model.embed_query(query)
        embeddingsArray = np.array(embeddedQuery)
        pgConnection =  db_connect()
        
        cursor = pgConnection.cursor()
        register_vector(cursor)
        cursor.execute("select * from values <=>%s", (embeddingsArray,))
        similarArticles = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        kbArticles = [dict(zip(columns, row)) for row in similarArticles]
        return kbArticles
    except Exception as e:
        print(str(e),'error in fetching from vector db')







def vector db(userQuery):
    try:
        boto3_bedrock = get_boto3_bedrock()
        embeddings_model = get_embeddings_model(boto3_bedrock)
        vector_store = get_vector_store(embeddings_model,userQuery)
        return vector_store
    except Exception as e:
        print(str(e))
        return str(e)