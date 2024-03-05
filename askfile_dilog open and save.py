from tkinter import filedialog

source = filedialog.askopenfile(
    mode='r',
    title='Select  imagefile',
    filetypes=[('jpg', '*.png *bmp')])

if not source:
    exit()

destination = filedialog.asksaveasfile(
    mode='w',
    title='Select a destination file',
    defaultextension='.csv',
    filetypes=[('png', '*.jpg *.bmp')])

destination.write(source.read())
source.close()
destination.close()
