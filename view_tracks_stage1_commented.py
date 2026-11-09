import tkinter as tk                     # imports tkinter so GUI widgets can be created
import tkinter.scrolledtext as tkst     # imports a text widget with a built-in scrollbar

import track_library as lib             # imports the library functions used to read track data
import font_manager as fonts            # imports the shared font configuration


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)     # clears everything currently shown in the text area
    text_area.insert(1.0, content)      # inserts the new text starting at the first character position


class TrackViewer():
    def __init__(self, window):
        window.geometry("750x350")      # sets the size of the window
        window.title("View Tracks")     # sets the window title

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)  # places the button in the grid

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)        # label explaining what the user should type

        self.input_txt = tk.Entry(window, width=3)               # entry box for the track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)  # button calls view_tracks_clicked when pressed

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        # this large scrolling text box shows the full track list

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        # this text box shows details for one chosen track

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        # this label shows feedback after a button click

        self.list_tracks_clicked()      # when the window opens, load the track list straight away

    def view_tracks_clicked(self):
        key = self.input_txt.get()      # reads whatever the user typed into the entry box
        name = lib.get_name(key)        # gets the track name from the library using that key

        if name is not None:            # if a valid track exists with that key
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)   # show the chosen track details in the text area
        else:
            set_text(self.track_txt, f"Track {key} not found")   # otherwise show an error message

        self.status_lbl.configure(text="View Track button was clicked!")  # updates the status label

    def list_tracks_clicked(self):
        track_list = lib.list_all()     # gets the full formatted list of tracks from the library
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")  # confirms the action to the user


if __name__ == "__main__":              # this section only runs if the file itself is run directly
    window = tk.Tk()                    # creates the main tkinter window
    fonts.configure()                   # applies the shared font settings
    TrackViewer(window)                 # creates the TrackViewer GUI inside the window
    window.mainloop()                   # keeps the window open and listens for events such as button clicks
