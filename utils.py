import fitz  # PyMuPDF
import re

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def split_into_sections(text):
    sections = {}
    pattern = r"(?i)(abstract|introduction|related work|methodology|methods|results|discussion|conclusion|references)"
    matches = list(re.finditer(pattern, text))

    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section_name = match.group(0).strip().lower()
        sections[section_name] = text[start:end].strip()

    return sections