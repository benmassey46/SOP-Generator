import openai
import config
from PyPDF2 import PdfReader
from pathlib import Path
 
# --- Initialize API Clients ---
# --- OpenAI Client ---
openai_client = None
if config.OPENAI_API_KEY:
    try:
        openai_client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        print("OpenAI client initialized successfully.")
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}. OpenAI functions unavailable.")
        config.OPENAI_API_KEY = None # Mark as unavailable
else:
    print("Warning: OPENAI_API_KEY environment variable not found. OpenAI functions unavailable.")


# -- Expert file API ---
def pdf_to_text_pypdf2(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    except FileNotFoundError:
        return f"Error: File not found at {pdf_path}"
    except Exception as e:
        return f"Error processing PDF: {e}"
    return text.strip()

expert_file = None
try:
    expert_filename = config.EXPERT_FILE_PATH
    file_path = Path(expert_filename)
    print(f"file_path: {file_path.suffix}")
    if(file_path.suffix==".pdf"):
        expert_text = pdf_to_text_pypdf2(expert_filename)
    elif (file_path.suffix==".txt"):
        f = open(expert_filename)
        expert_text = f.read()
    else:
        print("WARNING: file suffix unsupported")
except Exception as e:
    print(f"Error {e} opening user file {expert_filename}")
