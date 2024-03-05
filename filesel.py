class FileDirSelector:
    def __init__(self, parent):
        self.f3 = ttk.Frame(parent)
        self.dirs_list = []
        self.files_list = []
        self.text_widget = tk.Text(self.f3, wrap=tk.WORD)
        self.text_widget.grid(row=5, column=4)
        self.create_widgets()

    def create_widgets(self):
        self.dir_btn = ttk.Button(
            self.f3, text="Select Directory", command=self.select_directory
        )
        self.dir_btn.grid(row=4, column=1)
        self.file_btn = ttk.Button(
            self.f3, text="Select File", command=self.select_file
        )
        self.file_btn.grid(row=5, column=1)
        self.date_entry = tk.Entry(
            self.f3, width=12, background="blue", foreground="white", borderwidth=2
        )
        self.date_entry.grid(row=1, column=1)
        self.print_btn = ttk.Button(
            self.f3, text="Print Selected Items", command=self.print_selected
        )
        self.print_btn.grid(row=4, column=2)

    def select_directory(self):
        dir_name = filedialog.askdirectory()
        if dir_name:
            self.dirs_list.append(dir_name)

    def select_file(self):
        file_name = filedialog.askopenfilename()
        if file_name:
            self.files_list.append(file_name)

    def print_selected(self):
        self.text_widget.insert("1.0", "Selected Directories:\n")
        for d in self.dirs_list:
            self.text_widget.insert(tk.END, d + "\n")
        self.text_widget.insert(tk.END, "\nSelected Files:\n")
        for f in self.files_list:
            self.text_widget.insert(tk.END, f + "\n")
