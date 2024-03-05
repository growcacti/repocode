import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')


def value_changed(event):
    msg = f'You selected {value_cb.get()}!'
    showinfo(title='Result', message=msg)


# Values
value = ('')

label = ttk.Label(text="Please select a value:")
label.pack(fill='x', padx=5, pady=5)

# create a combobox
selected_value = tk.StringVar()

value_cb = ttk.Combobox(root, textvariable=selected_value)
value_cb['values'] = values
value_cb['state'] = 'readonly'  # normal
value_cb.pack(fill='x', padx=5, pady=5)

value_cb.bind('<<ComboboxSelected>>', value_changed)

root.mainloop()
