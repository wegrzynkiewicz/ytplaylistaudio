import pafy

playlist_url = 'https://www.youtube.com/playlist?list=' + str(input("wprowadz koncowke url: "))
playlist = pafy.get_playlist2(playlist_url)
filelist = []

for video in playlist:
  try:
    print(video.title)
    best = video.getbestaudio('m4a')
    filename = best.download()
    filelist.append(filename)
  except:
      pass

print("Pobrano")