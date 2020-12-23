import pytube
import urllib.request
import urllib.parse
import re
import tkinter as tk
import tkinter.font as font


def userInput():
    print("Please type such as: Chopin Nocturne No 9 op 5")
    subject = input("What video do you want to download in YouTube?")
    return subject


# Search the youtube video with what user type
def searchYoutube(subject):
    query_string = urllib.parse.urlencode({"search_query": subject})
    print("1")
    print(query_string)
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    print("2")
    print(html_content)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print(search_results)
    finalURL = "http://www.youtube.com/watch?v=" + search_results[0]
    print(finalURL)


# Download the first video
def downloadVideo(finalURL):
    youtube = pytube.YouTube(finalURL)
    video = youtube.streams.first()
    video.download('C:/Users/Muffin/Downloads')


def download():
    expression = field1.get()
    searchYoutube(expression)


# Interface
if __name__ == "__main__":
    master = tk.Tk()

    s = tk.StringVar()

    field1 = tk.Entry(master, textvariable=s)
    field1.config({"background": "Gold"})
    field2 = tk.Text(master, wrap="word", height=30, width=30)
    field2.config({"background": "Snow"})

    field1.place(x=20, y=20, width=660, height=40)
    field2.place(x=20, y=80, width=660, height=500)

    field2.configure(state='disabled')

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
    master.title("Recipe Finder")

    # set the configuration of GUI window
    master.geometry("970x600")

    # Buttons
    Download = tk.Button(master, text=' ENTER ', fg='black', bg='white',
                         command=download, height=5, width=30)
    Download.place(x=700, y=500)
    Download['font'] = myFont

# start the GUI
master.mainloop()
