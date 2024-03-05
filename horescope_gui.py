from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
"""
   this check_sign function checks and returns the zodiac sign
   by day and month of your birth

"""
r = tk.Tk()

def check_sign():
    
    bday = tk.Entry(r, )
    your_birth_day = input("enter your birthday day number> ")
    your_birth_month = input("cool, and the month number, please> ")
    if (int(your_birth_month) == 12 and int(your_birth_day) >= 22) or (
        int(your_birth_month) == 1 and int(your_birth_day) <= 19
    ):
        sign = "Capricorn"
    elif (int(your_birth_month) == 1 and int(your_birth_day) >= 20) or (
        int(your_birth_month) == 2 and int(your_birth_day) <= 17
    ):
        sign = "Aquarium"
    elif (int(your_birth_month) == 2 and int(your_birth_day) >= 18) or (
        int(your_birth_month) == 3 and int(your_birth_day) <= 19
    ):
        sign = "Pices"
    elif (int(your_birth_month) == 3 and int(your_birth_day) >= 20) or (
        int(your_birth_month) == 4 and int(your_birth_day) <= 19
    ):
        sign = "Aries"
    elif (int(your_birth_month) == 4 and int(your_birth_day) >= 20) or (
        int(your_birth_month) == 5 and int(your_birth_day) <= 20
    ):
        sign = "Taurus"
    elif (int(your_birth_month) == 5 and int(your_birth_day) >= 21) or (
        int(your_birth_month) == 6 and int(your_birth_day) <= 20
    ):
        sign = "Gemini"
    elif (int(your_birth_month) == 6 and int(your_birth_day) >= 21) or (
        int(your_birth_month) == 7 and int(your_birth_day) <= 22
    ):
        sign = "Cancer"
    elif (int(your_birth_month) == 7 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 8 and int(your_birth_day) <= 22
    ):
        sign = "Leo"
    elif (int(your_birth_month) == 8 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 9 and int(your_birth_day) <= 22
    ):
        sign = "Virgo"
    elif (int(your_birth_month) == 9 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 10 and int(your_birth_day) <= 22
    ):
        sign = "Libra"
    elif (int(your_birth_month) == 10 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 11 and int(your_birth_day) <= 21
    ):
        sign = "Scorpio"
    elif (int(your_birth_month) == 11 and int(your_birth_day) >= 22) or (
        int(your_birth_month) == 12 and int(your_birth_day) <= 21
    ):
        sign = "Sagittarius"

    return sign


def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text


if __name__ == "__main__":
    print("Daily Horoscope. \n")
    text = tk.Text(r, bg='cyan')
    text.insert('1.0', tk.END)
    text.grid(row=0, column=1, rowspan=7, columnspan=5)
    e1 = tk.Entry(r)
    e1.grid(column=1, row=2)
    zodiac_sign = e1.get()
    
        
        
    if zodiac_sign != "calculate":
        values =["yesterday", "today", "tomorrow"]
        day = ttk.Combobox(r, values)
        horoscope_text = horoscope(zodiac_sign, day.get())
        print(horoscope_text)
    else:
        print("\nOk, don't worry. Soon you'll get it just pass this tiny quiz")
        print("\nCongratulations! you are defenetly", check_sign())
