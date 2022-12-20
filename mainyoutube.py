# https://pytube.io/en/latest/index.html
# https://github.com/pytube/pytube#Quickstart

from pytube import YouTube

def Download(link):
    youtubeMovie = YouTube(link).streams.get_highest_resolution().download()

link = input('URL eingeben:')
Download(link)