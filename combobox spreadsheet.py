import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1900x1000")
root.title("Notebook Spreadsheet")


def command():
    pass


nb = ttk.Notebook(root)
nb.grid(row=0, column=0)
f1 = ttk.Frame(nb)
# Begin NoteBook SpreadSheet in TAB 1

listedstuff = ["subprocess.Popen", "for item in items", "filename"]

nb.add(f1, text="First")
r0c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c1.grid(row=0, column=1)

r1c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c1.grid(row=1, column=1)

r2c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c1.grid(row=2, column=1)

r3c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c1.grid(row=3, column=1)

r4c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c1.grid(row=4, column=1)

r5c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r5c1.grid(row=5, column=1)

r6c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r6c1.grid(row=6, column=1)

r7c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r7c1.grid(row=7, column=1)

r8c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r8c1.grid(row=8, column=1)

r9c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r9c1.grid(row=9, column=1)

r10c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r10c1.grid(row=10, column=1)

r11c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r11c1.grid(row=11, column=1)

r12c1 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r12c1.grid(row=12, column=1)

########################

r0c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c2.grid(row=0, column=2)

r1c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c2.grid(row=1, column=2)

r2c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c2.grid(row=2, column=2)

r3c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c2.grid(row=3, column=2)

r4c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c2.grid(row=4, column=2)

r5c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r5c2.grid(row=5, column=2)

r6c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r6c2.grid(row=6, column=2)

r7c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r7c2.grid(row=7, column=2)

r8c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r8c2.grid(row=8, column=2)

r9c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r9c2.grid(row=9, column=2)

r10c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r10c2.grid(row=10, column=2)

r11c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r11c2.grid(row=11, column=2)

r12c2 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r12c2.grid(row=12, column=2)

##############################

r0c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c3.grid(row=0, column=3)

r1c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c3.grid(row=1, column=3)

r2c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c3.grid(row=2, column=3)

r3c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c3.grid(row=3, column=3)

r4c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c3.grid(row=4, column=3)

r5c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r5c3.grid(row=5, column=3)

r6c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r6c3.grid(row=6, column=3)

r7c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r7c3.grid(row=7, column=3)

r8c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r8c3.grid(row=8, column=3)

r9c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r9c3.grid(row=9, column=3)

r10c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r10c3.grid(row=10, column=3)

r11c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r11c3.grid(row=11, column=3)

r12c3 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r12c3.grid(row=12, column=3)

################################
r0c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c4.grid(row=0, column=4)

r1c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c4.grid(row=1, column=4)

r2c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c4.grid(row=2, column=4)

r3c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c4.grid(row=3, column=4)

r4c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c4.grid(row=4, column=4)

r5c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r5c4.grid(row=5, column=4)

r6c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r6c4.grid(row=6, column=4)

r7c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r7c4.grid(row=7, column=4)

r8c4 = ttk.Combobox(f1, values=listedstuff)
r8c4.grid(row=8, column=4)

r9c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r9c4.grid(row=9, column=4)

r10c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r10c4.grid(row=10, column=4)

r11c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r11c4.grid(row=11, column=4)

r12c4 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r12c4.grid(row=12, column=4)

###############################

r0c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c5.grid(row=0, column=5)

r1c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c5.grid(row=1, column=5)

r2c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c5.grid(row=2, column=5)

r3c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c5.grid(row=3, column=5)

r4c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c5.grid(row=4, column=5)

r5c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r5c5.grid(row=5, column=5)

r6c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r6c5.grid(row=6, column=5)

r7c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r7c5.grid(row=7, column=5)

r8c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r8c5.grid(row=8, column=5)

r9c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r9c5.grid(row=9, column=5)

r10c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r10c5.grid(row=10, column=5)

r11c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r11c5.grid(row=11, column=5)

r12c5 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r12c5.grid(row=12, column=5)

#############################

r0c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r0c6.grid(row=0, column=6)

r1c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r1c6.grid(row=1, column=6)

r2c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r2c6.grid(row=2, column=6)

r3c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r3c6.grid(row=3, column=6)

r4c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r4c6.grid(row=4, column=6)

r5c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r5c6.grid(row=5, column=6)

r6c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r6c6.grid(row=6, column=6)

r7c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r7c6.grid(row=7, column=6)

r8c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r8c6.grid(row=8, column=6)

r9c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r9c6.grid(row=9, column=6)

r10c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r10c6.grid(row=10, column=6)

r11c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r11c6.grid(row=11, column=6)

r12c6 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r12c6.grid(row=12, column=6)

###############################

r0c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r0c7.grid(row=0, column=7)

r1c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r1c7.grid(row=1, column=7)

r2c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r2c7.grid(row=2, column=7)

r3c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r3c7.grid(row=3, column=7)

r4c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r4c7.grid(row=4, column=7)

r5c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r5c7.grid(row=5, column=7)

r6c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r6c7.grid(row=6, column=7)

r7c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r7c7.grid(row=7, column=7)

r8c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r8c7.grid(row=8, column=7)

r9c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r9c7.grid(row=9, column=7)

r10c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r10c7.grid(row=10, column=7)

r11c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r11c7.grid(row=11, column=7)

r12c7 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r12c7.grid(row=12, column=7)

############################

r0c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c8.grid(row=0, column=8)

r1c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c8.grid(row=1, column=8)

r2c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c8.grid(row=2, column=8)

r3c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c8.grid(row=3, column=8)

r4c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c8.grid(row=4, column=8)

r5c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r5c8.grid(row=5, column=8)

r6c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r6c8.grid(row=6, column=8)

r7c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r7c8.grid(row=7, column=8)

r8c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r8c8.grid(row=8, column=8)

r9c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r9c8.grid(row=9, column=8)

r10c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r10c8.grid(row=10, column=8)

r11c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r11c8.grid(row=11, column=8)

r12c8 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r12c8.grid(row=12, column=8)

#############################


r0c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r0c9.grid(row=0, column=9)

r1c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r1c9.grid(row=1, column=9)

r2c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r2c9.grid(row=2, column=9)

r3c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r3c9.grid(row=3, column=9)

r4c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)
r4c9.grid(row=4, column=9)

r5c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r5c9.grid(row=5, column=9)

r6c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r6c9.grid(row=6, column=9)

r7c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r7c9.grid(row=7, column=9)

r8c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r8c9.grid(row=8, column=9)

r9c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r9c9.grid(row=9, column=9)

r10c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r10c9.grid(row=10, column=9)

r11c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r11c9.grid(row=11, column=9)

r12c9 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r12c9.grid(row=12, column=9)

################################

r0c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r0c10.grid(row=0, column=10)

r1c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r1c10.grid(row=1, column=10)

r2c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r2c10.grid(row=2, column=10)

r3c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r3c10.grid(row=3, column=10)

r4c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r4c10.grid(row=4, column=10)

r5c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r5c10.grid(row=5, column=10)

r6c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r6c10.grid(row=6, column=10)

r7c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r7c10.grid(row=7, column=10)

r8c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r8c10.grid(row=8, column=10)

r9c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r9c10.grid(row=9, column=10)

r10c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r10c10.grid(row=10, column=10)

r11c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r11c10.grid(row=11, column=10)

r12c10 = ttk.Combobox(
    f1,
    values=listedstuff,
)

r12c10.grid(row=12, column=10)

################################


##r0c11 = ttk.Combobox(f1, values=listedstuff,  )

##r0c11.grid(row=0, column=11)

##r1c11 = ttk.Combobox(f1, values=listedstuff,  )

##r1c11.grid(row=1, column=11)

##r2c11 = ttk.Combobox(f1, values=listedstuff,  )

##r2c11.grid(row=2, column=11)

##r3c11 = ttk.Combobox(f1, values=listedstuff,  )

##r3c11.grid(row=3, column=11)

##r4c11 = ttk.Combobox(f1, values=listedstuff,  )

##r4c11.grid(row=4, column=11)

##r5c11 = ttk.Combobox(f1, values=listedstuff,  )

##r5c11.grid(row=5, column=11)

##r6c11 = ttk.Combobox(f1, values=listedstuff,  )

##r6c11.grid(row=6, column=11)

##r7c11 = ttk.Combobox(f1, values=listedstuff,  )

##r7c11.grid(row=7, column=11)

##r8c11 = ttk.Combobox(f1, values=listedstuff,  )

##r8c11.grid(row=8, column=11)

##r9c11 = ttk.Combobox(f1, values=listedstuff,  )

##r9c11.grid(row=9, column=11)

####r10c11 = ttk.Combobox(f1, values=listedstuff,  )

##r10c11.grid(row=10, column=11)

##r11c11 = ttk.Combobox(f1, values=listedstuff,  )

##r11c11.grid(row=11, column=11)

##r12c11 = ttk.Combobox(f1, values=listedstuff,  )

##r12c11.grid(row=12, column=11)

#################################

##r0c12 = ttk.Combobox(f1, values=listedstuff,  )

##r0c12.grid(row=0, column=12)

##r1c12 = ttk.Combobox(f1, values=listedstuff,  )

##r1c12.grid(row=1, column=12)

##r2c12 = ttk.Combobox(f1, values=listedstuff,  )

##r2c12.grid(row=2, column=12)

##r3c12 = ttk.Combobox(f1, values=listedstuff,  )

##r3c12.grid(row=3, column=12)

##r4c12 = ttk.Combobox(f1, values=listedstuff,  )

##r4c12.grid(row=4, column=12)

##r5c12 = ttk.Combobox(f1, values=listedstuff,  )

##r5c12.grid(row=5, column=12)

##r6c12 = ttk.Combobox(f1, values=listedstuff,  )

##r6c12.grid(row=6, column=12)

##r7c12 = ttk.Combobox(f1, values=listedstuff,  )

##r7c12.grid(row=7, column=12)

##r8c12 = ttk.Combobox(f1, values=listedstuff,  )

##r8c12.grid(row=8, column=12)

##r9c12 = ttk.Combobox(f1, values=listedstuff,  )

##r9c12.grid(row=9, column=12)

##r12c12 = ttk.Combobox(f1, values=listedstuff,  )

##r12c12.grid(row=10, column=12)

##r12c12 = ttk.Combobox(f1, values=listedstuff,  )

##r12c12.grid(row=11, column=12)

##r12c12 = ttk.Combobox(f1, values=listedstuff,  )

##r12c12.grid(row=12, column=12)

###############################


##r0c0 = ttk.Combobox(f1)

##r0c0.grid(row=0, column=0)

##r0c0 = ttk.Combobox(f1)

##r0c0.grid(row=0, column=0)

##r0c0 = ttk.Combobox(f1)

##r0c0.grid(row=0, column=0)

##r0c0 = ttk.Combobox(f1)

##r0c0.grid(row=0, column=0)

##r0c0 = ttk.Combobox(f1)

##r0c0.grid(row=0, column=0)

##r0c0 = ttk.Combobox(f1)

##r0c0.grid(row=0, column=0)


# cb.bind("<FocusIn>", defocus)


# combo_box.bind("<<ComboboxSelected>>"


##################################################################

# The is the start of the 2nd tab which is also the 2nd frame f2 and the container

###################################################################

f2 = ttk.Frame(nb)


nb.add(f2, text="Second")

r0c1 = ttk.Combobox(f2, bg="#847bb1")

r0c1.grid(row=0, column=1)

r1c1 = ttk.Combobox(f2, bg="#847bb1")

r1c1.grid(row=1, column=1)

r2c1 = ttk.Combobox(f2, bg="#847bb1")

r2c1.grid(row=2, column=1)

r3c1 = ttk.Combobox(f2, bg="#847bb1")

r3c1.grid(row=3, column=1)

r4c1 = ttk.Combobox(f2, bg="#847bb1")

r4c1.grid(row=4, column=1)

r5c1 = ttk.Combobox(f2, bg="#847bb1")

r5c1.grid(row=5, column=1)

r6c1 = ttk.Combobox(f2, bg="#847bb1")

r6c1.grid(row=6, column=1)

r7c1 = ttk.Combobox(f2, bg="#847bb1")

r7c1.grid(row=7, column=1)

r8c1 = ttk.Combobox(f2, bg="#847bb1")

r8c1.grid(row=8, column=1)

r9c1 = ttk.Combobox(f2, bg="#847bb1")

r9c1.grid(row=9, column=1)

r10c1 = ttk.Combobox(f2, bg="#847bb1")

r10c1.grid(row=10, column=1)

r11c1 = ttk.Combobox(f2, bg="#847bb1")

r11c1.grid(row=11, column=1)

r12c1 = ttk.Combobox(f2, bg="#847bb1")

r12c1.grid(row=12, column=1)

########################

r0c2 = ttk.Combobox(f2, bg="#847bb1")

r0c2.grid(row=0, column=2)

r1c2 = ttk.Combobox(f2, bg="#847bb1")

r1c2.grid(row=1, column=2)

r2c2 = ttk.Combobox(f2, bg="#847bb1")

r2c2.grid(row=2, column=2)

r3c2 = ttk.Combobox(f2, bg="#847bb1")

r3c2.grid(row=3, column=2)

r4c2 = ttk.Combobox(f2, bg="#847bb1")

r4c2.grid(row=4, column=2)

r5c2 = ttk.Combobox(f2, bg="#847bb1")

r5c2.grid(row=5, column=2)

r6c2 = ttk.Combobox(f2, bg="#847bb1")

r6c2.grid(row=6, column=2)

r7c2 = ttk.Combobox(f2, bg="#847bb1")

r7c2.grid(row=7, column=2)

r8c2 = ttk.Combobox(f2, bg="#847bb1")

r8c2.grid(row=8, column=2)

r9c2 = ttk.Combobox(f2, bg="#847bb1")

r9c2.grid(row=9, column=2)

r10c2 = ttk.Combobox(f2, bg="#847bb1")

r10c2.grid(row=10, column=2)

r11c2 = ttk.Combobox(f2, bg="#847bb1")

r11c2.grid(row=11, column=2)

r12c2 = ttk.Combobox(f2, bg="#847bb1")

r12c2.grid(row=12, column=2)

##############################

r0c3 = ttk.Combobox(f2, bg="#847bb1")

r0c3.grid(row=0, column=3)

r1c3 = ttk.Combobox(f2, bg="#847bb1")

r1c3.grid(row=1, column=3)

r2c3 = ttk.Combobox(f2, bg="#847bb1")

r2c3.grid(row=2, column=3)

r3c3 = ttk.Combobox(f2, bg="#847bb1")

r3c3.grid(row=3, column=3)

r4c3 = ttk.Combobox(f2, bg="#847bb1")

r4c3.grid(row=4, column=3)

r5c3 = ttk.Combobox(f2, bg="#847bb1")

r5c3.grid(row=5, column=3)

r6c3 = ttk.Combobox(f2, bg="#847bb1")

r6c3.grid(row=6, column=3)

r7c3 = ttk.Combobox(f2, bg="#847bb1")

r7c3.grid(row=7, column=3)

r8c3 = ttk.Combobox(f2, bg="#847bb1")

r8c3.grid(row=8, column=3)

r9c3 = ttk.Combobox(f2, bg="#847bb1")

r9c3.grid(row=9, column=3)

r10c3 = ttk.Combobox(f2, bg="#847bb1")

r10c3.grid(row=10, column=3)

r11c3 = ttk.Combobox(f2, bg="#847bb1")

r11c3.grid(row=11, column=3)

r12c3 = ttk.Combobox(f2, bg="#847bb1")

r12c3.grid(row=12, column=3)

################################

r0c4 = ttk.Combobox(f2, bg="#847bb1")

r0c4.grid(row=0, column=4)

r1c4 = ttk.Combobox(f2, bg="#847bb1")

r1c4.grid(row=1, column=4)

r2c4 = ttk.Combobox(f2, bg="#847bb1")

r2c4.grid(row=2, column=4)

r3c4 = ttk.Combobox(f2, bg="#847bb1")

r3c4.grid(row=3, column=4)

r4c4 = ttk.Combobox(f2, bg="#847bb1")

r4c4.grid(row=4, column=4)

r5c4 = ttk.Combobox(f2, bg="#847bb1")

r5c4.grid(row=5, column=4)

r6c4 = ttk.Combobox(f2, bg="#847bb1")

r6c4.grid(row=6, column=4)

r7c4 = ttk.Combobox(f2, bg="#847bb1")

r7c4.grid(row=7, column=4)

r8c4 = ttk.Combobox(f2, bg="#847bb1")

r8c4.grid(row=8, column=4)

r9c4 = ttk.Combobox(f2, bg="#847bb1")

r9c4.grid(row=9, column=4)

r10c4 = ttk.Combobox(f2, bg="#847bb1")

r10c4.grid(row=10, column=4)

r11c4 = ttk.Combobox(f2, bg="#847bb1")

r11c4.grid(row=11, column=4)

r12c4 = ttk.Combobox(f2, bg="#847bb1")

r12c4.grid(row=12, column=4)

###############################

r0c5 = ttk.Combobox(f2, bg="#847bb1")

r0c5.grid(row=0, column=5)

r1c5 = ttk.Combobox(f2, bg="#847bb1")

r1c5.grid(row=1, column=5)

r2c5 = ttk.Combobox(f2, bg="#847bb1")

r2c5.grid(row=2, column=5)

r3c5 = ttk.Combobox(f2, bg="#847bb1")

r3c5.grid(row=3, column=5)

r4c5 = ttk.Combobox(f2, bg="#847bb1")

r4c5.grid(row=4, column=5)

r5c5 = ttk.Combobox(f2, bg="#847bb1")

r5c5.grid(row=5, column=5)

r6c5 = ttk.Combobox(f2, bg="#847bb1")

r6c5.grid(row=6, column=5)

r7c5 = ttk.Combobox(f2, bg="#847bb1")

r7c5.grid(row=7, column=5)

r8c5 = ttk.Combobox(f2, bg="#847bb1")

r8c5.grid(row=8, column=5)

r9c5 = ttk.Combobox(f2, bg="#847bb1")

r9c5.grid(row=9, column=5)

r10c5 = ttk.Combobox(f2, bg="#847bb1")

r10c5.grid(row=10, column=5)

r11c5 = ttk.Combobox(f2, bg="#847bb1")

r11c5.grid(row=11, column=5)

r12c5 = ttk.Combobox(f2, bg="#847bb1")

r12c5.grid(row=12, column=5)

#############################

r0c6 = ttk.Combobox(f2, bg="#847bb1")

r0c6.grid(row=0, column=6)

r1c6 = ttk.Combobox(f2, bg="#847bb1")

r1c6.grid(row=1, column=6)

r2c6 = ttk.Combobox(f2, bg="#847bb1")

r2c6.grid(row=2, column=6)

r3c6 = ttk.Combobox(f2, bg="#847bb1")

r3c6.grid(row=3, column=6)

r4c6 = ttk.Combobox(f2, bg="#847bb1")

r4c6.grid(row=4, column=6)

r5c6 = ttk.Combobox(f2, bg="#847bb1")

r5c6.grid(row=5, column=6)

r6c6 = ttk.Combobox(f2, bg="#847bb1")

r6c6.grid(row=6, column=6)

r7c6 = ttk.Combobox(f2, bg="#847bb1")

r7c6.grid(row=7, column=6)

r8c6 = ttk.Combobox(f2, bg="#847bb1")

r8c6.grid(row=8, column=6)

r9c6 = ttk.Combobox(f2, bg="#847bb1")

r9c6.grid(row=9, column=6)

r10c6 = ttk.Combobox(f2, bg="#847bb1")

r10c6.grid(row=10, column=6)

r11c6 = ttk.Combobox(f2, bg="#847bb1")

r11c6.grid(row=11, column=6)

r12c6 = ttk.Combobox(f2, bg="#847bb1")

r12c6.grid(row=12, column=6)

###############################

r0c7 = ttk.Combobox(f2, bg="#847bb1")

r0c7.grid(row=0, column=7)

r1c7 = ttk.Combobox(f2, bg="#847bb1")

r1c7.grid(row=1, column=7)

r2c7 = ttk.Combobox(f2, bg="#847bb1")

r2c7.grid(row=2, column=7)

r3c7 = ttk.Combobox(f2, bg="#847bb1")

r3c7.grid(row=3, column=7)

r4c7 = ttk.Combobox(f2, bg="#847bb1")

r4c7.grid(row=4, column=7)

r5c7 = ttk.Combobox(f2, bg="#847bb1")

r5c7.grid(row=5, column=7)

r6c7 = ttk.Combobox(f2, bg="#847bb1")

r6c7.grid(row=6, column=7)

r7c7 = ttk.Combobox(f2, bg="#847bb1")

r7c7.grid(row=7, column=7)

r8c7 = ttk.Combobox(f2, bg="#847bb1")

r8c7.grid(row=8, column=7)

r9c7 = ttk.Combobox(f2, bg="#847bb1")

r9c7.grid(row=9, column=7)

r10c7 = ttk.Combobox(f2, bg="#847bb1")

r10c7.grid(row=10, column=7)

r11c7 = ttk.Combobox(f2, bg="#847bb1")

r11c7.grid(row=11, column=7)

r12c7 = ttk.Combobox(f2, bg="#847bb1")

r12c7.grid(row=12, column=7)

############################

r0c8 = ttk.Combobox(f2, bg="#847bb1")

r0c8.grid(row=0, column=8)

r1c8 = ttk.Combobox(f2, bg="#847bb1")

r1c8.grid(row=1, column=8)

r2c8 = ttk.Combobox(f2, bg="#847bb1")

r2c8.grid(row=2, column=8)

r3c8 = ttk.Combobox(f2, bg="#847bb1")

r3c8.grid(row=3, column=8)

r4c8 = ttk.Combobox(f2, bg="#847bb1")

r4c8.grid(row=4, column=8)

r5c8 = ttk.Combobox(f2, bg="#847bb1")

r5c8.grid(row=5, column=8)

r6c8 = ttk.Combobox(f2, bg="#847bb1")

r6c8.grid(row=6, column=8)

r7c8 = ttk.Combobox(f2, bg="#847bb1")

r7c8.grid(row=7, column=8)

r8c8 = ttk.Combobox(f2, bg="#847bb1")

r8c8.grid(row=8, column=8)

r9c8 = ttk.Combobox(f2, bg="#847bb1")

r9c8.grid(row=9, column=8)

r10c8 = ttk.Combobox(f2, bg="#847bb1")

r10c8.grid(row=10, column=8)

r11c8 = ttk.Combobox(f2, bg="#847bb1")

r11c8.grid(row=11, column=8)

r12c8 = ttk.Combobox(f2, bg="#847bb1")

r12c8.grid(row=12, column=8)

#############################


r0c9 = ttk.Combobox(f2, bg="#847bb1")

r0c9.grid(row=0, column=9)

r1c9 = ttk.Combobox(f2, bg="#847bb1")

r1c9.grid(row=1, column=9)

r2c9 = ttk.Combobox(f2, bg="#847bb1")

r2c9.grid(row=2, column=9)

r3c9 = ttk.Combobox(f2, bg="#847bb1")

r3c9.grid(row=3, column=9)

r4c9 = ttk.Combobox(f2, bg="#847bb1")

r4c9.grid(row=4, column=9)

r5c9 = ttk.Combobox(f2, bg="#847bb1")

r5c9.grid(row=5, column=9)

r6c9 = ttk.Combobox(f2, bg="#847bb1")

r6c9.grid(row=6, column=9)

r7c9 = ttk.Combobox(f2, bg="#847bb1")

r7c9.grid(row=7, column=9)

r8c9 = ttk.Combobox(f2, bg="#847bb1")

r8c9.grid(row=8, column=9)

r9c9 = ttk.Combobox(f2, bg="#847bb1")

r9c9.grid(row=9, column=9)

r10c9 = ttk.Combobox(f2, bg="#847bb1")

r10c9.grid(row=10, column=9)

r11c9 = ttk.Combobox(f2, bg="#847bb1")

r11c9.grid(row=11, column=9)

r12c9 = ttk.Combobox(f2, bg="#847bb1")

r12c9.grid(row=12, column=9)

################################

r0c10 = ttk.Combobox(f2, bg="#847bb1")

r0c10.grid(row=0, column=10)

r1c10 = ttk.Combobox(f2, bg="#847bb1")

r1c10.grid(row=1, column=10)

r2c10 = ttk.Combobox(f2, bg="#847bb1")

r2c10.grid(row=2, column=10)

r3c10 = ttk.Combobox(f2, bg="#847bb1")

r3c10.grid(row=3, column=10)

r4c10 = ttk.Combobox(f2, bg="#847bb1")

r4c10.grid(row=4, column=10)

r5c10 = ttk.Combobox(f2, bg="#847bb1")

r5c10.grid(row=5, column=10)

r6c10 = ttk.Combobox(f2, bg="#847bb1")

r6c10.grid(row=6, column=10)

r7c10 = ttk.Combobox(f2, bg="#847bb1")

r7c10.grid(row=7, column=10)

r8c10 = ttk.Combobox(f2, bg="#847bb1")

r8c10.grid(row=8, column=10)

r9c10 = ttk.Combobox(f2, bg="#847bb1")

r9c10.grid(row=9, column=10)

r10c10 = ttk.Combobox(f2, bg="#847bb1")

r10c10.grid(row=10, column=10)

r11c10 = ttk.Combobox(f2, bg="#847bb1")

r11c10.grid(row=11, column=10)

r12c10 = ttk.Combobox(f2, bg="#847bb1")

r12c10.grid(row=12, column=10)


################################


##r0c11 = ttk.Combobox(f2)

##r0c11.grid(row=0, column=11)

##r1c11 = ttk.Combobox(f2)

##r1c11.grid(row=1, column=11)

##r2c11 = ttk.Combobox(f2)

##r2c11.grid(row=2, column=11)

##r3c11 = ttk.Combobox(f2)

##r3c11.grid(row=3, column=11)

##r4c11 = ttk.Combobox(f2)

##r4c11.grid(row=4, column=11)

##r5c11 = ttk.Combobox(f2)

##r5c11.grid(row=5, column=11)

##r6c11 = ttk.Combobox(f2)

##r6c11.grid(row=6, column=11)

##r7c11 = ttk.Combobox(f2)

##r7c11.grid(row=7, column=11)

##r8c11 = ttk.Combobox(f2)

##r8c11.grid(row=8, column=11)

##r9c11 = ttk.Combobox(f2)

##r9c11.grid(row=9, column=11)

####r10c11 = ttk.Combobox(f2)

##r10c11.grid(row=10, column=11)

##r11c11 = ttk.Combobox(f2)

##r11c11.grid(row=11, column=11)

##r12c11 = ttk.Combobox(f2)

##r12c11.grid(row=12, column=11)

#################################

##r0c12 = ttk.Combobox(f2)

##r0c12.grid(row=0, column=12)

##r1c12 = ttk.Combobox(f2)

##r1c12.grid(row=1, column=12)

##r2c12 = ttk.Combobox(f2)

##r2c12.grid(row=2, column=12)

##r3c12 = ttk.Combobox(f2)

##r3c12.grid(row=3, column=12)

##r4c12 = ttk.Combobox(f2)

##r4c12.grid(row=4, column=12)

##r5c12 = ttk.Combobox(f2)

##r5c12.grid(row=5, column=12)

##r6c12 = ttk.Combobox(f2)

##r6c12.grid(row=6, column=12)

##r7c12 = ttk.Combobox(f2)

##r7c12.grid(row=7, column=12)

##r8c12 = ttk.Combobox(f2)

##r8c12.grid(row=8, column=12)

##r9c12 = ttk.Combobox(f2)

##r9c12.grid(row=9, column=12)

##r12c12 = ttk.Combobox(f2)

##r12c12.grid(row=10, column=12)

##r12c12 = ttk.Combobox(f2)

##r12c12.grid(row=11, column=12)

##r12c12 = ttk.Combobox(f2)


##########################################

## TAB3

##########################################


f3 = ttk.Frame(nb)


nb.add(f3, text="Tab3")


Label(f3, text="label").grid(column=0, row=0)


Label(f3, text="label1").grid(column=0, row=0)


Label(f3, text="label1").grid(column=0, row=2)


ee1 = tk.StringVar()


Entry(f3, textvariable=ee1, bg="yellow").grid(column=0, row=3)


Label(f3, text="label1").grid(column=0, row=4)


ee2 = tk.StringVar()


Entry(f3, textvariable=ee2, bg="yellow").grid(column=0, row=5)


##btn1=tk.Button(f1, values=listedstuff,  text='button 1', command=command).grid(column=2, row=1)

##

##btn2=tk.Button(f1, values=listedstuff,  text='button 2', command=command).grid(column=2, row=2)

##

##btn3=tk.Button(f1, values=listedstuff,  text='button 3', command=command).grid(column=2, row=3)

##

##btn4=tk.Button(f1, values=listedstuff,  text='button 4', command=command).grid(column=2, row=4)

##

##btn5=tk.Button(f1, values=listedstuff,  text='button 5', command=command).grid(column=2, row=5)

##

##btn6=tk.Button(f1, values=listedstuff,  text='button 6', command=command).grid(column=3, row=1)

##

##btn7=tk.Button(f1, values=listedstuff,  text='button 7', command=command).grid(column=3, row=2)

##

##btn8u=tk.Button(f1, values=listedstuff,  text='button 8', command=command).grid(column=3, row=3)

##

##btn9=tk.Button(f1, values=listedstuff,  text='button 9', command=command).grid(column=3, row=4)

##

##btn10=tk.Button(f1, values=listedstuff,  text='button 10', command=command).grid(column=3, row=5)  command=command).grid(column=2, row=4)

##

##btn5=tk.Button(f1, values=listedstuff,  text='button 5', command=command).grid(column=2, row=5)


text = tk.Text(f3, bg="pink", height=500, width=1000)


text.insert("1.0", tk.END)


text.grid(row=1, column=4, rowspan=5, columnspan=10)


#########################################

# TAB4

##########################################


def termsCheck():

    if ckb.get() == 1:

        submit_btn["state"] = NORMAL

    else:

        submit_btn["state"] = DISABLED

        messagebox.showerror("Accept the terms & conditions")


##

##

##f4 = ttk.Frame(nb)

##

##nb.add(f4, text='Tab4')

##

##

##from tkinter import *

##from tkinter import colorchooser

##

##def pick_color():

##    color = colorchooser.askcolor(title ="Choose color")

##    color_me.config(bg=color[1])

##    color_me.config(text=color)

##

##

##f4 = Tk()

##f4.title('PythonGuides')

##f4.geometry('400x300')

##

##color_me = Label(

##    f4,

##    text='(217, 217, 217) #d9d9d9',

##    font = ('Times', 20),

##    relief = SOLID,

##    padx=20,

##    pady=20

##)

##color_me.grid(row=5, column=4)

##button = Button(

##    f4,

##    text = "Choose Color",

##    command = pick_color,

##    padx=10,

##    pady=10,

##    font=('Times', 18),

##    bg='#4a7a8c'

##    )

##button.grid(row=2, column=2)

##

##f4.mainloop()

####

##

##Label(f4, text= 'label1').grid(column=0, row=2)

##

##ee1 = tk.StringVar()

##

##Entry(f4, textvariable=ee1, bg="yellow").grid(column=0, row=3)

##

##Label(f4, text= 'label1').grid(column=0, row=4)

##

##ee2 = tk.StringVar()

##

##Entry(f4, textvariable=ee2, bg="yellow").grid(column=0, row=5)

##

##

##

##

##

##ckb = IntVar()

##

##Checkbutton(f4, text='Accept the terms & conditions',

##

##            variable=ckb,onvalue=1, offvalue=0,command=termsCheck).grid(row=8, columnspan=4, pady=5)

##

##

##

##

##

##

##

##rb1 = tk.IntVar()

##

##rb1.set(1)

##

##

##

##radiobutton1 = tk.Radiobutton(f4, text="Radio 1", variable=rb1, value=1)

##

##radiobutton1.grid(column=4, row=1)

##

##

##

##radiobutton2 = tk.Radiobutton(f4, text="Radio 2", variable=rb1, value=2)

##

##radiobutton2.grid(column=5, row=1)

##

##

#############################################

##########Tab 5

#############################################

##

##f5 = ttk.Frame(nb, height=1000, width=1000)

##

##nb.add(f5, text='Tab5')

##

##

##

##

##nnb = ttk.Notebook(f5)

##nnb.grid(row=0, column=0)

##ff1 = ttk.Frame(nnb, height=1000, width=100)

##

##ff2 = ttk.Frame(nnb, height=1000, width=100)

##ff3= ttk.Frame(nnb, height=1000, width=100)

##ff4 = ttk.Frame(nnb, height=1000, width=1000)

##ff5 = ttk.Frame(nnb, height=1000, width=1000)

##ff6 = ttk.Frame(nnb, height=1000, width=1000)

##ff7 = ttk.Frame(nnb, height=1000, width=1000)

##ff8 = ttk.Frame(nnb, height=1000, width=1000)

##nnb.add(ff1, text='Tab1')

##nnb.add(ff2, text='Tab2')

##nnb.add(ff3, text='Tab3')

##nnb.add(ff4, text='Tab4')

##nnb.add(ff5, text='Tab5')

##nnb.add(ff6, text='Tab6')

##nnb.add(ff7, text='Tab7')

##nnb.add(ff8, text='Tab8')

##

####Label(ff1, text= 'label').grid(column=2, row=0)

##

##Label(ff2, text= 'label').grid(column=4, row=0)

##

##Label(ff3, text= 'label').grid(column=6, row=2)

##

##Label(ff1, text= 'label').grid(column=8, row=3)

##

##Label(ff2, text= 'label').grid(column=1, row=4)

##

##Label(ff3, text= 'label').grid(column=6, row=3)

##

##Label(ff1, text= 'label').grid(column=1, row=1)

##

##Label(ff4, text= 'label2').grid(column=1, row=4)

##

##Label(ff42, text= 'label3').grid(column=2, row=7)

##

##Label(ff4, text= 'label4').grid(column=4, row=7)

##

##Label(ff4, text= 'label5').grid(column=6, row=0)

##

##lbox1 = tk.Listbox(ff6).grid(column=2, row=1)

##

##lbox2 = tk.Listbox(ff7).grid(column=4, row=1)

##

##lbox3 = tk.Listbox(ff8).grid(column=6, row=1)

##

##

##

##Label(ff2, text= 'label').grid(column=3, row=5)

##

##ee1 = tk.StringVar()

##

####Entry(ff1, textvariable=ee1, bg="yellow").grid(column=0, row=3)

####

####Label(ff1, text= 'label').grid(column=0, row=4)

##

##eef2 = tk.StringVar()

##eeff2 = tk.StringVar()

##

####Entry(ff1, textvariable=eef2, bg="yellow").grid(column=0, row=5)

####

####Entry(ff1, textvariable=eeff2, bg="yellow").grid(column=0, row=5)

##

##btn1=tk.Button(ff1, text='button ', command=command).grid(column=2, row=1)

##

##btn2=tk.Button(ff2, text='button ', command=command).grid(column=2, row=2)

##

##

##

##ttt1 = tk.Text(ff3, bg='light green', height=20)

##

##ttt1.insert('1.0', tk.END)

##

##ttt1.grid(row=5, column=4, rowspan=5, columnspan=10)

##btn1=tk.Button(ff1, text='button 1', command=command).grid(column=2, row=1)

##

##btn2=tk.Button(ff1, text='button 2', command=command).grid(column=2, row=2)

##

##btn3=tk.Button(ff1, text='button 3', command=command).grid(column=2, row=3)

##

##btn4=tk.Button(ff1, text='button 4', command=command).grid(column=2, row=4)

##

##btn5=tk.Button(ff1, text='button 5', command=command).grid(column=2, row=5)

##

##btn6=tk.Button(ff1, text='button 6', command=command).grid(column=3, row=1)

##

##btn7=tk.Button(ff1, text='button 7', command=command).grid(column=3, row=2)

##

##btn8u=tk.Button(ff1, text='button 8', command=command).grid(column=3, row=3)

##

##btn9=tk.Button(ff1, text='button 9', command=command).grid(column=3, row=4)

##

##btn10=tk.Button(ff1, text='button 10', command=command).grid(column=3, row=5)


root.mainloop()
