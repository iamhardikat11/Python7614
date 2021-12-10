import pyttsx3,PyPDF2
pdfreader = PyPDF2.PdfFileReader(open('sample.pdf','rb'))
speak = pyttsx3.init()
for page_num in range(pdfreader.numPages):
  text = pdfreader.getPage(page_num).extractText() #Extraction of Text from Page page_num from the PDF File
  clean_text = text.strip().replace('\n',',') #REMOVAL of Unecessary Break_Lines(\n) and Spaces
  print(clean_text) #Print the Text from PDF to Cosole
  #speak.say(clean_text)
  speak.save_to_file(clean_text,'sample.mp3')
  speak.runAndWait()
speak.stop()  
  
  
  
