import tkinter
import customtkinter
from pytube import YouTube

# Info
# This is pretty simple, just run "python main.py"

# Functions


def startDownload():
    try:
        # Get entered youtube link
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        title.configure(text=ytObject.title)
        finished.configure(text="", text_color="white")

        vid = ytObject.streams.get_highest_resolution()
        vid.download()

        finished.configure(text="Download Complete")
    except:
        finished.configure(text="Invalid Link", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = (bytes_downloaded / total_size) * 100
    per = str(int(percent_completed))

    # Percent Label
    percentLabel.configure(text=per + "%")
    percentLabel.update()

    # Progress Bar
    progressBar.set(float(percent_completed) / 100)


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# frame size
app = customtkinter.CTk()

app.geometry("720x480")
app.title("Youtube Downloader")

# Add UI Elements
title = customtkinter.CTkLabel(app, text="Insert Youtube Link")
title.pack(padx=0, pady=10)

# Link Input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Finished Label
finished = customtkinter.CTkLabel(app, text="")
finished.pack()

# Progress Bar Stuff
percentLabel = customtkinter.CTkLabel(app, text="0%")
percentLabel.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Run App
app.mainloop()
