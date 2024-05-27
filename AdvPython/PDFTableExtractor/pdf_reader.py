import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize
# Download necessary resources for NLTK
nltk.download('punkt')

pdf_path = '/workspaces/PythonPractice/AdvPython/PDFTableExtractor/OOPS-Python.pdf'
document = fitz.open(pdf_path)

# Open the text file in append mode so each new run doesn't erase the previous content
with open('/workspaces/PythonPractice/AdvPython/PDFTableExtractor/PDFinTXT.txt','a') as tf:
    # Iterate through each page of the PDF
    for page_num in range(len(document)):
        # Load the page
        page = document.load_page(page_num)
        # Extract text from the page
        page_text = page.get_text()
        # Tokenize the text into sentences
        sentences = sent_tokenize(page_text)

        # Write each sentence to the file, one per line
        for sentence in sentences:
            tf.write(sentence + '\n')

document.close()