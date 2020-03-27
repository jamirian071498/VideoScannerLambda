import json
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
	query = event['queryStringParameters']['query']
	vid_id = event['queryStringParameters']['vid_id']

	print('query: {}'.format(query))
	print('vid_id: {}'.format(vid_id))

	timestamps = []

	try:
		transcript_data = YouTubeTranscriptApi.get_transcript(vid_id)

		for caption in transcript_data:
			if 'text' in caption and 'start' in caption and query in caption['text']:
				timestamps.append(caption['start'])
	except:
		print("An error occured during lambda execution")

	response = {
		'statusCode': 200,
		'headers': { 
			'Access-Control-Allow-Origin': '*'
		},
		'body': json.dumps(timestamps)
	}

	print(response)
	return response
