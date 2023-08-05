!pip3 install moviepy
!pip install imageio-ffmpeg
!pip3 install imageio==2.4.1
!pip install --upgrade imageio-ffmpeg
!pip install pexels_api_py
!pip install pydub
!pip install numpy
import requests
import os
import moviepy.editor as mp
from pexelsapi.pexels import Pexels
from pydub import AudioSegment, silence
import moviepy.audio.fx.all as afx
import numpy as np
from itertools import chain

most = 0

def smaller(arr):
 result = []
 result2 = []
 for i in range(len(arr)):
    if arr[i] < 1:
        if i+1 < len(arr):
            arr[i+1] += arr[i]
    else:
        result.append(arr[i])
 return result

def too_big(C): # checks if there are leaps bigger than 3 // insert array
  C.sort()
  m = C[0]
  for i in range(1, len(C)):
    if C[i] - C[i-1] > m:
      m = C[i] - C[i-1]
  if m >= 4:
    return True
  else: return False

def findel(arr, target):
    closest_element = None
    min_difference = 10
    for element in arr:
        difference = abs(element - target)
        if difference < min_difference:
            closest_element = element
            min_difference = difference
    return closest_element

def insertel(arr1, arr2):
    result = []
    arr1.insert(0,0)
    arr2.insert(0,0)
    for i in range(0, len(arr1)):
        result.append(arr1[i])
        if arr1[i] - arr1[i-1] > 4:
            mean = (arr1[i] + arr1[i-1]) / 2
            arr3 = [b for b in arr2 if arr1[i-1] <= b <= arr1[i]]
            closest_element = findel(arr3, mean) - 0.1
            result.append(closest_element)
    result.sort()
    result.remove(0)
    return result

def getstamps(aud, thr):
   myaudio = AudioSegment.from_wav(aud)
   total = myaudio.duration_seconds
   ok = silence.detect_silence(myaudio, min_silence_len=600, silence_thresh=-thr)
   ok = [((start/1000),(stop/1000)) for start,stop in ok] #convert to sec
   timestamp = []
   for i in range(len(ok)-1):
      timestamp.append(ok[i][1])
   timestamp.append(total)
   return timestamp

def stamps(audio):
   timestampSix = getstamps(audio, 30)
   print(timestampSix)
   timestampNine = getstamps(audio, 25)
   print(timestampNine)
   for i in range(0, len(timestampSix)):
       if too_big(timestampSix):
        timestampSixx = insertel(timestampSix, timestampNine)
        timestampSix = timestampSixx
        i = 0
   timestamps = [*set(timestampSix)]
   timestamps.sort()
   print("MERGED")
   print(timestamps)
   clips = [0]
   clips[0] = timestamps[0]
   for i in range(1, len(timestamps)):
     clip = timestamps[i] - timestamps[i-1]
     clip2 = round(clip, 6)
     clips.append(clip2)
   return clips

a = stamps("WC1.wav")
print(a)
