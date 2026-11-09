import json
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import filedialog

import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CreateTrackList:
    def __init__(self, window):
        self.window = window
        self.playlist = []

        window.geometry("750x380")
        window.title("Create Track List")

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_clicked)
        add_track_btn.grid(row=0, column=2, padx=10, pady=10)

        play_list_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_list_btn.grid(row=0, column=3, padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)
        reset_btn.grid(row=0, column=4, padx=10, pady=10)

        save_btn = tk.Button(window, text="Save Playlist", command=self.save_playlist_clicked)
        save_btn.grid(row=0, column=5, padx=10, pady=10)

        load_btn = tk.Button(window, text="Load Playlist", command=self.load_playlist_clicked)
        load_btn.grid(row=0, column=6, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(window, width=70, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=7, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=7, sticky="W", padx=10, pady=10)

        self.refresh_playlist_display()

    def normalise_key(self, key):
        key = key.strip()
        if key == "":
            self.status_lbl.configure(text="Please enter a track number.")
            return None
        if not key.isdigit():
            self.status_lbl.configure(text="Track number must be numeric, for example 04.")
            return None
        key = key.zfill(2)
        if lib.get_name(key) is None:
            self.status_lbl.configure(text=f"Track {key} was not found.")
            return None
        return key

    def refresh_playlist_display(self):
        if len(self.playlist) == 0:
            set_text(self.playlist_txt, "Playlist is currently empty.")
            return

        playlist_output = ""
        track_total = 1
        for key in self.playlist:
            name = lib.get_name(key)
            artist = lib.get_artist(key)
            playlist_output += f"{track_total}. {key} {name} - {artist}\n"
            track_total += 1
        set_text(self.playlist_txt, playlist_output)

    def add_track_clicked(self):
        key = self.normalise_key(self.input_txt.get())
        if key is None:
            return

        self.playlist.append(key)
        self.refresh_playlist_display()
        name = lib.get_name(key)
        self.status_lbl.configure(text=f"{name} was added to the playlist.")

    def play_playlist_clicked(self):
        if len(self.playlist) == 0:
            self.status_lbl.configure(text="The playlist is empty, so there is nothing to play.")
            return

        for key in self.playlist:
            lib.increment_play_count(key)

        self.status_lbl.configure(
            text=f"Playlist button was clicked. {len(self.playlist)} track(s) were played in the simulation."
        )

    def reset_clicked(self):
        self.playlist.clear()
        self.refresh_playlist_display()
        self.status_lbl.configure(text="The playlist was cleared.")

    def save_playlist_clicked(self):
        if len(self.playlist) == 0:
            self.status_lbl.configure(text="You cannot save an empty playlist.")
            return

        file_name = filedialog.asksaveasfilename(
            title="Save playlist",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if file_name == "":
            return

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.playlist, file)

        self.status_lbl.configure(text="Playlist saved successfully.")

    def load_playlist_clicked(self):
        file_name = filedialog.askopenfilename(
            title="Load playlist",
            filetypes=[("JSON files", "*.json")]
        )
        if file_name == "":
            return

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                loaded_playlist = json.load(file)

            checked_playlist = []
            for key in loaded_playlist:
                key = str(key).zfill(2)
                if lib.get_name(key) is not None:
                    checked_playlist.append(key)

            self.playlist = checked_playlist
            self.refresh_playlist_display()
            self.status_lbl.configure(text="Playlist loaded successfully.")
        except (OSError, ValueError, TypeError):
            self.status_lbl.configure(text="The selected file could not be loaded.")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTrackList(window)
    window.mainloop()
