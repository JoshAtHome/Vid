



def links(number, word, format):
   linkarr = []
   key = 'QxskOidzwLe5gdKTDjhrKzyvN2w4uYxwxapWk5JcE8fhyIAP1IxknS3h'
   pexel = Pexels(key)
   seen = 0

   for k in range(0, 10): #pages
    if len(linkarr) == number:
      break
    search_videos = pexel.search_videos(query=word, orientation='', size='small', color='', locale='', page=k, per_page=80)

    for j in range(1, 79): #videos
      if len(linkarr) == number:
        break
      location = search_videos['videos'][j]['video_files']
      found = False

      for i in range(0,len(location)): #exact video
        if len(linkarr) == number:
          break
        measurements = False
        if (location[i]['width'] != 0) & (location[i]['height'] != 0) & (location[i]['quality'] == 'sd'):
          measurements = (0.56 < (location[i]['height'] / location[i]['width']) < 0.565)
          if format is True:
            measurements = (1.77 < (location[i]['height'] / location[i]['width']) < 1.78)
        link = search_videos['videos'][j]['video_files'][i]['link']
        duration = search_videos['videos'][0]['duration']
#         speed = location[i]['fps'] >= 24
        if measurements & (duration > 5):   # replace 8 with most
             linkarr.append(link)
             found = True
             break
        seen += 1

   print(seen)
   if len(linkarr) != number:
    print("!!! NOT ENOUGH LINKS !!!")
   return linkarr
