import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pyautogui as pg
import pyperclip as pc
import sys

root = tk.Tk()
root.geometry("600x600")
root.title("JH APP Clipboard Pipe")
top = Toplevel(root)
fr1 = ttk.Frame(root)
fr1.grid(row=0, column=0, rowspan=10)
fr2 = ttk.Frame(root)
fr2.grid(row=4, column=1)
fr3 = ttk.Frame(root)
fr3.grid(row=3, column=2)
fr4 = ttk.Frame(root)
fr4.grid(row=3, column=3, rowspan=10)
fr5 = ttk.Frame(root)
fr5.grid(row=3, column=4)
fr6 = ttk.Frame(root)
fr6.grid(row=3, column=5, rowspan=10)


def get_filename(_type=""):
    "Returns the path and name of file selected"
    # _type=".txt" to get txt file name

    filename = filedialog.askopenfilename(
        initialdir=".",  # same dir of this script
        title="Select file",
        filetypes=(("", _type), ("all files", "*.*")),
    )
    return filename


###########################################################
def insert1():
    lb1.insert(1, cb1.get())


def insert2():
    lb1.insert(1, cb2.get())


def insert3():
    lb1.insert(1, cb1.get())


def insert3():
    lb1.insert(1, cb1.get())


def insert4():
    lb1.insert(1, cb1.get())


def insert5():
    lb1.insert(1, cb1.get())


def clear():
    lb1.delete(0, END)


def cl():
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    root.update()
    root.deiconify()
    return


def paste():
    # pg.hotkey('alt', 'tab')  # change window
    pg.hotkey("ctrl", "v")  # ctrl-v to paste
    return


def copy():
    pg.hotkey("ctrl", "c")  # ctrl-c to copy
    return


def manager():
    pass


text1 = "www.distrowatch.com"


def auto1():
    text1 = "www.distrowatch.com"
    pg.hotkey("alt", "F3", interval=1)  # change window
    pg.typewrite("firefox")
    pg.press("enter")
    pg.moveTo(522, 120)
    pg.click(x=522, y=120)
    pg.click(x=522, y=120)
    pg.press("enter")
    pg.press("backspace")
    pc.copy(text1)
    pg.hotkey("ctrl", "v")
    pg.press("enter")


##pg.click(x=100, y=200)
## pg.hotkey('F3')   # select  all
## pg.write("waterfox")
## #pg.hotkey('alt', 'tab')
## pg.hotkey('alt', 'tab')


def auto2():
    pg.hotkey("alt", "tab")
    pg.hotkey("ctrl", "alt", "t")
    pg.hotkey("ctrl", "alt", "t")
    pg.hotkey("ctrl", "alt", "t")
    pg.hotkey("shift", "ctrl", "v")


def auto3():
    pg.hotkey("alt", "tab")
    pg.hotkey("ctrl", "alt", "t")


################################################################

##menubar = tk.Menu(top)
##menubar.add_command(label="load web", command=auto1)
##menubar.add_command(label="File", command=get_filename)
##menubar.add_command(label="Call", command=None)
##menubar.add_command(label="Insert", command=None)
##menubar.add_command(label="Run", command=None)
##menubar.add_command(label="1", command=None)
##menubar.add_command(label="2", command=None)
##menubar.add_command(label="3", command=None)
##menubar.add_command(label="4", command=None)
##menubar.add_command(label="5", command=None)
###################################################################
btn1 = tk.Button(fr1, text="btn1", command=insert1)
btn1.grid(column=0, row=1)
btn2 = tk.Button(fr1, text="btn2", command=insert2)
btn2.grid(column=0, row=2)
btn3 = tk.Button(fr1, text="btn3", command=insert3)
btn3.grid(column=0, row=3)
btn4 = tk.Button(fr1, text="clear", command=clear)
btn4.grid(column=0, row=4)
btn5 = tk.Button(fr1, text="web broswer", command=auto1)
btn5.grid(column=0, row=5)
btn6 = tk.Button(fr1, text="button 6", command=None)
btn6.grid(column=0, row=6)
btn7 = tk.Button(fr1, text="button 7", command=None)
btn7.grid(column=0, row=7)
btn8 = tk.Button(fr1, text="button 8", command=None)
btn8.grid(column=0, row=8)
btn9 = tk.Button(fr1, text="button 9", command=None)
btn9.grid(column=0, row=9)
btn10 = tk.Button(fr1, text="button 10", command=None)
btn10.grid(column=0, row=10)
########################################################################
list1 = [
    "john.hewitt@cox.net",
    "Whobade55!",
    "john.hewitt1970@gmail.com",
    "ajolily@cox.net",
]
cb1 = ttk.Combobox(fr2, values=list1)
cb1.grid(row=3, column=1)
cb2 = ttk.Combobox(fr2, values=list1)
cb2.grid(row=4, column=1)
###########################################################################
lb1 = tk.Listbox(fr5)
lb1.grid(row=3, column=4)


##btn11=tk.Button(root, text='copy', command=copy)
##btn11.grid(column=1, row=1)
##btn12=tk.Button(root, text='auto1', command=auto1)
##btn12.grid(column=1, row=2)
##btn13=tk.Button(root, text='auto2', command=command)
##btn13.grid(column=1, row=3)
##btn14=tk.Button(root, text='button 4', command=command)
##btn14.grid(column=1, row=4)
##btn15=tk.Button(root, text='button 5', command=command)
##btn15.grid(column=1, row=5)
##btn16=tk.Button(root, text='button 6', command=command)
##btn16.grid(column=1, row=6)
##btn17=tk.Button(root, text='button 7', command=command)
##btn17.grid(column=1, row=7)
##btn18=tk.Button(root, text='button 8', command=command)
##btn18.grid(column=1, row=8)
##btn19=tk.Button(root, text='button 9', command=command)
##btn19.grid(column=1, row=9)
##btn20=tk.Button(root, text='button 10', command=command)
##btn20.grid(column=1, row=10)


##btn21=tk.Button(root, text='copy', command=copy)
##btn21.grid(column=2, row=1)
##btn22=tk.Button(root, text='auto1', command=auto1)
##btn22.grid(column=2, row=2)
##btn23=tk.Button(root, text='auto2', command=command)
##btn23.grid(column=2, row=3)
##btn24=tk.Button(root, text='button 4', command=command)
##btn24.grid(column=2, row=4)
##btn25=tk.Button(root, text='button 5', command=command)
##btn25.grid(column=2, row=5)
##btn26=tk.Button(root, text='button 6', command=command)
##btn26.grid(column=2, row=6)
##btn27=tk.Button(root, text='button 7', command=command)
##btn27.grid(column=2, row=7)
##btn28=tk.Button(root, text='button 8', command=command)
##btn28.grid(column=2, row=8)
##btn29=tk.Button(root, text='button 9', command=command)
##btn29.grid(column=2, row=9)
##btn30=tk.Button(root, text='button 10', command=command)
##btn30.grid(column=2, row=10)
##
##


pag_str = """
Mouse Control Functions
The Screen and Mouse Position

Locations on your screen are referred to by X and Y Cartesian coordinates. The X coordinate starts at 0 on the left side and increases going right. Unlike in mathematics, the Y coordinate starts at 0 on the top and increases going down.

0,0       X increases -->
+---------------------------+
|                           | Y increases
|                           |     |
|   1920 x 1080 screen      |     |
|                           |     V
|                           |
|                           |
+---------------------------+ 1919, 1079

The pixel at the top-left corner is at coordinates 0, 0. If your screen’s resolution is 1920 x 1080, the pixel in the lower right corner will be 1919, 1079 (since the coordinates begin at 0, not 1).

The screen resolution size is returned by the size() function as a tuple of two integers. The current X and Y coordinates of the mouse cursor are returned by the position() function.

For example:

>>> pyautogui.size()
(1920, 1080)
>>> pyautogui.position()
(187, 567)

Here is a short Python 3 program that will constantly print out the position of the mouse cursor:

#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

Here is the Python 2 version:

#! python
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print positionStr,
        print '\b' * (len(positionStr) + 2),
        sys.stdout.flush()
except KeyboardInterrupt:
    print '\n'

To check if XY coordinates are on the screen, pass them (either as two integer arguments or a single tuple/list arguments with two integers) to the onScreen() function, which will return True if they are within the screen’s boundaries and False if not. For example:

>>> pyautogui.onScreen(0, 0)
True
>>> pyautogui.onScreen(0, -1)
False
>>> pyautogui.onScreen(0, 99999999)
False
>>> pyautogui.size()
(1920, 1080)
>>> pyautogui.onScreen(1920, 1080)
False
>>> pyautogui.onScreen(1919, 1079)
True

Mouse Movement

The moveTo() function will move the mouse cursor to the X and Y integer coordinates you pass it. The None value can be passed for a coordinate to mean “the current mouse cursor position”. For example:

>>> pyautogui.moveTo(100, 200)   # moves mouse to X of 100, Y of 200.
>>> pyautogui.moveTo(None, 500)  # moves mouse to X of 100, Y of 500.
>>> pyautogui.moveTo(600, None)  # moves mouse to X of 600, Y of 500.

Normally the mouse cursor will instantly move to the new coordinates. If you want the mouse to gradually move to the new location, pass a third argument for the duration (in seconds) the movement should take. For example:

>>> pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds

(If the duration is less than pyautogui.MINIMUM_DURATION the movement will be instant. By default, pyautogui.MINIMUM_DURATION is 0.1.)

If you want to move the mouse cursor over a few pixels relative to its current position, use the move() function. This function has similar parameters as moveTo(). For example:

>>> pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
>>> pyautogui.move(0, 50)       # move the mouse down 50 pixels.
>>> pyautogui.move(-30, 0)      # move the mouse left 30 pixels.
>>> pyautogui.move(-30, None)   # move the mouse left 30 pixels.

Mouse Drags

PyAutoGUI’s dragTo() and drag() functions have similar parameters as the moveTo() and move() functions. In addition, they have a button keyword which can be set to 'left', 'middle', and 'right' for which mouse button to hold down while dragging. For example:

>>> pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
>>> pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
>>> pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button

Tween / Easing Functions

Tweening is an extra feature to make the mouse movements fancy. You can probably skip this section if you don’t care about this.

A tween or easing function dictates the progress of the mouse as it moves to its destination. Normally when moving the mouse over a duration of time, the mouse moves directly towards the destination in a straight line at a constant speed. This is known as a linear tween or linear easing function.

PyAutoGUI has other tweening functions available in the pyautogui module. The pyautogui.easeInQuad function can be passed for the 4th argument to moveTo(), move(), dragTo(), and drag() functions to have the mouse cursor start off moving slowly and then speeding up towards the destination. The total duration is still the same as the argument passed to the function. The pyautogui.easeOutQuad is the reverse: the mouse cursor starts moving fast but slows down as it approaches the destination. The pyautogui.easeOutElastic will overshoot the destination and “rubber band” back and forth until it settles at the destination.

For example:

>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end

These tweening functions are copied from Al Sweigart’s PyTweening module: https://pypi.python.org/pypi/PyTweening https://github.com/asweigart/pytweening This module does not have to be installed to use the tweening functions.

If you want to create your own tweening function, define a function that takes a single float argument between 0.0 (representing the start of the mouse travelling) and 1.0 (representing the end of the mouse travelling) and returns a float value between 0.0 and 1.0.
Mouse Clicks

The click() function simulates a single, left-button mouse click at the mouse’s current position. A “click” is defined as pushing the button down and then releasing it up. For example:

>>> pyautogui.click()  # click the mouse

To combine a moveTo() call before the click, pass integers for the x and y keyword argument:

>>> pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.

To specify a different mouse button to click, pass 'left', 'middle', or 'right' for the button keyword argument:

>>> pyautogui.click(button='right')  # right-click the mouse

To do multiple clicks, pass an integer to the clicks keyword argument. Optionally, you can pass a float or integer to the interval keyword argument to specify the amount of pause between the clicks in seconds. For example:

>>> pyautogui.click(clicks=2)  # double-click the left mouse button
>>> pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
>>> pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks

As a convenient shortcut, the doubleClick() function will perform a double click of the left mouse button. It also has the optional x, y, interval, and button keyword arguments. For example:

>>> pyautogui.doubleClick()  # perform a left-button double click

There is also a tripleClick() function with similar optional keyword arguments.

The rightClick() function has optional x and y keyword arguments.
The mouseDown() and mouseUp() Functions

Mouse clicks and drags are composed of both pressing the mouse button down and releasing it back up. If you want to perform these actions separately, call the mouseDown() and mouseUp() functions. They have the same x, y, and button. For example:

>>> pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
>>> pyautogui.mouseDown(button='right')  # press the right button down
>>> pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.

Mouse Scrolling

The mouse scroll wheel can be simulated by calling the scroll() function and passing an integer number of “clicks” to scroll. The amount of scrolling in a “click” varies between platforms. Optionally, integers can be passed for the the x and y keyword arguments to move the mouse cursor before performing the scroll. For example:

>>> pyautogui.scroll(10)   # scroll up 10 "clicks"
>>> pyautogui.scroll(-10)  # scroll down 10 "clicks"
>>> pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

On OS X and Linux platforms, PyAutoGUI can also perform horizontal scrolling by calling the hscroll() function. For example:

>>> pyautogui.hscroll(10)   # scroll right 10 "clicks"
>>> pyautogui.hscroll(-10)   # scroll left 10 "clicks"

The scroll() function is a wrapper for vscroll(), which performs vertical scrolling.
"""


pag_str2 = """
Mouse Clicks

The click() function simulates a single, left-button mouse click at the mouse’s current position. A “click” is defined as pushing the button down and then releasing it up. For example:

>>> pyautogui.click()  # click the mouse

To combine a moveTo() call before the click, pass integers for the x and y keyword argument:

>>> pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.

To specify a different mouse button to click, pass 'left', 'middle', or 'right' for the button keyword argument:

>>> pyautogui.click(button='right')  # right-click the mouse

To do multiple clicks, pass an integer to the clicks keyword argument. Optionally, you can pass a float or integer to the interval keyword argument to specify the amount of pause between the clicks in seconds. For example:

>>> pyautogui.click(clicks=2)  # double-click the left mouse button
>>> pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
>>> pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks

As a convenient shortcut, the doubleClick() function will perform a double click of the left mouse button. It also has the optional x, y, interval, and button keyword arguments. For example:

>>> pyautogui.doubleClick()  # perform a left-button double click

There is also a tripleClick() function with similar optional keyword arguments.

The rightClick() function has optional x and y keyword arguments.
The mouseDown() and mouseUp() Functions

Mouse clicks and drags are composed of both pressing the mouse button down and releasing it back up. If you want to perform these actions separately, call the mouseDown() and mouseUp() functions. They have the same x, y, and button. For example:

>>> pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
>>> pyautogui.mouseDown(button='right')  # press the right button down
>>> pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.

Mouse Scrolling

The mouse scroll wheel can be simulated by calling the scroll() function and passing an integer number of “clicks” to scroll. The amount of scrolling in a “click” varies between platforms. Optionally, integers can be passed for the the x and y keyword arguments to move the mouse cursor before performing the scroll. For example:

>>> pyautogui.scroll(10)   # scroll up 10 "clicks"
>>> pyautogui.scroll(-10)  # scroll down 10 "clicks"
>>> pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

On OS X and Linux platforms, PyAutoGUI can also perform horizontal scrolling by calling the hscroll() function. For example:

>>> pyautogui.hscroll(10)   # scroll right 10 "clicks"
>>> pyautogui.hscroll(-10)   # scroll left 10 "clicks"

The scroll() function is a wrapper for vscroll(), which performs vertical scrolling.
"""

pag_str3 = """
Keyboard Control Functions
The write() Function

The primary keyboard function is write(). This function will type the characters in the string that is passed. To add a delay interval in between pressing each character key, pass an int or float for the interval keyword argument.

For example:

>>> pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
>>> pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character

You can only press single-character keys with write(), so you can’t press the Shift or F1 keys, for example.
The press(), keyDown(), and keyUp() Functions

To press these keys, call the press() function and pass it a string from the pyautogui.KEYBOARD_KEYS such as enter, esc, f1. See KEYBOARD_KEYS.

For example:

>>> pyautogui.press('enter')  # press the Enter key
>>> pyautogui.press('f1')     # press the F1 key
>>> pyautogui.press('left')   # press the left arrow key

The press() function is really just a wrapper for the keyDown() and keyUp() functions, which simulate pressing a key down and then releasing it up. These functions can be called by themselves. For example, to press the left arrow key three times while holding down the Shift key, call the following:

>>> pyautogui.keyDown('shift')  # hold down the shift key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.keyUp('shift')    # release the shift key

To press multiple keys similar to what write() does, pass a list of strings to press(). For example:

>>> pyautogui.press(['left', 'left', 'left'])

Or you can set how many presses left:

>>> pyautogui.press('left', presses=3)

To add a delay interval in between each press, pass an int or float for the interval keyword argument.
The hold() Context Manager

To make holding a key convenient, the hold() function can be used as a context manager and passed a string from the pyautogui.KEYBOARD_KEYS such as shift, ctrl, alt, and this key will be held for the duration of the with context block. See KEYBOARD_KEYS.

>>> with pyautogui.hold('shift'):
        pyautogui.press(['left', 'left', 'left'])

…is equivalent to this code:

>>> pyautogui.keyDown('shift')  # hold down the shift key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.keyUp('shift')    # release the shift key

The hotkey() Function

To make pressing hotkeys or keyboard shortcuts convenient, the hotkey() can be passed several key strings which will be pressed down in order, and then released in reverse order. This code:

>>> pyautogui.hotkey('ctrl', 'shift', 'esc')

…is equivalent to this code:

>>> pyautogui.keyDown('ctrl')
>>> pyautogui.keyDown('shift')
>>> pyautogui.keyDown('esc')
>>> pyautogui.keyUp('esc')
>>> pyautogui.keyUp('shift')
>>> pyautogui.keyUp('ctrl')

To add a delay interval in between each press, pass an int or float for the interval keyword argument.
KEYBOARD_KEYS

The following are the valid strings to pass to the press(), keyDown(), keyUp(), and hotkey() functions:

['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

"""


if __name__ == "__main__":

    root.mainloop()
