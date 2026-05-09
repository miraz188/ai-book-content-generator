from pypdf import PdfReader

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        for p in reader.pages:
            text += p.extract_text() or ""
        return text
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
