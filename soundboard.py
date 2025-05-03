import os
import tkinter as tk
import tkinter.filedialog as fd
import pygame 


class SoundboardApp(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.root.title("Soundboard")
        self.root.geometry("300x200")
        self.root.configure(bg="#2c3e50")

        pygame.mixer.init()

        self.sounds = {}

        self.create_frames()

        self.create_widgets()

    def create_frames(self):
        # Top frame for controlling the sound playback
        self.control_frame = tk.Frame(self.root, bg="#2c3e50", padx=12, pady=14)
        self.control_frame.pack(fill="x")

        # Frame for sound buttons
        self.soundboard_frame = tk.Frame(self.root, bg="#2c3e50", padx=12, pady=14)
        self.soundboard_frame.pack(fill="both", expand=True)

    def create_widgets(self):

        # Control buttons
        self.add_btn = tk.Button(
            self.control_frame,
            text="Add a Sound",
            command=self.add_sound,
            bg="#3498db",
            fg="white",
            padx=12,
            pady=6
        )
        self.add_btn.pack(side="left", padx=5)

        self.remove_btn = tk.Button(
            self.control_frame,
            text="Remove a Sound",
            command=self.remove_sound,
            bg="#e74c3c",
            fg="white",
            padx=12,
            pady=6
        )
        self.remove_btn.pack(side="left", padx=5)