import collections
import collections.abc
import textract
import os


def get_text_from_textract():
    directory = "data"
    available_filetypes = ['.csv', '.doc', '.docx', '.epub', '.jpg', '.html', '.pdf', '.png', '.pptx', '.txt', '.xlsx', '.xls']
    texts = ''
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            if os.path.splitext(file)[1] in available_filetypes:
                text = str(textract.process(filepath))
                escapes = ''.join([chr(char) for char in range(1, 32)])
                text = text.translate(str.maketrans('', '', escapes))
                texts += text+'. '
    return texts

print(get_text_from_textract())