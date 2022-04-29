
import vlc
global isplaying
isplaying = False


def play(link):
    global media, isplaying

    if(isplaying == False):
        media = vlc.MediaPlayer(link)
        media.play()
        isplaying = True



def stop():
    global isplaying
    media.stop()
    isplaying = False
