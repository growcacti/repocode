import tkinter as tk
from tkinter import ttk

def indent_text():
    text.tag_configure("indent", lmargin1=30)
    apply_indent_dedent()

def dedent_text():
    text.tag_configure("indent", lmargin1=0)
    apply_indent_dedent()

def apply_indent_dedent(self):
    sel_start, sel_end = text.tag_ranges(tk.SEL)
    if sel_start and sel_end:
        text.tag_add("indent", sel_start, sel_end)

def change_indent_spaces(self):
    spaces = int(indent_spaces.get())
    text.tag_configure("indent", lmargin1=spaces * 7)  # Assuming 1 indentation level is equal to 4 spaces.
    apply_indent_dedent()
def apply_indent_dedent(self):
    sel_start, sel_end = text.tag_ranges(tk.SEL)
    if sel_start and sel_end:
        text.tag_add("indent", sel_start, sel_end)
app = tk.Tk()
app.title("Text Widget Indentation")

text = tk.Text(app, wrap="word")
text.pack(expand=True, fill="both")

# Buttons for indenting and de-denting
indent_button = ttk.Button(app, text="Indent", command=indent_text)
indent_button.pack(side="left", padx=5, pady=5)

dedent_button = ttk.Button(app, text="De-dent", command=dedent_text)
dedent_button.pack(side="left", padx=5, pady=5)

# Option to change indent spaces
indent_label = ttk.Label(app, text="Indent Spaces:")
indent_label.pack(side="left", padx=5, pady=5)

indent_spaces = tk.StringVar()
indent_spacedefdef apply_indent_dedent():
    sel_start, sel_end = text.tag_ranges(tk.SEL)
    if sel_start and sel_end:
        text.tag_add("indent", sel_start, sel_end) apply_indent_dedent():
    sel_start, sel_end = text.tag_ranges(tk.SEL)
    if sel_start and sel_end:
        text.tag_add("indent", sel_start, sel_end)s.set("4")  # Default indent spaces
indent_entry = ttk.Spinbox(app, textvariable=indent_spaces)
indent_entry.pack(side="left", padx=5, pady=5)

change_button = ttk.Button(app, text="Change", command=change_indent_spaces)
change_button.pack(side="left", padx=5, pady=5)

app.mainloop()
