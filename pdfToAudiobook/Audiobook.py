#Import Libraries
#Import Google Text to Speech library

from gtts import gTTS

#Import PDF reader PyPDF2
from PyPDF2 import PdfReader

#Open file Path
pdf_File = open('pdftoAudiobook/test.pdf', 'rb')

#Create PDF Reader Object
pdf_Reader = PdfReader(pdf_File)
count = len(pdf_Reader.pages) # <- Counts the number of pages in the pdf
textList = []

#Extracts text data from each page of the pdf file
for page in pdf_Reader.pages:
    try:
        text = page.extract_text()
        textList.append(text)
    except:
        pass

print(textList)  # Add this line to debug

# Converts multiline text to a single line text
textString = " ".join(textList)

print(textString)  # Add this line to debug

# Select language (english = en / spanish = es etc)
language = 'en'

# Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")