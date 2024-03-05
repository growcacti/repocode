import tkinter as tk
import re
from tkinter import ttk, Toplevel, Listbox, Scrollbar, END
from string import punctuation
from collections import Counter


class Wordcount(object):
    def __init__(self, text):
        self.rt = tk.Tk()

        self.lb = tk.Listbox(self.rt, height=20, selectmode=tk.EXTENDED)
        self.sc = ttk.Scrollbar(self.rt, orient=tk.VERTICAL, command=self.lb.yview)
        self.lb["yscrollcommand"] = self.sc.set
        self.sc.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        self.lb.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.text = text
        self.text2 = "".join(c for c in self.text.lower() if c not in punctuation)
        self.mostcommon_count = Counter(self.text2.split()).most_common()
        self.mc_cnt = self.mostcommon_count
        self.search_loop()
        self.word = ""
        self.freq = 0

    def search_loop(self):
        for self.word, self.freq in self.mc_cnt:
            print("{:3d}  {}".format(self.freq, self.word))
            self.lb.insert(END, "{:3d}  {}".format(self.freq, self.word))

        self.mc_cnt_w = sorted(self.mc_cnt)
        self.mc_cnt_fw = sorted(self.mc_cnt_w, key=lambda tup: tup[1], reverse=True)

        self.wordcount = len(re.findall("\w+", self.text))
        total = f"total words= {self.wordcount}"
        self.lb.insert(END, total)


def main():
    text = """You do not need to be following along our Tkinter series to participate in this tutorial. If you are here purely to learn Object Oriented Programming, that is fine.

    With our program in mind, it has become time that we consider Object Oriented Programming (OOP) to achieve our back-end goals. Up until this point,
    my tutorials have excluded object oriented programming for the most part. It's just not generally my style,
    and often times complicates the learning of the specific topic by adding another layer of complexity in the form of obfuscation to the task.

    For those of you who are unfamiliar with, or confused by, what object oriented programming actually is, you are not alone. Even people who use
    it do not usually fully understand the inner workings sometimes. I do not consider myself an OOP expert, especially since I rarely use it,
    but I know enough to know it will help us out here in the long run with our Tkinter application and I can share what I do know for you fine folks!

    So, Object Oriented Programming is a programming paradigm, or better put: a structure. That's it. It's just a structure with which we build a program.
    Python is often treated purely as a scripting language, but it is fundamentally an OOP language, actually.


    With OOP, you basically state the structure of your program, and your classes quite literally return "objects," which is why it is called "object" oriented.
    The objects serve as "instances" of your classes. That's about all I want to say on the matter before we just jump into an example. I think a practical example goes a long way in helping to learn, so let's get into it!

    I will share the code in chunks, explaining each step of the way. If you get lost, I will post the "full" version of this series' code at the very bottom, so fear not!"
    """

    wc = Wordcount(text)


if __name__ == "__main__":
    main()
