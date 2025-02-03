
import re
import tkinter as tk
from tkinter import ACTIVE, END, Entry, Listbox, StringVar, Tk
from tkinter import *

class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*',
                                     re.IGNORECASE)
                return re.match(pattern, acListEntry)

            self.matchesFunction = matches


        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)

        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"],
                                           height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(),
                                       y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False

    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]
    
if __name__ == '__main__':
    autocompleteList =[ 'john.hewitt@cox.net',
                        'john.hewitt1970@gmail.com',
                        '1073 N 84th Place',
						'Scottsdale',
						"AZ",
						"85257",
						"john.hewitt",
                        '602-376-2119',
						
                       ]

    def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)
    def cl():
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(entry.get())
        root.update() # now it stays on the clipboard after the window is closed
        #r.destroy()
    root = Tk()
    root.title('Autocomplete Demo')
    root.geometry('300x200')
    
    entry = AutocompleteEntry(autocompleteList, root, listboxLength=6,
                              width=32, matchesFunction=matches)
    entry.grid(row=0, column=0)
    btn1 = tk.Button(root, text="send to clipboardz", command=cl)
    btn1.grid(row=2, column=1)


    root.mainloop()
