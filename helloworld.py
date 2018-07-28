#!python3
import docx
print("hello world!")
print("githup update!")
doc=docx.Document()
doc.add_paragraph('Hello World!')
doc.save('helloworld.docx')
