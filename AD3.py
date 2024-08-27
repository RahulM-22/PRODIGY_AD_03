import tkinter as tk
from tkinter import StringVar

# Initialize the main window
root = tk.Tk()
root.title("Stopwatch")

# Define global variables
running = False
counter = 0

# Define the time display string
time_string = StringVar()
time_string.set("00:00:00")

# Function to start the stopwatch
def start_timer():
    global running
    if not running:
        running = True
        update_timer()

# Function to pause the stopwatch
def pause_timer():
    global running
    if running:
        running = False

# Function to reset the stopwatch
def reset_timer():
    global running, counter
    if running:
        running = False
    counter = 0
    time_string.set("00:00:00")

# Function to update the time
def update_timer():
    global counter
    if running:
        # Calculate minutes, seconds, and milliseconds
        minutes = counter // 6000
        seconds = (counter // 100) % 60
        milliseconds = counter % 100

        # Format the time string
        time_string.set(f"{minutes:02}:{seconds:02}:{milliseconds:02}")

        # Increment the counter
        counter += 1

        # Call the update_timer function after 10 milliseconds
        root.after(10, update_timer)

# Define the time label
time_label = tk.Label(root, textvariable=time_string, font=("Arial", 40), bg="black", fg="white")
time_label.pack(pady=20)

# Define the control buttons
start_button = tk.Button(root, text="Start", font=("Arial", 20), command=start_timer)
start_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(root, text="Pause", font=("Arial", 20), command=pause_timer)
pause_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(root, text="Reset", font=("Arial", 20), command=reset_timer)
reset_button.pack(side=tk.LEFT, padx=10)

# Run the main loop
root.mainloop()
