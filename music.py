import tkinter as tk
from pygame import mixer



root = tk.Tk()
root.geometry("100x200")

music_file = "escape_room.mp3"
mixer.init()
mixer.music.load(music_file)
mixer.music.play()

button = tk.Button(root, text="Pause", font=("Arial", 20), command=toggle_pause)
button.pack()

root.mainloop()
