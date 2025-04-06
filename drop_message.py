import json
import boto3
import os
import uuid

# Initialize the SQS client
sqs = boto3.client('sqs', region_name='ap-south-1')

# Get the queue URL from environment variables
QUEUE_URL = os.environ.get('QUEUE_URL')

def lambda_handler(event, context):
    # Create the message
    message = {
        'id': '123456',
        'action': 'process_order',
        'data': {
            'customer_id': 'C1000',
            'product_id': 'P2000',
            'quantity': 5,
            'payment_type' : 'mass_payment'
        }
    }
    
    try:
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(message),
            MessageDeduplicationId=str(uuid.uuid4()),
            MessageGroupId='MP'
            
        )
        
        # Log the message ID
        print(f"Message sent to SQS. MessageId: {response['MessageId']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Message sent to queue successfully',
                'messageId': response['MessageId']
            })
        }
    
    except Exception as e:
        print(f"Error sending message to SQS: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error sending message to queue',
                'error': str(e)
            })
        }