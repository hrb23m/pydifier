import sys, copy
from PyPDF2 import PdfFileWriter, PdfFileReader

class Pdf:
  def __init__(self):
    self.input_stream = None
    self.output_stream = None
    self.pages = []

  def getPages(self):
    return self.pages

  def setPages(self, pages):
    self.pages = pages

  def getPage(self, i):
    return self.pages[i]

  def setPage(self, i, page):
    self.pages[i] = page

  def load(self, path):
    self.input_stream = open(path, 'rb')
    reader = PdfFileReader(self.input_stream)
    for i in range(reader.getNumPages()):
      page = copy.copy(reader.getPage(i))
      self.pages.append(page)

  def save(self, path):
    writer = PdfFileWriter()
    for page in self.pages:
      writer.addPage(page)

    self.output_stream = open(path, 'wb')
    writer.write(self.output_stream)

  def close(self):
    if (self.input_stream != None):
      self.input_stream.close()
    if (self.output_stream != None):
      self.output_stream.close()
