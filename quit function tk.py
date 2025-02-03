def quit(self):
        if messagebox.askokcancel("Quit?", "Really quit?"):
            self.root.destroy()
