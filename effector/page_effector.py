from effector import Effector

class PageEffector(Effector):
  def apply(self, pdf):
    for page in pdf.getPages():
      self.applyPerPage(page)

  def applyPerPage(self, page):
    return page
