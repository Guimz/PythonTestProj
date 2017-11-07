import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World. This is my first AWS python application',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
