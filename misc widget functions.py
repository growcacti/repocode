def clickMe(button, name, number):
    button.configure(text='Hello {} {}'.format(name.get(), number.get()))

# Button callback Clear Text   
def clearScrol(scr):
    scr.delete('1.0', tk.END)    

# Spinbox callback 
def _spin(spin, scr):
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Checkbox callback  
def checkCallback(*ignoredArgs):
    pass

#------------------------------------------
def create_display_area():
    # add empty label for spacing 
    display_area_label = tk.Label(display_area, text="", height=2)
    display_area_label.grid(column=0, row=0)
    
    # Creating three checkbuttons
    chVarDis = tk.IntVar()
    check1 = tk.Checkbutton(ctrl_tab2, text="Disabled", variable=chVarDis, state='disabled')
    check1.select()
    check1.grid(column=0, row=0, sticky=tk.W)                 
    
    chVarUn = tk.IntVar()
    check2 = tk.Checkbutton(ctrl_tab2, text="UnChecked", variable=chVarUn)
    check2.deselect()
    check2.grid(column=1, row=0, sticky=tk.W )                  
     
    chVarEn = tk.IntVar()
    check3 = tk.Checkbutton(ctrl_tab2, text="Toggle", variable=chVarEn)
    check3.deselect()
    check3.grid(column=2, row=0, sticky=tk.W)                 

    # Create a container to hold labels
    labelsFrame = ttk.LabelFrame(ctrl_tab2, text=' Labels in a Frame ')
    labelsFrame.grid(column=0, row=7)
     
    # Place labels into the container element - vertically
    ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
    ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
    
    # Add some space around each label
    for child in labelsFrame.winfo_children(): 
        child.grid_configure(padx=8)
        # Container frame to hold all other widgets
    ctrl_tab = ttk.LabelFrame(display_area, text=' Mighty Python ')
    ctrl_tab.grid(column=0, row=0, padx=8, pady=4)
    
    # Adding a Label
    ttk.Label(ctrl_tab, text="Enter a name:").grid(column=0, row=0, sticky='W')
    
    # Adding a Textbox Entry widget
    name = tk.StringVar()
    nameEntered = ttk.Entry(ctrl_tab, width=12, textvariable=name)
    nameEntered.grid(column=0, row=1, sticky='W')
    
    ttk.Label(ctrl_tab, text="Choose a number:").grid(column=1, row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(ctrl_tab, width=12, textvariable=number)
    numberChosen['values'] = (1, 2, 4, 42, 100)
    numberChosen.grid(column=1, row=1)
    numberChosen.current(0)

    # Adding a Button
    action = ttk.Button(ctrl_tab, text="Click Me!", command= lambda: clickMe(action, name, number))   
    action.grid(column=2, row=1)
    
    # Using a scrolled Text control    
    scrolW  = 30; scrolH  =  3
    scr = scrolledtext.ScrolledText(ctrl_tab, width=scrolW, height=scrolH, wrap=tk.WORD)
    scr.grid(column=0, row=3, sticky='WE', columnspan=3)  
             
    # Adding a Spinbox widget using a set of values
    spin = Spinbox(ctrl_tab, values=(1, 2, 4, 42, 100), width=5, bd=8, command= lambda: _spin(spin, scr)) 
    spin.grid(column=0, row=2, sticky='W')  
  
    # Adding another Button
    clear = ttk.Button(ctrl_tab, text="Clear Text", command= lambda: clearScrol(scr))   
    clear.grid(column=2, row=2)

    # Adding more Feature Buttons
    startRow = 4
    for idx in range(12):
        if idx < 2:
            colIdx = idx
            col = colIdx
        else:
            col += 1
        if not idx % 3: 
            startRow += 1
            col = 0

        b = ttk.Button(ctrl_tab, text="Feature " + str(idx+1))   
        b.grid(column=col, row=startRow)   
            
ctrl_tab2 = ttk.LabelFrame(display_area, text=' Holy Grail ')
    ctrl_tab2.grid(column=0, row=0, padx=8, pady=4)
    

