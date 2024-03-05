from tkinter import *

from random import *


window = Tk()

window.title("Resistor Divider with Load Resistor")


def create_grid(window):

    width = 1800

    height = 1000

    canvas = Canvas(window, background="white", width=width, height=height)

    for line in range(0, width, 10):  # range(start, stop, step)

        canvas.create_line(
            [(line, 0), (line, height)], fill="black", tags="grid_line_w"
        )

    for line in range(0, height, 10):

        canvas.create_line([(0, line), (width, line)], fill="black", tags="grid_line_h")

    canvas.grid(row=0, column=0)

    line = canvas.create_line(180, 70, 180, 90, fill="black", width=7)

    line2 = canvas.create_line(180, 90, 180, 120, fill="black", width=7)

    line3 = canvas.create_line(180, 120, 220, 140, fill="black", width=7)

    line4 = canvas.create_line(220, 140, 180, 160, fill="black", width=7)

    line5 = canvas.create_line(180, 160, 220, 180, fill="black", width=7)

    line6 = canvas.create_line(220, 180, 180, 200, fill="black", width=7)

    line7 = canvas.create_line(180, 200, 220, 220, fill="black", width=7)

    line8 = canvas.create_line(220, 220, 180, 240, fill="black", width=7)

    line9 = canvas.create_line(180, 350, 430, 350, fill="black", width=7)

    ine1 = canvas.create_line(220, 370, 220, 370, fill="black", width=7)

    ine2 = canvas.create_line(180, 370, 180, 400, fill="black", width=7)

    ine3 = canvas.create_line(180, 400, 220, 420, fill="black", width=7)

    ine4 = canvas.create_line(220, 420, 180, 440, fill="black", width=7)

    ine5 = canvas.create_line(180, 440, 220, 460, fill="black", width=7)

    ine6 = canvas.create_line(220, 460, 180, 480, fill="black", width=7)

    ine7 = canvas.create_line(180, 480, 220, 500, fill="black", width=7)

    ine8 = canvas.create_line(220, 500, 180, 520, fill="black", width=7)

    ine9 = canvas.create_line(180, 520, 180, 600, fill="black", width=7)

    line11 = canvas.create_line(100, 600, 260, 600, fill="black", width=7)

    line12 = canvas.create_line(150, 620, 210, 620, fill="black", width=7)

    line13 = canvas.create_line(170, 640, 190, 640, fill="black", width=7)

    line14 = canvas.create_line(220, 140, 180, 160, fill="black", width=7)

    line15 = canvas.create_line(180, 160, 220, 180, fill="black", width=7)

    line16 = canvas.create_line(220, 180, 180, 200, fill="black", width=7)

    line17 = canvas.create_line(180, 200, 220, 220, fill="black", width=7)

    line18 = canvas.create_line(220, 220, 180, 240, fill="black", width=7)

    line19 = canvas.create_line(180, 240, 180, 370, fill="black", width=7)

    ne1 = canvas.create_line(430, 350, 430, 370, fill="black", width=7)

    ne2 = canvas.create_line(430, 370, 430, 400, fill="black", width=7)

    ne3 = canvas.create_line(430, 400, 470, 420, fill="black", width=7)

    ne4 = canvas.create_line(470, 420, 430, 440, fill="black", width=7)

    ine5 = canvas.create_line(430, 440, 470, 460, fill="black", width=7)

    ine6 = canvas.create_line(470, 460, 430, 480, fill="black", width=7)

    ine7 = canvas.create_line(430, 480, 470, 500, fill="black", width=7)

    ine8 = canvas.create_line(470, 500, 430, 520, fill="black", width=7)

    ine9 = canvas.create_line(430, 520, 430, 600, fill="black", width=7)

    gnd21 = canvas.create_line(350, 600, 520, 600, fill="black", width=7)

    gnd22 = canvas.create_line(400, 620, 460, 620, fill="black", width=7)

    gnd23 = canvas.create_line(420, 640, 440, 640, fill="black", width=7)


##

##

##

##

##

##

##

##

##

####

####

####    line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)

####

####    line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)

####

##    line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)

##

##    line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)

##

##

##    line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)

##

##    line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)

##    line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)

##

##    line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)

##

##    line444 =canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill ='black', width = 7)

##

##    line434 =canvas.create_line(655, 585, 755, 585, 605, 680, 655, 585, fill ='black', width = 7)

##

##    line4e4 =canvas.create_line(355, 485, 455, 585, 505, 480, 455, 485, fill ='black', width = 7)

##

##

##    line344 =canvas.create_line(755, 785, 655, 785, 605, 680, 755, 785, fill ='black', width = 7)

##

##


create_grid(window)

window.mainloop()
