import os
import tkinter
from tkinter import filedialog, messagebox

from PyPDF2 import PdfReader
from gtts import gTTS


def extract_text_from_pdf(pdf_file, audio_file, lang='en', slow=False):
    try:
        if not os.path.exists(pdf_file):
            raise FileNotFoundError(f"The PDF file does not exist: {pdf_file}")

        reader = PdfReader(pdf_file)
        text = ''

        for page in reader.pages:
            text += page.extract_text() + '\n'

        if not text.strip():
            raise ValueError("No text found in the PDF file.")

        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(audio_file)

        messagebox.showinfo(f"Text extracted successfully from {pdf_file} and saved to {audio_file}")

    except FileNotFoundError as fnf_error:
        messagebox.showerror(f"Error: \n {fnf_error}")
    except ValueError as v_error:
        messagebox.showerror(f"Error: {v_error}")
    except Exception as e:
        messagebox.showerror(f"Unknown error occurred: {e}")


def select_pdf():
    pdf_file = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    pdf_path_var.set(pdf_file)


def select_output():
    audio_file = filedialog.asksaveasfilename(
        title="Choose the output audio file",
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")]
    )
    audio_path_var.set(audio_file)


def convert_to_audio():
    pdf_file = pdf_path_var.get().strip()
    audio_file = audio_path_var.get().strip()

    if not pdf_file.lower().endswith('.pdf'):
        messagebox.showerror("Error: Please provide a PDF file.")
        return

    if not audio_file.lower().endswith('.mp3'):
        messagebox.showerror("Error: Please provide an MP3 file as the output.")
        return

    extract_text_from_pdf(pdf_file, audio_file)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("PDF to Audio Converter")

    pdf_path_var = tkinter.StringVar()
    audio_path_var = tkinter.StringVar()

    tkinter.Label(root, text="PDF File:").grid(row=0, column=0, padx=10, sticky='w')
    tkinter.Entry(root, textvariable=pdf_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
    tkinter.Button(root, text="Select PDF", command=select_pdf).grid(row=0, column=2, padx=10, pady=10)

    tkinter.Label(root, text="Audio File:").grid(row=1, column=0, padx=10, sticky='w')
    tkinter.Entry(root, textvariable=audio_path_var, width=50).grid(row=1, column=1, padx=10, pady=10)
    tkinter.Button(root, text="Select Output", command=select_output).grid(row=1, column=2, padx=10, pady=10)

    tkinter.Button(root,
                   text="Convert to Audio",
                   command=convert_to_audio,
                   bg='green',
                   fg='white').grid(row=2, column=0, columnspan=3, pady=20)

    root.mainloop()
