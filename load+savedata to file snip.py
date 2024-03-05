def save_to_file():
    with open("DATA.txt", "w") as file:
        for data in lb.get(0, tk.END):
            file.write(data + "\n")
            
save_btn = tk.Button(root, text="Save to File", command=save_to_file)
save_btn.grid(row=7, column=1)



def load_from_file():
    if not os.path.exists("data.txt"):
        showinfo("Error", "File not found!")
        return
    
    with open("Data.txt", "r") as file:
        data = file.readlines()
        
    lb.delete(0, tk.END)  # Clear the listbox
    for data in datas:
        lb.insert(tk.END, data.strip())  # .strip() removes the newline character
    
load_btn = tk.Button(root, text="Load from File", command=load_from_file)
load_btn.grid(row=8, column=1)
