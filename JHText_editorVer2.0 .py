import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, messagebox, filedialog
import os

root = tk.Tk()
root.title("An Editter")
root.geometry("700x700")

# ********************************************* Main Menu ************************************************
main_menu = tk.Menu()

# INSERTING IMAGES
file = tk.Menu(main_menu, tearoff=True)


edit = tk.Menu(main_menu, tearoff=True)


view = tk.Menu(main_menu, tearoff=True)

theme_choice = tk.StringVar()


color = tk.Menu(main_menu, tearoff=True)


color_dict = {
    "Light Default": (
        "#000000",
        "#ffffff",
    ),  # here there is text color and backgrund color
    "Light Plus": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Greygarious Grey": ("83406a.d1d4d1"),
    "Lovely Lavender": ("202b4b.e1e1ff"),
    "Aquamarine": ("5b8340.d1e7e0"),
    "Bold Beige": ("4b4620.fff0e1"),
    "Cobalt Blue": ("ffffBB.3333aa"),
    "Olive Green": ("d1e7e0.5b8340"),
}


# ******cascades******
main_menu.add_cascade(label="Files", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Colors", menu=color)
# ***********************************************End of Main menu*******************************************


# *********************************************Toolbar************************************************
tool_bar = ttk.Label(root)
tool_bar.grid(row=0, column=1)

# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_combo = ttk.Combobox(
    tool_bar, width=25, state="readonly", textvariable=font_family
)
font_combo["values"] = font_tuple
font_combo.grid(row=0, column=0, padx=4)
font_combo.current(font_tuple.index("Arial"))

# size box
size_var = tk.IntVar()
size_combo = ttk.Combobox(tool_bar, width=15, textvariable=size_var, state="readonly")
size_combo["values"] = tuple(range(5, 50, 3))
size_combo.grid(row=0, column=1, padx=4)
size_combo.current(3)

# now creating all the buttons


bold_button = ttk.Button(tool_bar, text="Bold")
bold_button.grid(row=0, column=2, padx=4)

italic_button = ttk.Button(tool_bar, text="italic")
italic_button.grid(row=0, column=3, padx=4)

underline_button = ttk.Button(tool_bar, text="underline")
underline_button.grid(row=0, column=4, padx=4)

font_color_button = ttk.Button(tool_bar, text="Font Color")
font_color_button.grid(row=0, column=5, padx=4)

align_left_button = ttk.Button(tool_bar, text="JustLeft")
align_left_button.grid(row=0, column=6, padx=4)

align_center_button = ttk.Button(tool_bar, text="Center")
align_center_button.grid(row=0, column=7, padx=4)

align_right_button = ttk.Button(tool_bar, text="RightJust")
align_right_button.grid(row=0, column=8, padx=4)
# ***********************************************End of Tool bar******************************************
# *********************************************************************************************************


# *********************************************Text Editor************************************************
text = tk.Text(root)
text.config(wrap="word", relief=tk.FLAT)
text.focus_set()

scroll_bar = tk.Scrollbar(root)
scroll_bar.grid(row=2, column=4)
text.grid(row=2, column=1)
scroll_bar.config(command=text.yview)
text.config(yscrollcommand=scroll_bar.set)

# font family and font size functionalities
current_font_family = "Arial"
current_font_size = 12


def change_font(root):
    global current_font_family
    current_font_family = font_family.get()
    text.configure(font=(current_font_family, current_font_size))


def change_size(root):
    global current_font_size
    current_font_size = size_var.get()
    text.configure(font=(current_font_family, current_font_size))


font_combo.bind("<<ComboboxSelected>>", change_font)
size_combo.bind("<<ComboboxSelected>>", change_size)

# ****************buttons functionality
def change_bold():
    text_property = tk.font.Font(font=text["font"])
    if text_property.actual()["weight"] == "normal":
        text.configure(font=(current_font_family, current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text.configure(font=(current_font_family, current_font_size, "normal"))


bold_button.configure(command=change_bold)

# italic functionality
def change_italic():
    italic = tk.font.Font(font=text["font"])
    if italic.actual()["slant"] == "roman":
        text.configure(font=(current_font_family, current_font_size, "italic"))
    if italic.actual()["slant"] == "italic":
        text.configure(font=(current_font_family, current_font_size, "roman"))


italic_button.configure(command=change_italic)

# underline functionality
def change_underline():
    underline = tk.font.Font(font=text["font"])
    if underline.actual()["underline"] == 0:
        text.configure(font=(current_font_family, current_font_size, "underline"))
    if underline.actual()["underline"] == 1:
        text.configure(font=(current_font_family, current_font_size, "normal"))


underline_button.configure(command=change_underline)

# color functionality
def color_change():
    color = tk.colorchooser.askcolor()
    text.configure(fg=color[1])
    font_color_button.configure(command=color_change)


# now we will do allignment
def left():
    text_content = text.get(1.0, "end")
    text.tag_config("left", justify=tk.LEFT)
    text.delete(1.0, tk.END)
    text.insert(tk.INSERT, text_content, "left")
    align_left_button.configure(command=left)


def center():
    text_content = text.get(1.0, "end")
    text.tag_config("center", justify=tk.CENTER)
    text.delete(1.0, tk.END)
    text.insert(tk.INSERT, text_content, "center")
    align_center_button.configure(command=center)


def right():
    text_content = text.get(1.0, "end")
    text.tag_config("right", justify=tk.RIGHT)
    text.delete(1.0, tk.END)
    text.insert(tk.INSERT, text_content, "right")
    align_right_button.configure(command=right)
    text.configure(font=("Arial", 12))


# # ***********************************************End of Text editor******************************************

# ************************************************Status bar***************************************************


def select_all(event=None):
    content_text.tag_add("sel", "1.0", "end")
    return "break"


def about():
    tkinter.messagebox.showinfo(
        "About",
        "{}{}".format(
            PROGRAM_NAME,
            "\nThis is a Text Editor application still in development JH APPS 2021",
        ),
    )


def help():
    tkinter.messagebox.showinfo("Help", "")


def show_info_bar():
    val = showinbar.get()
    if val:
        line_number_bar.pack(expand=NO, fill=None, side=RIGHT, anchor="se")
    elif not val:
        "<<ListboxSelect>>", line_number_bar.pack_forget()


def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()


def on_content_changed(event=None):
    update_line_numbers()
    update_cursor_info_bar()


def show_cursor_info_bar():
    show_cursor_info_checked = showinbar.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand="no", fill=None, side="right", anchor="se")
    else:
        cursor_info_bar.pack_forget()


def get_line_numbers():
    output = ""
    if showinbar.get():
        row, col = content_text.index("end").split(".")
        for i in range(1, int(row)):
            output += str(i) + "\n"
    return output


def update_cursor_info_bar(event=None):
    row, col = content_text.index(INSERT).split(".")
    line_num, col_num = str(int(row)), str(int(col) + 1)
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


def showcontent(event=None):
    lbox.focus_set()
    file_name = input_file_name
    file = lbox.curselection()
    filename = lbox.get(file)
    with open(file_name) as f:
        content_text.insert(1.0, f.read())


def changed(event=None):
    global text_changed
    if text.edit_modified():
        text_changed = True
        words = len(text.get(1.0, "end-1c").split())
        characters = len(text.get(1.0, "end-1c"))
        status_bar.config(text=f"Characters:{characters}  Words : {words} ")
    text.edit_modified(False)


text.bind("<<Modified>>", changed)
# ************************************************End of status bar********************************************

# ************************************************Main menu functionality***********************************
url = ""  # variable

# new functionality
def new_file(event=None):
    global url
    url = ""
    text.delete(1.0, tk.END)


# file new command
file.add_command(label="New", compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)

# open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    try:
        with open(url, "r") as fr:
            text.delete(1.0, tk.END)
            text.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))


# open command
file.add_command(
    label="Open", compound=tk.LEFT, accelerator="Ctrl+O", command=open_file
)
file.add_separator()

# functionality to save a file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(
                mode="w",
                defaultextension=".txt",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
            )
            content = text.get(1.0, tk.END)
            url.write(content)
            url.close()
    except:
        return


# save command
file.add_command(
    label="Save", compound=tk.LEFT, accelerator="Ctrl+S", command=save_file
)

# save as functionality
def save_as(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(
            mode="w",
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
        )
        content = text.get(1.0, tk.END)
        url.write(content)
        url.close()
    except:
        return


# save as command
file.add_command(
    label="Save As", compound=tk.LEFT, accelerator="Ctrl+S", command=save_as
)
file.add_separator()

# Exit command functionality
def exit_fun(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel(
                "Warning!", "Do you want to save your file?"
            )
            if mbox:
                if url:
                    content = str(text.get(1.0, tk.END))
                    with open(url, "w", encoding="utf-8") as wf:
                        wf.write(content)
                        root.destroy()
                else:
                    url = filedialog.asksaveasfile(
                        mode="w",
                        defaultextension=".txt",
                        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
                    )
                    content2 = text.get(1.0, tk.END)
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


# exit command
file.add_command(label="Exit", compound=tk.LEFT, accelerator="Ctrl+Z", command=exit_fun)

# edit commands adding functionality
# find functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text.tag_config("match", foreground="red", background="yellow")

    def replace():
        word = find_input.get()
        replace_content = replace_input.get()
        content = text.get(1.0, tk.END)
        new_content = content.replace(word, replace_content)
        text.delete(1.0, tk.END)
        text.insert(1.0, new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry("450x250+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0, 0)

    find_frame = ttk.Labelframe(find_dialog, text="Find/Replace")
    find_frame.grid(row=1, column=1)

    # labels
    text_find_label = ttk.Label(find_frame, text="Find: ")
    text_replace_label = ttk.Label(find_frame, text="Replace")
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    # entry boxes
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    # buttons
    find_button = ttk.Button(find_frame, text="Find", command=find)
    replace_button = ttk.Button(find_frame, text="Replace", command=replace)
    find_button.grid(row=2, column=0, padx=4, pady=4)
    replace_button.grid(row=2, column=1, padx=4, pady=4)


edit.add_command(
    label="Copy",
    compound=tk.LEFT,
    accelerator="Ctrl+C",
    command=lambda: text.event_generate("<Control c>"),
)
edit.add_command(
    label="Paste",
    compound=tk.LEFT,
    accelerator="Ctrl+V",
    command=lambda: text.event_generate("<Control v>"),
)
edit.add_command(
    label="Cut",
    compound=tk.LEFT,
    accelerator="Ctrl+X",
    command=lambda: text.event_generate("<Control x>"),
)
edit.add_separator()

edit.add_command(
    label="Find", compound=tk.LEFT, accelerator="Ctrl+F", command=find_func
)

# view checkbuttons

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.grid_forget()
        show_toolbar = False
    else:
        text.grid_forget()
        status_bar.grid_forget()
        tool_bar.grid(row=0, column=2)
        text.grid(row=1, column=3)
        status_bar.grid(row=1, column=1)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.grid_forget()
        show_statusbar = False
    else:
        status_bar.grid(row=50, column=1)
        show_statusbar = True


view.add_checkbutton(
    label="Status Bar",
    onvalue=True,
    offvalue=False,
    variable=show_statusbar,
    compound=tk.LEFT,
    command=hide_statusbar,
)
view.add_checkbutton(
    label="Tool bar",
    onvalue=True,
    offvalue=False,
    variable=show_toolbar,
    compound=tk.LEFT,
    command=hide_toolbar,
)

# color Theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color.add_radiobutton(
        label=i, variable=theme_choice, compound=tk.LEFT, command=change_theme
    )
    count += 1


# ********************************************End of Main Menu Functionality*********************************
root.config(menu=main_menu)

# binding shortcut keys
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as)
root.bind("<Control-f>", find_func)
root.bind("<Control-q>", exit_fun)

root.mainloop()
