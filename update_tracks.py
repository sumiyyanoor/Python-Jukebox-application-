import tkinter as tk

import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class UpdateTracks:
    def __init__(self, window):
        window.geometry("520x220")
        window.title("Update Tracks")

        track_lbl = tk.Label(window, text="Enter Track Number")
        track_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.track_input = tk.Entry(window, width=3)
        self.track_input.grid(row=0, column=1, padx=10, pady=10)

        rating_lbl = tk.Label(window, text="Enter New Rating")
        rating_lbl.grid(row=0, column=2, padx=10, pady=10)

        self.rating_input = tk.Entry(window, width=3)
        self.rating_input.grid(row=0, column=3, padx=10, pady=10)

        update_btn = tk.Button(window, text="Update Rating", command=self.update_clicked)
        update_btn.grid(row=0, column=4, padx=10, pady=10)

        self.output_txt = tk.Text(window, width=34, height=4, wrap="none")
        self.output_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

    def update_clicked(self):
        key = self.track_input.get().strip()
        rating_text = self.rating_input.get().strip()

        if key == "":
            self.status_lbl.configure(text="Please enter a track number.")
            set_text(self.output_txt, "")
            return

        if not key.isdigit():
            self.status_lbl.configure(text="Track number must be numeric, for example 04.")
            set_text(self.output_txt, "")
            return

        key = key.zfill(2)
        name = lib.get_name(key)

        if name is None:
            self.status_lbl.configure(text=f"Track {key} was not found.")
            set_text(self.output_txt, "")
            return

        if not rating_text.isdigit():
            self.status_lbl.configure(text="Rating must be a whole number between 1 and 5.")
            set_text(self.output_txt, "")
            return

        rating = int(rating_text)
        if rating < 1 or rating > 5:
            self.status_lbl.configure(text="Rating must be between 1 and 5.")
            set_text(self.output_txt, "")
            return

        lib.set_rating(key, rating)
        artist = lib.get_artist(key)
        play_count = lib.get_play_count(key)
        track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
        set_text(self.output_txt, track_details)
        self.status_lbl.configure(text="Update Rating button was clicked!")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracks(window)
    window.mainloop()
