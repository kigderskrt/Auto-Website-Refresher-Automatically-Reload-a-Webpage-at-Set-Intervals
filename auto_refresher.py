import time
import webbrowser
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

def get_seconds(value: float, unit: str) -> int:
    unit = unit.lower()
    if unit.startswith('s'):
        return int(value)
    elif unit.startswith('m'):
        return int(value * 60)
    elif unit.startswith('h'):
        return int(value * 3600)
    else:
        raise ValueError("Unsupported time unit. Use seconds, minutes, or hours.")

def start_refresher():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        interval = float(interval_entry.get())
        interval_unit = interval_unit_var.get()
        interval_seconds = get_seconds(interval, interval_unit)

        duration = float(duration_entry.get())
        duration_unit = duration_unit_var.get()
        duration_seconds = get_seconds(duration, duration_unit)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        return

    def refresher():
        nonlocal interval_seconds, duration_seconds, url
        print(f"\nStarting refresher for {url}")
        print(f"Refresh every {interval_seconds} seconds for {duration_seconds} seconds.\n")

        end_time = datetime.now() + timedelta(seconds=duration_seconds)
        count = 0

        while datetime.now() < end_time:
            webbrowser.open(url, new=0)
            count += 1
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Refresh #{count}")
            time.sleep(interval_seconds)

        print(f"\nDone refreshing {count} times. Exiting...")
        messagebox.showinfo("Done", f"Refreshed {count} times.")

    root.after(100, refresher)

# Create the GUI
root = tk.Tk()
root.title("Auto Website Refresher")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(frame, text="Website URL:").grid(row=0, column=0, sticky="w", pady=5)
url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Refresh Interval:").grid(row=1, column=0, sticky="w", pady=5)
interval_entry = ttk.Entry(frame, width=10)
interval_entry.grid(row=1, column=1, sticky="w", pady=5)
interval_unit_var = tk.StringVar(value="seconds")
interval_unit_menu = ttk.Combobox(frame, textvariable=interval_unit_var, values=["seconds", "minutes"], state="readonly")
interval_unit_menu.grid(row=1, column=1, sticky="e", pady=5)

ttk.Label(frame, text="Total Duration:").grid(row=2, column=0, sticky="w", pady=5)
duration_entry = ttk.Entry(frame, width=10)
duration_entry.grid(row=2, column=1, sticky="w", pady=5)
duration_unit_var = tk.StringVar(value="minutes")
duration_unit_menu = ttk.Combobox(frame, textvariable=duration_unit_var, values=["minutes", "hours"], state="readonly")
duration_unit_menu.grid(row=2, column=1, sticky="e", pady=5)

start_btn = ttk.Button(frame, text="Start Refresher", command=start_refresher)
start_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
