# download button will default to download mp4 at 720p
from pytube import YouTube
from pytube.streams import Stream
import tkinter
from tkinter import ttk

url = ""
yt = None

def searchStream():
    global inputname, yt, status
    status.config(text = "searching for stream...")

    url = inputname.get(1.0, "end-1c") # read from 0th character of 1st line, remove the last character (\n)
    yt = YouTube(url)

    availableMp4 = yt.streams.filter(file_extension='mp4', type="video")
    print("mp4: ")
    for i in range(len(availableMp4)):
        if(availableMp4[i - 1].resolution != availableMp4[i].resolution):
            print(availableMp4[i].resolution)

    availableMp3 = yt.streams.filter(type='audio')
    print("mp3: ")
    for i in range(len(availableMp3)):
        print(availableMp3[i])
    download("mp4", "720p")
    

def download(format, resolution=None):
    global status
    if(format == 'mp4'):
        try:
            stream = yt.streams.filter(res=resolution)[0]
            print(stream)
            stream.download(output_path='Python/video')
            status.config(text = "download completed! check Python/video/")
        except Exception as e:
            print(e)
    if(format == 'mp3'):
        try:
            stream = yt.streams.filter(type='audio')[0]
            print(stream)
            stream.download(output_path='Python/video')
            status.config(text = "download completed! check Python/video/")
        except Exception as e:
            print(e)

def main():
    global inputname, status

    # window configuration
    window = tkinter.Tk()
    window.title("YouTube Downloader")
    window.geometry("600x400")
    frame = ttk.Frame(window, padding=10)
    frame.grid()

    # widgets configuration
    inputname = tkinter.Text(frame, height = 5, width = 50)
    inputname.grid(column=0, row=0)
    inputbutton = tkinter.Button(frame, text="Download", command=searchStream)
    inputbutton.grid(column=1, row=0)
    status = tkinter.Label(frame, text="")
    status.grid(column=0, row=1)

    window.mainloop()

if __name__ == "__main__":
    main()
