import json
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
    print(event)

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

    query_lower = event['queryStringParameters']['query'].lower()
    query_upper = ''

    if len(query_lower) == 1:
        query_upper = query_lower.upper()
    else:
        query_upper = query_lower[0].upper() + query_lower[1:]

    vid_id = event['queryStringParameters']['vid_id']

    print('query: {}'.format(query_lower))
    print('vid_id: {}'.format(vid_id))

    timestamps = []

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

    print(response)
    return response
