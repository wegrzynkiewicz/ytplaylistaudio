import sys
import pafy

playlist_url = 'https://www.youtube.com/playlist?list=' + sys.argv[1]
playlist = pafy.get_playlist2(playlist_url)

for video in playlist:
  try:
    print(video.title)
    video.getbestaudio('m4a').download()
  except:
    pass
