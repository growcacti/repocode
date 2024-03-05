 1 from Tkinter import *
 2 
 3 field_value = "Field value to output"  # returned from another part of the code
 4 
 5 # triggered off left button click on text_field
 6 def copy_text_to_clipboard(event):
 7    field_value = event.widget.get("1.0", 'end-1c')  # get field value from event, but remove line return at end
 8    window.clipboard_clear()  # clear clipboard contents
 9    window.clipboard_append(field_value)  # append new value to clipbaord
10 
11 window = Tk()
12     
13 # setup frame and grid
14 frame = Frame(window)
15 frame.grid()
16 
17 # setup our inline label and widget
18 Label(frame, text="Field Label").grid(row=0, column=0)
19 text_field = Text(frame, height=1, borderwidth=0)
20 text_field.insert(1.0, field_value)
21 text_field.grid(row=0, column=1)
22 
23 # Bind left click on text widget to copy_text_to_clipboard() function
24 text_field.bind("<Button-1>", copy_text_to_clipboard)  
25 window.mainloop()
