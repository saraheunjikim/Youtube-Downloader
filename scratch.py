import urllib.request
import urllib.parse
import re

html = urllib.request.urlopen("http://www.youtube.com/results?search_query=chopin")
print(html.read().decode())