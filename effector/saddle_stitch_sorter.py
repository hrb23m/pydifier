from effector import Effector
from config import Config

class SaddleStitchSorter(Effector):

  def setFrontPageLocation(self, location):
    self.front_page_location = location

  def apply(self, pdf):
    pages = pdf.getPages()
    num_pages = len(pages)

    sorted_pages = [0] * num_pages

    if self.front_page_location == Config.FRONT_SECOND:
      for i in range(num_pages//4):
        sorted_pages[num_pages//2 - 1 - i*2] = pages[i*4]
        sorted_pages[num_pages//2     + i*2] = pages[i*4 + 1]
        sorted_pages[num_pages//2 + 1 + i*2] = pages[i*4 + 2]
        sorted_pages[num_pages//2 - 2 - i*2] = pages[i*4 + 3]
    else:
      for i in range(num_pages//4):
        sorted_pages[num_pages//2 - 1 - i*2] = pages[i*4 + 3]
        sorted_pages[num_pages//2     + i*2] = pages[i*4 + 2]
        sorted_pages[num_pages//2 + 1 + i*2] = pages[i*4 + 1]
        sorted_pages[num_pages//2 - 2 - i*2] = pages[i*4]

    pdf.setPages(sorted_pages)

    return pdf
