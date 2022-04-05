import pyttsx3
import PyPDF2
book= open('DATA SCIENCE WITH PYTHON.pdf','rb')
ReadingBook =PyPDF2.PdfFileReader(book)
pages =ReadingBook.numPages

print(pages)
speaker =pyttsx3.init()

page = ReadingBook.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()