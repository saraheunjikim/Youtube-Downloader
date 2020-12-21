"""
Another interesting project is to make a nice interface through
which you can download youtube videos in different formats and video quality.

1. Ask user what video they want to download
2. Search the youtube video with what user type
3. Download the first video

04/08/2020
Update to:
- Additional option to download the YouTube video as audio file mp3
- GUI
"""
import pytube
import urllib.request
import urllib.parse
import re

class YouTubeDownloader:
    def __init__(self):
        self.subject = self.userInput()
        self.finalURL = self.searchYoutube()
        self.finalURL = self.downloadVideo()

    # Ask user what video they want to download
    def userInput(self):
        print("Please type such as: Chopin Nocturne No 9 op 5")
        subject = input("What video do you want to download in YouTube?")
        return subject

    # Search the youtube video with what user type
    def searchYoutube(self):
        query_string = urllib.parse.urlencode({"search_query": self.subject})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        finalURL = "http://www.youtube.com/watch?v=" + search_results[0]
        return finalURL

    # Download the first video
    def downloadVideo(self):
        youtube = pytube.YouTube(self.finalURL)
        video = youtube.streams.first()
        video.download('C:/Users/Muffin/Downloads')

if __name__ == '__main__':
    youtube_downloader = YouTubeDownloader()
