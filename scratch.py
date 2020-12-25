import urllib.request
import urllib.parse
import re
import requests
from googleapiclient.discovery import build



api_key = 'AIzaSyAI4KllSjqbwCLb1Wg5soAUHE7JtdJK0mI'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(part='snippet', q='Chopin', type='video',
                                maxResults=3)

response = request.execute()

search = {}
search_data = []
for item in response['items']:

    title = item['snippet']['title']
    print(title)
    description = item['snippet']['description']
    video = item['id']['videoId']

    search[title] = {}
    search[title]['description'] = description
    search[title]['videoId'] = video

    search_data.append(search)

print(search_data[0]['Chopin Nocturnes'])









