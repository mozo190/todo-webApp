import os
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


if __name__ == "__main__":
    pdf_file = input("Enter the path to the PDF file: ").strip('"')
    audio_file = input("Enter the name of the audio file (e.g., output.mp3): ").strip()

    if not pdf_file.lower().endswith('.pdf'):
        print("Error: Please provide a PDF file.")
    elif not audio_file.lower().endswith('.mp3'):
        print("Error: Please provide an MP3 file as the output.")
    else:
        extract_text_from_pdf(pdf_file, audio_file)


