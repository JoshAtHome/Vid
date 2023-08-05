aud = "WC1.wav"
word = "Business"
Short = False

t = [2.121, 5.905, 9.02095238095238]


def clips():
   stamp = stamps(aud)
   cl = stamp
   many = len(stamp)
   most = max(stamp)
   video_urls = links(many, word, Short)

#   video_urls[0] = "a1.mp4"
   if len(video_urls) != many:
    ("!!! LINKS != STAMPS !!!")
   videos = []
   delay = 0.11288889
   quality = (1920, 1080)
   if Short:
    quality = (1080, 1920)
   for i in range(0, many):
     video = mp.VideoFileClip(video_urls[i])
     video = video.resize(quality)
     video = video.subclip(1, cl[i]+1)
     videos.append(video)

   final_video = mp.concatenate_videoclips(videos)
   test = final_video.subclip(delay, sum(cl))

   speechclip = mp.AudioFileClip(aud)
   #songclip = mp.AudioFileClip(song)
   #songsub = songclip.subclip(1, total + 1).volumex(0.05)
   #final_audio = mp.CompositeAudioClip([speechclip, songsub])
   #EXO = video.set_audio(final_audio)

   #EXO = final_video.set_audio(speechclip)

   EXO = test.set_audio(speechclip)

   if os.path.exists(word + ".mp4"):
    os.remove(word + ".mp4")
   EXO.write_videofile(word + ".mp4")

##################### ##################### #####################

clips()

##################### ##################### #####################
