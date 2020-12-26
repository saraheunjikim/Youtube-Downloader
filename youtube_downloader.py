from pytube import YouTube
import tkinter as tk
import tkinter.font as font
import re
from googleapiclient.discovery import build

api_key = 'Your API Key'


def search():
    keyword = field1.get()
    if len(keyword) < 4:
        field2.insert('end', 'Please type more than 4 letter.')
    else:
        field2.delete(0, 'end')
        searchYoutube(keyword)


def searchYoutube(keyword):
    global search_data
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_request = youtube.search().list(part='snippet', q=keyword,
                                           type='video', maxResults=10)
    search_result = search_request.execute()
    search = {}
    search_data = {}

    for item in search_result['items']:

        title = item['snippet']['title']
        description = item['snippet']['description']
        video = item['id']['videoId']
        full_data = title + "    Video Id:" + video

        search[video] = {'title': title, 'description': description}
        search_data.update(search)

        field2.insert('end', full_data)

    return search_data


def getDetails():
    global desc
    full_data = field2.get(field2.curselection())
    video_id = re.findall('(?<=Video Id:).*$', full_data)[0]

    for idx, info in search_data.items():
        if idx == video_id:
            if info['description']:
                desc = info['description']
            else:
                desc = 'No Description'

    field3.insert('end', desc)

    return video_id


# Download the first video
def downloadVideo():
    full_data = field2.get(field2.curselection())
    video_id = re.findall('(?<=Video Id:).*$', full_data)[0]

    return YouTube('https://www.youtube.com/watch?v=' + video_id).streams[0].download()


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
                       command=search, height=5, width=30)
    Search.place(x=700, y=300)
    Search['font'] = myFont

    Details = tk.Button(master, text=' GET DETAILS ', fg='black', bg='Ivory',
                        command=getDetails, height=5, width=30)
    Details.place(x=700, y=400)
    Details['font'] = myFont

    Download = tk.Button(master, text=' DOWNLOAD ', fg='black', bg='red',
                         command=downloadVideo, height=5, width=30)
    Download.place(x=700, y=500)
    Download['font'] = myFont

# start the GUI
master.mainloop()
