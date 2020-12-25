import pytube
import tkinter as tk
import tkinter.font as font
from googleapiclient.discovery import build

api_key = '0'


def download():
    keyword = field1.get()
    searchYoutube(keyword)


def searchYoutube(keyword):
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_request = youtube.search().list(part='snippet', q=keyword,
                                           type='video', maxResults=10)
    search_result = search_request.execute()
    search_result = {'kind': 'youtube#searchListResponse', 'etag': 'Ht9pCdmBDrnxDL4fr68iZSW-Ts4',
                     'nextPageToken': 'CAoQAA',
                     'regionCode': 'US', 'pageInfo': {'totalResults': 1000000, 'resultsPerPage': 10}, 'items': [
            {'kind': 'youtube#searchResult', 'etag': '_quYyNz6XPXmAaWfx4pkGm_ZXRA',
             'id': {'kind': 'youtube#video', 'videoId': 'Jn09UdSb3aA'},
             'snippet': {'publishedAt': '2020-03-04T12:00:04Z', 'channelId': 'UCyOfqgtsQaM3S-VZnsYnHjQ',
                         'title': 'The Best of Chopin',
                         'description': 'Buy the MP3 album on the Official Halidon Music Store: http://bit.ly/2VsAYhx Listen to our playlist on Spotify: http://bit.ly/ChopinEssentialClassics Order “100 ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/Jn09UdSb3aA/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/Jn09UdSb3aA/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/Jn09UdSb3aA/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'HALIDONMUSIC', 'liveBroadcastContent': 'none',
                         'publishTime': '2020-03-04T12:00:04Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'MZlBVe69q-F48BsRJGGu2F857E0',
             'id': {'kind': 'youtube#video', 'videoId': 'wygy721nzRc'},
             'snippet': {'publishedAt': '2012-10-04T12:20:38Z', 'channelId': 'UCyOfqgtsQaM3S-VZnsYnHjQ',
                         'title': 'The Best of Chopin',
                         'description': 'Buy the MP3 album on the Official Halidon Music Store: http://bit.ly/VzxEKC Stream it on Spotify: https://spoti.fi/2NtSPPg iTunes & Apple Music: ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/wygy721nzRc/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/wygy721nzRc/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/wygy721nzRc/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'HALIDONMUSIC', 'liveBroadcastContent': 'none',
                         'publishTime': '2012-10-04T12:20:38Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'gGV-HMYHh4I0__r6kBeB6wq7DXA',
             'id': {'kind': 'youtube#video', 'videoId': '-gDinVAmtA0'},
             'snippet': {'publishedAt': '2014-11-16T13:39:29Z', 'channelId': 'UCbMVYFIWtp3NJR4LUvttbMQ',
                         'title': 'Chopin Nocturnes', 'description': 'François Chaplin ,piano.', 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/-gDinVAmtA0/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/-gDinVAmtA0/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/-gDinVAmtA0/hqdefault.jpg', 'width': 480, 'height': 360}},
                         'channelTitle': 'Wonders Of Classical Music', 'liveBroadcastContent': 'none',
                         'publishTime': '2014-11-16T13:39:29Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'U1D-TECfacJob5-K1v2uNLVyWLE',
             'id': {'kind': 'youtube#video', 'videoId': '9E6b3swbnWg'},
             'snippet': {'publishedAt': '2013-06-19T10:46:07Z', 'channelId': 'UC1Prrgck1S6abc3yPWhc7Jw',
                         'title': 'Chopin - Nocturne op.9 No.2',
                         'description': 'Nocturne in E-flat major, Op. 9, No. 2 Played by Vadim Chaimovich (https://www.youtube.com/vadimchaimovich) FB-Vadim: ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/9E6b3swbnWg/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/9E6b3swbnWg/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/9E6b3swbnWg/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'andrea romano', 'liveBroadcastContent': 'none',
                         'publishTime': '2013-06-19T10:46:07Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'rIjwlaD7v3_p7wHsgE6LesxuTbY',
             'id': {'kind': 'youtube#video', 'videoId': 'YzoPmyelSzw'},
             'snippet': {'publishedAt': '2019-02-18T12:00:05Z', 'channelId': 'UCyOfqgtsQaM3S-VZnsYnHjQ',
                         'title': 'The Best of Chopin',
                         'description': 'Buy "3 Hours Chopin for Studying, Concentration, Relaxation" (MP3 album) on the Official Halidon Music Store: http://bit.ly/2MM25ya ♫ Buy “100 Classical ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/YzoPmyelSzw/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/YzoPmyelSzw/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/YzoPmyelSzw/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'HALIDONMUSIC', 'liveBroadcastContent': 'none',
                         'publishTime': '2019-02-18T12:00:05Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'hcYEGgUYacLpPaBXRf_UqActmOA',
             'id': {'kind': 'youtube#video', 'videoId': 'EFJ7kDva7JE'},
             'snippet': {'publishedAt': '2017-02-28T19:11:01Z', 'channelId': 'UCfWXf5EvbPUxrN7vFDspDQQ',
                         'title': 'Chopin - Spring Waltz (Mariage d&#39;Amour) [Please Read Description]',
                         'description': "Disclaimer: This piece is also known as Mariage D'amour by Paul de Senneville. ''Chopin - Spring Waltz'' is just a pseudonym. Chopin hasn't written this piece.",
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/EFJ7kDva7JE/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/EFJ7kDva7JE/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/EFJ7kDva7JE/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'Toms Mucenieks', 'liveBroadcastContent': 'none',
                         'publishTime': '2017-02-28T19:11:01Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'bZF8cB1U72y3BoPBVepE8vJo81c',
             'id': {'kind': 'youtube#video', 'videoId': 'AJesAlohO6I'},
             'snippet': {'publishedAt': '2018-01-29T12:00:01Z', 'channelId': 'UCyOfqgtsQaM3S-VZnsYnHjQ',
                         'title': '6 Hours Chopin | Classical Music for Studying, Concentration, Relaxation',
                         'description': 'Buy the MP3 album on the Official Halidon Music Store: http://bit.ly/2MM25ya Listen to our playlist on Spotify: http://bit.ly/ChopinEssentialClassics Like us on ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/AJesAlohO6I/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/AJesAlohO6I/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/AJesAlohO6I/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'HALIDONMUSIC', 'liveBroadcastContent': 'none',
                         'publishTime': '2018-01-29T12:00:01Z'}},
            {'kind': 'youtube#searchResult', 'etag': '6k8fhXyzkSnuKtTzeXfC_z00gdA',
             'id': {'kind': 'youtube#video', 'videoId': 'Gus4dnQuiGk'},
             'snippet': {'publishedAt': '2019-02-14T14:00:01Z', 'channelId': 'UCPZUQqtVDmcjm4NY5FkzqLA',
                         'title': 'Chopin - Fantaisie-Impromptu (Op. 66)',
                         'description': 'Fantaisie Impromptu, Chopin Op. 66 Click the bell to always be notified on new uploads! ♫ Listen on Spotify: http://spoti.fi/2LdpqK7 ♫ Sheet Music on nkoda: ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/Gus4dnQuiGk/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/Gus4dnQuiGk/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/Gus4dnQuiGk/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'Rousseau', 'liveBroadcastContent': 'none',
                         'publishTime': '2019-02-14T14:00:01Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'tOHO0J9qctj3V3DbCtQIg6dfjLg',
             'id': {'kind': 'youtube#video', 'videoId': 'QJs1H-kytQQ'},
             'snippet': {'publishedAt': '2016-08-29T19:18:45Z', 'channelId': 'UCwn_mzmSTKdkfHV245Av0fA',
                         'title': 'Chopin   Complete Nocturnes Brigitte Engerer', 'description': '', 'thumbnails': {
                     'default': {'url': 'https://i.ytimg.com/vi/QJs1H-kytQQ/default.jpg', 'width': 120, 'height': 90},
                     'medium': {'url': 'https://i.ytimg.com/vi/QJs1H-kytQQ/mqdefault.jpg', 'width': 320, 'height': 180},
                     'high': {'url': 'https://i.ytimg.com/vi/QJs1H-kytQQ/hqdefault.jpg', 'width': 480, 'height': 360}},
                         'channelTitle': 'Classical Music', 'liveBroadcastContent': 'none',
                         'publishTime': '2016-08-29T19:18:45Z'}},
            {'kind': 'youtube#searchResult', 'etag': 'obaiqxthByQOBgva4wp1saQxm38',
             'id': {'kind': 'youtube#video', 'videoId': '38uEZN5-Hqg'},
             'snippet': {'publishedAt': '2018-10-15T11:00:01Z', 'channelId': 'UCyOfqgtsQaM3S-VZnsYnHjQ',
                         'title': 'Chopin - Best of Piano',
                         'description': 'Buy "Chopin: Piano Solo" (MP3 album) from the Official Halidon music store: http://bit.ly/2nhpOuP Listen to "Chopin: Essential Classics" on Spotify: ...',
                         'thumbnails': {
                             'default': {'url': 'https://i.ytimg.com/vi/38uEZN5-Hqg/default.jpg', 'width': 120,
                                         'height': 90},
                             'medium': {'url': 'https://i.ytimg.com/vi/38uEZN5-Hqg/mqdefault.jpg', 'width': 320,
                                        'height': 180},
                             'high': {'url': 'https://i.ytimg.com/vi/38uEZN5-Hqg/hqdefault.jpg', 'width': 480,
                                      'height': 360}}, 'channelTitle': 'HALIDONMUSIC', 'liveBroadcastContent': 'none',
                         'publishTime': '2018-10-15T11:00:01Z'}}]}
    search = {}
    search_data = []

    for item in search_result['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        video = item['id']['videoId']
        search['title'] = title
        search['description'] = description
        search['videoId'] = video


        field2.insert('end', title)
    print(search_data)

    return search_data


def getDetails():
    detail = field2.get(field2.curselection())
    print(detail)


# Download the first video
def downloadVideo(finalURL):
    youtube = pytube.YouTube(finalURL)
    video = youtube.streams.first()
    video.download('C:/Users/Muffin/Downloads')


# Interface
if __name__ == "__main__":
    master = tk.Tk()

    s = tk.StringVar()

    field1 = tk.Entry(master, textvariable=s)
    field1.config({"background": "Gold"})
    field2 = tk.Listbox(master, height=30, width=30)
    field2.config({"background": "Snow"})
    field3 = tk.Text(master, height=30, width=30)
    field3.config({"background": "Snow"})

    field1.place(x=20, y=20, width=660, height=40)
    field2.place(x=20, y=80, width=660, height=200)
    field3.place(x=20, y=300, width=660, height=280)

    # set font
    myFont = font.Font(family='Verdana', size=9, weight='bold')

    text = "Welcome to YouTube Downloader!\n" \
           + "Instruction: Search the title,\n" \
           + "and click the title from the list,\n" \
           + "and download is done!"

    canvas = tk.Canvas(master, width=250, height=100, bg='Maroon')
    canvas.pack()
    canvas.place(x=700, y=40)
    canvas.create_text(125, 50, fill="white", font=myFont, text=text)

    # set the background colour of GUI window
    master.configure(background="PeachPuff2")

    # set the title of GUI window
    master.title("Sarah's YouTube Downloader")

    # set the configuration of GUI window
    master.geometry("970x600")

    # Buttons
    Search = tk.Button(master, text=' SEARCH ', fg='black', bg='white',
                       command=download, height=5, width=30)
    Search.place(x=700, y=300)
    Search['font'] = myFont

    Details = tk.Button(master, text=' GET DETAILS ', fg='black', bg='Ivory',
                        command=getDetails, height=5, width=30)
    Details.place(x=700, y=400)
    Details['font'] = myFont

    Download = tk.Button(master, text=' DOWNLOAD ', fg='black', bg='red',
                         command='', height=5, width=30)
    Download.place(x=700, y=500)
    Download['font'] = myFont

# start the GUI
master.mainloop()
