import sys
import traceback
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class CustomErrorDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("Error Display")

        self.text_widget = ScrolledText(root, wrap=tk.WORD, height=20, width=80)
        self.text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Redirect stderr to this class
        sys.stderr = self

    def write(self, message):
        """Write message to the text widget."""
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        """Required for file-like objects, no operation needed."""
        pass

    def display_exception(self, exc_type, exc_value, tb):
        """Format and display the exception."""
        formatted_traceback = ''.join(traceback.format_exception(exc_type, exc_value, tb))
        self.write(formatted_traceback)


# Main application
def main():
    root = tk.Tk()
    app = CustomErrorDisplay(root)

    # Set custom exception hook
    def custom_exception_handler(exc_type, exc_value, tb):
        app.display_exception(exc_type, exc_value, tb)

    sys.excepthook = custom_exception_handler

    # Example button to trigger an error
    def cause_error():
        raise ValueError("This is a test error!")

    tk.Button(root, text="Cause Error", command=cause_error).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
