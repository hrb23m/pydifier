from effector import Effector

class Reverser(Effector):
  def apply(self, pdf):
    pages = pdf.getPages()
    pages.reverse()
    pdf.setPages(pages)

    return pdf
