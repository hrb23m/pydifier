from .page_effector import PageEffector

class Rotater(PageEffector):
  def __init__(self, degree):
    self.degree = degree
  
  def applyPerPage(self, page):
    page.rotateClockwise(self.degree)
    return page
