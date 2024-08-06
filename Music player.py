import tkinter as tk
from tkinter import filedialog
from pygame import mixer
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        mixer.init()
        self.is_playing = False
        self.track_file = ""
        # Create UI elements
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack(pady=20)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(pady=20)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=20)
        self.load_button = tk.Button(root, text="Load", command=self.load)
        self.load_button.pack(pady=20)
    def load(self):
        self.track_file = filedialog.askopenfilename(filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*")))
        if self.track_file:
            mixer.music.load(self.track_file)
    def play(self):
        if self.track_file:
            if not self.is_playing:
                mixer.music.play()
                self.is_playing = True
            else:
                mixer.music.unpause()
    def pause(self):
        if self.is_playing:
            mixer.music.pause()
            self.is_playing = False
    def stop(self):
        mixer.music.stop()
        self.is_playing = False
if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()