import os
import tkinter
from tkinter import filedialog

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

        print(f"Text extracted from {pdf_file} and saved to {audio_file}")
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as v_error:
        print(f"Error: {v_error}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")


def select_pdf():
    pdf_file = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    pdf_path_var.set(pdf_file)


def convert_to_audio():
    pdf_file = input("Enter the path to the PDF file: ").strip('"')
    audio_file = input("Enter the name of the audio file (e.g., output.mp3): ").strip()
    if not pdf_file.lower().endswith('.pdf'):
        print("Error: Please provide a PDF file.")
    elif not audio_file.lower().endswith('.mp3'):
        print("Error: Please provide an MP3 file as the output.")
    else:
        extract_text_from_pdf(pdf_file, audio_file)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("PDF to Audio Converter")

    pdf_path_var = tkinter.StringVar()
    audio_path_var = tkinter.StringVar()

    tkinter.Label(root, text="PDF File:").grid(row=0, column=0, padx=10, sticky='w')
    tkinter.Entry(root, textvariable=audio_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
    tkinter.Button(root, text="Select PDF", command=select_pdf).grid(row=0, column=2, padx=10, pady=10)

    tkinter.Label(root, text="Audio File:").grid(row=1, column=0, padx=10, sticky='w')
    tkinter.Entry(root, textvariable=select_output, width=50).grid(row=1, column=1, padx=10, pady=10)
    tkinter.Button(root, text="Select Output", command=select_output).grid(row=1, column=2, padx=10, pady=10)

    root.mainloop()