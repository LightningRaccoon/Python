import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()

# Existing widget with pack() layout (example)
existing_widget = tk.Label(root, text="Existing Widget")
existing_widget.pack(padx=10, pady=10)

# Create a frame for the new buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Create the first new button and pack it to the left inside the button_frame
button1 = tk.Button(button_frame, text="New Button 1", command=button_click)
button1.pack(side=tk.LEFT, padx=5, pady=5)

# Create the second new button and pack it to the left inside the button_frame
button2 = tk.Button(button_frame, text="New Button 2", command=button_click)
button2.pack(side=tk.LEFT, padx=5, pady=5)

# Start the main event loop
root.mainloop()