import fitz
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageDraw
import PyPDF2
from PyPDF2 import PdfFileMerger
import io


def extract_pdf_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page_text = reader.getPage(page_num).extractText()
            # Do some minimal reformatting here
            formatted_text = page_text.replace("\n", " ").replace(". ", ".\n")
            text += formatted_text
    return text


def extract_images_from_pdf(file_path):
    doc = fitz.open(file_path)
    images = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        img_list = page.get_images(full=True)
        for img_index, img in enumerate(img_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            pil_image = Image.open(io.BytesIO(image_bytes))
            images.append(pil_image)
    return images


def pdf_merge():
    """Merges all the pdf files in current directory"""
    merger = PdfFileMerger()
    allpdfs = [a for a in glob("*.pdf")]
    [merger.append(pdf) for pdf in allpdfs]
    with open("Merged_pdfs.pdf", "wb") as new_file:
        merger.write(new_file)


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    # Extract text
    extracted_text = extract_pdf_text(file_path)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, extracted_text)

    # Extract and display images
    images = extract_images_from_pdf(file_path)
    for image in canvas.winfo_children():
        image.destroy()
    for idx, img in enumerate(images):
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(canvas, image=photo)
        label.image = photo
        label.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PDF Extractor")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=1, fill="both", padx=10, pady=10)

    # Text extraction tab
    text_frame = ttk.Frame(notebook)
    notebook.add(text_frame, text="Text Extractor")

    read_frame = ttk.Notebook(root)
    notebook.add(read_frame, text="Read")
