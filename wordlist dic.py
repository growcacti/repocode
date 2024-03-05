import tkinter as tk


def word_generator(file_path):
    with open(file_path, "r") as file:
        for word in file:
            yield word.strip()


def check_word():
    word = entry.get().strip()
    if word:
        if word in word_list_generator:
            result_label.config(text="Word found in the dictionary.")
        else:
            result_label.config(text="Word not found in the dictionary.")


# Create Tkinter window
window = tk.Tk()

# Create entry widget for word input
entry = tk.Entry(window)
entry.pack()

# Create button for word check
check_button = tk.Button(window, text="Check", command=check_word)
check_button.pack()

# Create label for displaying the result
result_label = tk.Label(window)
result_label.pack()

# Create word list generator
word_list_generator = word_generator("word_list.txt")

# Start the Tkinter event loop
window.mainloop()
