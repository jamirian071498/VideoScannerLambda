import json
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
	print(event)

	query = event['queryStringParameters']['query']
	vid_id = event['queryStringParameters']['vid_id']

	print('query: {}'.format(query))
	print('vid_id: {}'.format(vid_id))

	timestamps = []

	try:
		transcript_data = YouTubeTranscriptApi.get_transcript(vid_id)

		for caption in transcript_data:
			if query in caption['text']:
				timestamps.append(caption['start'])
	except:
		print(err)

	result = {
		'statusCode': 200,
		'headers': { 
			'Access-Control-Allow-Origin': '*'
		},
		'body': json.dumps(timestamps)
	}

	print(result)

	return result
