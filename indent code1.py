import tkinter as tk


def indent_text():
    # Get the indices of the highlighted text
    start_index = text.index(tk.SEL_FIRST)
    end_index = text.index(tk.SEL_LAST)

    # Create a tag with left margin properties
    text.tag_configure("indent", lmargin1="20m", lmargin2="20m")

    # Apply the tag to the highlighted text
    text.tag_add("indent", start_index, end_index)


root = tk.Tk()
text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text.pack()

# Insert some text
text.insert(tk.END, "Highlight some text and then press the button to indent it.")

# Create a button to trigger the indentation
button = tk.Button(root, text="Indent Text", command=indent_text)
button.pack()

root.mainloop()
