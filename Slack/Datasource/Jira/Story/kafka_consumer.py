import json
from confluent_kafka import Consumer, KafkaError
from datetime import datetime
from convert_embeddings import get_embeddings
# from initial_kb_insertion import insertKb
from data_insert_update import check_id
from Services.apiCall import postRequest,getRequest
from flask import Flask
import threading
import os
import dotenv
dotenv.load_dotenv()

app = Flask(__name__)

# Kafka Consumer Configuration
kafka_conf = {
    'bootstrap.servers' :'pkc-921jm.us-east-2.aws.confluent.cloud:9092',
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username' : os.getenv("SASL_USERNAME"),
    'sasl.password': os.getenv('SASL_PASSWORD'),
    'session.timeout.ms':'45000',
    'group.id': 'test454',
    'auto.offset.reset': 'earliest'
}


# This function helps to consume jira issues using kafka consumer
def jira_story_consume_messages():
    

    # consumer = postRequest("https://d29ud6r7hzf0hf.cloudfront.net/kafka_consumer",{},{"group_id":'prefix_name_e37f5f90-3831-41f6-943c-dd5e2a24b430.Issues'})
    # consumer.subscribe(['prefix_name_e37f5f90-3831-41f6-943c-dd5e2a24b430.Issues'])
    consumer = Consumer(kafka_conf)
    print(consumer,"consumer for kafka")
    consumer.subscribe(['jira_story_issues']) 
    issues = []
    count  = 0
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Reached the end of the partition
                    print('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
                elif msg.error().code() != KafkaError.NO_ERROR:
                    # Any error other than end of partition
                    print(msg.error())
            else:
                # Successful message consumption
                message_value = msg.value().decode('utf-8') 
                try:
                    print("inside data extraction")
                    message_json = json.loads(message_value)
                    print(message_json,"llllll")
                    
                    # Extracting required fields from message_jsons
                    initial_created_date = message_json["data"]["fields"].get("created", "na") if message_json["data"]["fields"].get("created") or message_json["data"]["fields"].get("created") == "" else "na"
                    timestamp = initial_created_date / 1000  
                    dt_object = datetime.fromtimestamp(timestamp)
                    created_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                    # Formating the received issues from kafka consumer 
                    print(message_json["data"]["fields"]["issuetype"]["name"],"kkkkkk")
                    if message_json["data"]["fields"]["issuetype"]["name"]=="Story":
                        for message_data in message_json["data"]['transitions']:
                            print(message_data,"aaaaa")
                            formatted_issues = {
                                "issues_id": int(message_json["data"]["id"]),
                                "labels": message_json["data"]["fields"].get("labels", "na") if message_json["data"]["fields"].get("labels") or message_json["data"]["fields"].get("labels") == "" else "na",
                                "duedate": message_json["data"]["fields"].get("duedate", "na") if message_json["data"]["fields"].get("duedate") or message_json["data"]["fields"].get("duedate") == "" else "na",
                                "issues_link": message_json["data"].get("self", "na") if message_json["data"].get("self") else "na",
                                "issues_type": message_json["data"]["fields"]["issuetype"].get("name", "na") if message_json["data"]["fields"]["issuetype"].get("name") else "na",
                                "application_name": message_json["data"]["fields"]["project"].get("key", "na") if message_json["data"]["fields"]["project"].get("key") else "na",
                                "assigned_to": message_json["data"]["fields"]["assignee"]["displayName"] if message_json["data"]["fields"]["assignee"] and "displayName" in message_json["data"]["fields"]["assignee"] else "na",
                                "description": message_json["data"]["fields"].get("description", "na") if message_json["data"]["fields"].get("description") or message_json["data"]["fields"].get("description") == "" else "na",
                                "project_name": message_json["data"]["fields"]["project"].get("name", "na") if message_json["data"]["fields"]["project"].get("name") else "na",
                                "status": message_json["data"]["fields"]["status"].get("name", "na") if message_json["data"]["fields"]["status"].get("name") else "na",
                                "summary": message_json["data"]["fields"].get("summary", "") if message_json["data"]["fields"].get("summary") or message_json["data"]["fields"].get("summary") == "" else "",
                                "created_date": str(created_date)
                            }
                            count = count + 1
                            print("\n")
                            print(f"{count} formatting completed")
                        # Converting the formated issues into vector embeddings
                            issue_embeddings = get_embeddings(formatted_issues)
                            print(f"embedded successfully {count}")
                            check_id(formatted_issues, issue_embeddings)
                        # insertKb(formatted_issues, issue_embeddings)  # This function helps to insert kb articles (Initial)
                            print("\n")
                            print("\ndb execution complete\n")
                            print("\n")
                except json.JSONDecodeError:
                    print("inside json.JSOnDecoderError exception")
                    print(f"Consumed message (raw): {message_value}")

    except KeyboardInterrupt:
        print("Message consumption stopped by user.")
    finally:
        consumer.close()


if __name__ == '__main__':
    # Start Kafka consumer in a separate thread
    kafka_thread = threading.Thread(target=jira_story_consume_messages)
    kafka_thread.start()

    # Run Flask app
    app.run(port=8080)