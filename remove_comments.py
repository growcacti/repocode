import tkinter as tk

def remove_text_after_hash_every_line():
    # Get the total number of lines in the Text widget
    total_lines = int(textwidget.index('end-1c').split('.')[0])
    
    for line_number in range(1, total_lines + 1):
        # Get the content of the current line
        line_content = textwidget.get(f"{line_number}.0", f"{line_number}.end")
        
        # Find the position of the first '#' character in the line
        hash_position = line_content.find('#')
        
        # If '#' is found, delete the text after it until the end of the line
        if hash_position != -1:
            textwidget.delete(f"{line_number}.{hash_position}", f"{line_number}.end")

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Create a Text widget
textwidget = tk.Text(root, height=10, width=40)
textwidget.pack(pady=20)

# Create a Button widget, which calls the remove_text_after_hash_every_line function when clicked
button = tk.Button(root, text="Remove Text After # in All Lines", command=remove_text_after_hash_every_line)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
