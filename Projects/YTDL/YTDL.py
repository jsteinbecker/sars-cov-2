from pytube import YouTube
import pytube
import asyncio
import os



CACHE_PATH = 'cache'


def before_start():
    """ Before the bot starts """
    if not os.path.exists(CACHE_PATH):
        os.mkdir(CACHE_PATH)
        
        
async def download_audio(video:pytube.YouTube,name:str):
    """ Download the audio of a video """
    audio = video.streams.filter(only_audio=True).first()
    path = os.path.join(CACHE_PATH, name + '.wav')
    with open(path, 'wb') as f:
        audio.stream_to_buffer(f)
    return path

# MAIN FUNCTION
def yt_download(videoURL:str,name:str="Untitled"):
    before_start()
    """ Main function """
    video = pytube.YouTube(videoURL)
    asyncio.run(download_audio(video,name))
    
    
    

if __name__ == "__main__":
    yt_download("https://www.youtube.com/watch?v=kwA5GsQBVOk", "BLACK : DUET FOR 2 BASS CLARINETS")