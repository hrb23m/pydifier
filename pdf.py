import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

class Pdf:
  def __init__(self):
    self.pages = []

  def getPages(self):
    return self.pages

  def getPage(self, i):
    return self.pages[i]

  def setPages(self, pages):
    self.pages = pages

  def load(self, path):
    f = open(path, 'rb')
    reader = PdfFileReader(f)
    for i in range(reader.getNumPages()):
      pages[i] = reader.getPage(i)
    f.close()

  def save(self, path):
    f = open(path, 'wb')
    writer = PdfFileWriter(f)
    for i in range(pages):
      writer.addPage(pages[i])
    f.close()
