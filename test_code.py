import sys
import os
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
os.system('cls')


link = "iG58Jo5udLA"
full_text = ''' '''
video_transcript = YouTubeTranscriptApi.get_transcript(link)
print(video_transcript)
for item in range(len(video_transcript)):
    full_text += video_transcript[item]["text"] + " "
    print(video_transcript[item]["text"])
print([video_transcript, full_text])