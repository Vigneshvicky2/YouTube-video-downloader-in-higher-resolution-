
from pytube import YouTube
link=str(input("Enter your video link : "))
yt=YouTube(link)
print("************YOUR VIDEO TITLE************")
print(yt.title)
print("please wait your video is now downloading....")
resolution=yt.streams.filter(progressive='True',file_extension='mp4')

resolution.get_highest_resolution().download()
print("Download completed")
print("This program was created by vignesh")