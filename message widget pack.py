import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

message = tk.Message(text="This is a message", relief=tk.SUNKEN)
message.pack()

app.mainloop()
