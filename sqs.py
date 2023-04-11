import boto3
import json
import os
def create_sns_topic(topic_name, email_address):
    sns = boto3.client('sns')
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    sns.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email_address
    )
    return topic_arn
def send_sns_message():
    with open('config.json') as f:
        config = json.load(f)
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn=create_sns_topic(config['topic_name'], 'sahithi.bade12@gmail.com'),
        Message=config['message_body']
    )
    return response['MessageId']
if __name__ == '__main__':
    send_sns_message()

