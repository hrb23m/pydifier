import copy

from effector import Effector

class HorizontalSplitter(Effector):
  def apply(self, pdf):
    numPages = len(pdf.getPages())

    pages = [0] * (numPages*2)
    for i in range(numPages):
      p1 = copy.copy(pdf.getPage(i))
      p2 = copy,copy(pdf.getPage(i))
      (w, h) = p.mediaBox.upperRight

      p1.mediaBox.upperLeft  = (0, h/2)
      p1.mediaBox.upperRight = (w, h/2)
      p1.mediaBox.lowerRight = (w, 0)
      p1.mediaBox.lowerLeft  = (0, 0)

      p2.mediaBox.upperLeft  = (0, h)
      p2.mediaBox.upperRight = (w, h)
      p2.mediaBox.lowerRight = (w, h/2)
      p2.mediaBox.lowerLeft  = (0, h/2)

      pages[i*2] = p1
      pages[i*2 + 1] = p2

    pdf.setPages(pages)

    return pdf
