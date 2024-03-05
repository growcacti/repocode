# ... [The initial imports and the class definition remain the same]


class PDFApp:
    def __init__(self, root):
        # ... [Same initializations as before]

        # Changes start here
        self.nb.grid(row=0, column=0, sticky="nsew")

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.txt.grid(row=0, column=0, sticky="nsew")

        self.load_button.grid(row=1, column=0)
        self.prev_button.grid(row=2, column=0, sticky="w")
        self.next_button.grid(row=2, column=1, sticky="e")

        self.extract_button.grid(row=1, column=0, pady=10)
        self.merge_button.grid(row=2, column=0, pady=10)

        self.image_canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas2.grid(row=0, column=0, sticky="nsew")
        self.image_extract_button.grid(row=1, column=0, pady=10)

        self.button_zoom_in.grid(row=3, column=0, sticky="w")
        self.button_zoom_out.grid(row=3, column=1, sticky="e")

        # Configure rows and columns weight for resizing
        self.f1.grid_rowconfigure(0, weight=1)
        self.f1.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    # ... [The rest of the functions remain unchanged]


# ... [The main part of the code remains unchanged]
