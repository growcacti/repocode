def __init__(self, root):
    # ... other code ...

    self.canvas.grid(
        row=0, column=0, columnspan=3, sticky=tk.NSEW
    )  # Allow canvas to expand

    self.load_button.grid(row=1, column=0, sticky=tk.W)
    self.prev_button.grid(row=1, column=1)
    self.next_button.grid(row=1, column=2, sticky=tk.E)

    self.txt.grid(row=0, column=0, sticky=tk.NSEW)  # Allow text widget to expand

    self.extract_button.grid(row=1, column=0, pady=10)
    self.merge_button.grid(row=2, column=0, pady=10)

    self.image_canvas.grid(row=0, column=0, sticky=tk.NSEW)  # Allow canvas to expand
    self.image_extract_button.grid(row=1, column=0, pady=10)

    self.canvas2.grid(row=0, column=0, sticky=tk.NSEW)  # Allow canvas to expand

    self.button_zoom_in.grid(row=1, column=1)
    self.button_zoom_out.grid(row=1, column=2, sticky=tk.E)

    # Configure the row and column weights so they expand properly when resized
    for frame in (self.f1, self.f2, self.f3, self.f4):
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)
