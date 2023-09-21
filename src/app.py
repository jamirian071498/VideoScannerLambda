import json
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
    if 'path' in event and event['path'] == 'ping':
        response = {
            'statusCode': 200
        }
        return response

    if 'query' not in event['queryStringParameters'] or 'vid_id' not in event['queryStringParameters']:
        response = {
            'statusCode': 200,
            'body': 'Query params not specified'
        }
        print(response)
        return response
    
    query_lower = event['queryStringParameters']['query'].lower()
    query_upper = ''

    if len(query_lower) == 1:
        query_upper = query_lower.upper()
    else:
        query_upper = query_lower[0].upper() + query_lower[1:]

    vid_id = event['queryStringParameters']['vid_id']

    timestamps = []

    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(vid_id)
    except:
        response = {
            'statusCode': 200,
            'headers': { 
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({"no_captions": "true"})
        }

        print(response)
        return response

    for caption in transcript_data:
        if 'text' in caption and 'start' in caption and (query_lower in caption['text'] or query_upper in caption['text']):
            timestamps.append(caption['start'])

    response = {
        'statusCode': 200,
        'headers': { 
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(timestamps)
    }
    return response
