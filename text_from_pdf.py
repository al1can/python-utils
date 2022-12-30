import PyPDF2
import glob

def get_text_from_pdf():
    texts = ''
    for file in glob.glob("data/*.pdf"):
        pdf_file = open('data/Get_Started_With_Smallpdf.pdf', 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        page_count = len(pdf_reader.pages)
        for i in range(page_count):
            page = pdf_reader.pages[i]
            text = page.extract_text()
            texts += text
        pdf_file.close()
    return texts
    