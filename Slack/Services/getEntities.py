import json, boto3
from langchain.llms import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from decouple import config


def getEntity(incident, entity_object, existing_entity):
    user_request = incident
    entities = list(entity_object.keys())
    print(user_request, entities, "got it")
    boto3_bedrock = boto3.client(
        "bedrock-runtime",
        aws_access_key_id=config("ACCESS_KEY"),
        aws_secret_access_key=config("SECRET_ACCESS_KEY"),
        region_name="us-east-1",
    )
    llm = Bedrock(
        model_id=config("BEDROCK_MODEL_ID"),
        client=boto3_bedrock,
        region_name="us-east-1",
    )
    template = """You are an assistant that helps people find information.
      Extract the entities "{entities}" and also consider existing  
      Entity {existing_entity} from the user request "{user_request}"
        and and return them JSON format Please find the sample json Format: {entity_object}
          Note: Expecting property name enclosed in double quotes.,
            without any additional information, details, comments or context. """
    prompt = PromptTemplate(
        template=template,
        input_variables=[
            "user_request",
            "entities",
            "entity_object",
            "existing_entity",
        ],
    )
    llm_interaction = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
    )

    llmResponse = llm_interaction(
        {
            "entities": entities,
            "user_request": user_request,
            "entity_object": entity_object,
            "existing_entity": existing_entity,
        }
    )
    print(llmResponse)
    print("llmResponse")
    replaced_quotes = llmResponse["text"].replace("'", '"')
    print(replaced_quotes, "replaced")
    output = json.loads(replaced_quotes)
    print(output)
    # response_body = json.loads(llmResponse.get("body").read())
    outputText = output
    return outputText
    # res = conn.getresponse()
    # data = res.read()

    # data_dict=json.loads(data.decode("utf-8"))
    # return data_dict["choices"][0]["message"]["content"]
