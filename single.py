import sys
import pafy

url = 'https://www.youtube.com/watch?v=' + sys.argv[1]
video = pafy.new(url)
print(video.title)
video.getbestaudio('m4a').download()