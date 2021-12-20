import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


# JH APPS
# redevelopment Project from console to GUI APP



root = tk.Tk()
root.geometry("800x800")




nb = ttk.Notebook(root)
nb.grid(row=0, column=0)

r = ttk.Frame(nb)
r.grid(row=1, column=1)
nb.add(r, text="list")


btn = ttk.Frame(nb)
btn.grid(row=1, column=1)
nb.add(btn, text="Select")

top = ttk.Frame(nb)
top.grid(row=1, column=1)
nb.add(top, text="view")

#to specify size of window. 
 
##def next():
##   
##
##    txt.insert(tk.END, horoscope_text)
### To Create a text widget and specify size. 
##
### TO Create label 
##l = tk.Label(r, text = "Daily Horoscope")
##l.grid(row=1, column=4)
##l.config(font =("Courier", 14))
txt = tk.Text(top, height=40, width=20 , font=("Chancery Uralic", 16))
txt.grid(row=1, column=1)

def main():
 
    
      
    # Create a button for the next text. 


    def horoscope(zodiac_sign: int, day: str) -> str:
        
       
        url = (
            "https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
        )
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        
        return soup.find("div", class_="main-horoscope").p.text
    
    txt.insert(tk.END, horoscope(sp.get(), cb2.get()))


    b1 = tk.Button(btn, text = "Next", command=lambda: horoscope(sp.get(), cb2.get()))
    b1.grid(row=3, column=1)
    
    
sel_str="""
    Daily Horoscope. \n

    enter your Zodiac sign number:\n
    1. Aries\n
    2. Taurus\n
    3. Gemini\n
    4. Cancer\n
    5. Leo\n
    6. Virgo\n
    7. Libra\n
    8. Scorpio\n
    9. Sagittarius\n
    10. Capricorn\n
    11. Aquarius\n
    12. Pisces\n
"""







label=tk.Label(r, text=sel_str, bg="white").grid(row=0, column=0)


day = ["yesterday", "today", "tomorrow"]
cb2 = ttk.Combobox(btn, values=day)
cb2.grid(row=1, column=1)
sp = tk.Spinbox(btn, from_=1, to=12, increment=1)
sp.grid(row=0,column=1)


#print("choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
#ay = input("enter the day> ")
##sel_day = tk.StringVar()
##days = ["yesterday", "today", "tomorrow"]
##cb2 = ttk.Combobox(root, textvariable=sel_day)
##cb2.grid(row=3, column=1)
##cb2['values'] = days
##cb2['state'] = 'readonly'

#oroscope_text = horoscope(sp.get(), cb2.get())
#print(horoscope_text)

bt1 = tk.Button(btn, text = "Next", command=main)
bt1.grid(row=5, column=1)


if __name__=='__main__':
    
    r.mainloop
