import time
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os
def update_frame():
    global frame_index
    frame_index = (frame_index + 1) % frame_count
    monkey_label.configure(image=frames[frame_index])
    root.after(frame_delay, update_frame)
def move_window():
    global x, y, dx, dy, screen_width, screen_height, window_width, window_height
    x += dx
    y += dy
    if x <= 0 or x + window_width >= screen_width:
        dx = -dx
    if y <= 0 or y + window_height >= screen_height:
        dy = -dy
    root.geometry(f"+{x}+{y}")
    root.after(20, move_window)
root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "pink")
root.attributes("-topmost", True)
gif_path = "monkey_dancing.gif"
if not os.path.exists(gif_path):
    print(f"Error: The file {gif_path} does not exist.")
    print("Shutting down in 3 seconds...")
    time.sleep(1)
    print("Shutting down in 2 seconds...")
    time.sleep(1)
    print("Shutting down in 1 second...")
    time.sleep(1)
    print("Shutting down now.")
    time.sleep(0.25)
    exit()
gif = Image.open(gif_path)
frames = []
frame_delay = gif.info.get("duration", 100)
try:
    while True:
        frame = ImageTk.PhotoImage(gif.convert("RGBA"))
        frames.append(frame)
        gif.seek(len(frames))
except EOFError:
    pass
frame_count = len(frames)
frame_index = 0
window_width = 200
window_height = 200
x, y = 100, 100  # Initial position
dx, dy = 5, 5  # Velocity (change in x and y coordinates per step)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.configure(bg="pink")  # Ensure the transparent parts of the GIF will match this color
monkey_label = Label(root, bg="pink")  # Must match the window's transparent color
monkey_label.pack()
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
update_frame()
move_window()
root.bind("<Button-1>", lambda e: root.destroy())
root.mainloop()
