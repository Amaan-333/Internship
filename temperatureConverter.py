import tkinter as tk
from tkinter import messagebox
import datetime
import threading
import winsound
import time


def set_alarm():
    alarm_time = alarm_entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid time in HH:MM format")
        return

    alarm_time_obj = datetime.time(alarm_hour, alarm_minute)
    current_time = datetime.datetime.now().time()

    time_diff_seconds = (datetime.datetime.combine(datetime.date.today(), alarm_time_obj) -
                         datetime.datetime.combine(datetime.date.today(), current_time)).total_seconds()

    if time_diff_seconds <= 0:
        messagebox.showerror("Error", "Please set a time in the future")
        return

    threading.Thread(target=wait_for_alarm, args=(time_diff_seconds,)).start()


def wait_for_alarm(seconds):
    print("Alarm set!")
    print(f"Alarm will ring in {seconds} seconds.")
    time.sleep(seconds)  # Pause execution until alarm time
    messagebox.showinfo("Alarm", "Wake up!")
    winsound.Beep(500, 1000)  # Beep sound (Windows specific)



root = tk.Tk()
root.title("Alarm Clock")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

alarm_label = tk.Label(main_frame, text="Set Alarm Time (HH:MM):")
alarm_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
alarm_entry = tk.Entry(main_frame)
alarm_entry.grid(row=0, column=1, padx=10, pady=5)

set_button = tk.Button(main_frame, text="Set Alarm", command=set_alarm)
set_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
