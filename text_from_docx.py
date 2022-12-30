import docx
import glob

def get_text_from_docx():
    texts = ''
    for file in glob.glob("data/*.docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            escapes = ''.join([chr(char) for char in range(1, 32)])
            text = para.text.translate(str.maketrans('', '', escapes))
            texts += text+'. '
    return texts
    