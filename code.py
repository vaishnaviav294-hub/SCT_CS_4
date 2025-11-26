from pynput import keyboard

log_file = "key_input_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False

print("Type inside this window. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
