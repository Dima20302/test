import tkinter as tk
import time
import threading

class CountdownTimer:
    def __init__(self, root, duration):
        self.root = root
        self.duration = duration
        self.running = False
        self.time_left = self.duration

        self.label = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def start_timer(self):
        if not self.running:
            self.running = True
            self.time_left = self.duration
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.label.config(text="Time's up!")
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown Timer")
    root.attributes("-topmost", True)

    duration = 30 * 60  # 30 minutes in seconds
    timer = CountdownTimer(root, duration)

    root.mainloop()