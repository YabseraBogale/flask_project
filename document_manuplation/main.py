import docx 

doc=docx.Document("question.docx")


for i in doc.paragraphs:
    print(i.text)