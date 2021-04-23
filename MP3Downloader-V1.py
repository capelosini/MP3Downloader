import youtube_dl
import youtube_search
import requests
import os

print("\n=- MP3 Downloader V1 -=\n")
while True:
    link=input("Link: ")


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        if "https://www.youtube.com/" in link or "https://youtu.be/" in link:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print(" ")
                ydl.download([link])
                print(" ")
        elif "https://cdn.discordapp.com/attachments/" in link:
            name=link.split("/")
            name=name[-1]
            name=name.split(".")
            extlink=name[-1]
            name=name[0]
            ext="mp3"
            if extlink == "png" or extlink == "jpg":
                ext="png"
            print(" ")
            os.system(f"curl {link} -o {name}.{ext}")
            print(" ")
        elif "https://open.spotify.com/track/" in link:
            r=requests.get(link)
            content=(r.text).splitlines()
            content=content[0]
            titlestart=content.find("<title>")
            titleend=content.find("</title>")
            name=content[titlestart+7:titleend]
            search=(youtube_search.YoutubeSearch(name, max_results=1).to_dict()[0])["url_suffix"]
            ytlink=(f"https://www.youtube.com{search}")
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print(" ")
                ydl.download([ytlink])
                print(" ")
    except:
        print("\nPlease Try Again\n")
