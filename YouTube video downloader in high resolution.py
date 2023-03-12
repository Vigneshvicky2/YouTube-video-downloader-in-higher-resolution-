#importing module
from pytube import YouTube
#getting link from user
link=str(input("Enter your video link : "))
yt=YouTube(link)
#printing tile
print("************YOUR VIDEO TITLE************")
print(yt.title)
print("please wait your video is now downloading....")
#Downloading video
resolution=yt.streams.filter(progressive='True',file_extension='mp4')
resolution.get_highest_resolution().download()
print("Download completed")
print("This program was created by vignesh")
