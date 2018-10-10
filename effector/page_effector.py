from effector import Effector

class PageEffector(Effector):
  def apply(self, pdf):
    pages = pdf.getPages()
    for i in range(len(pages)):
      applied_page = self.applyPerPage(pages[i])
      pdf.setPage(i, applied_page)

    return pdf

  def applyPerPage(self, page):
    return page
