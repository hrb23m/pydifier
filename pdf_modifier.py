from effector import *

from pdf import Pdf

class PdfModifier:
  def __init__(self, config):
    self.config = config

    self.__buildEffectorChain()

  
  def execute(self):
    pdf = Pdf()

    try:
      pdf.load(self.config.getInputFilePath())
      for effector in self.effectorChain:
        pdf = effector.apply(pdf)

      pdf.save(self.config.getOutputFilePath())
    finally:
      pdf.close()


  def __buildEffectorChain(self):
    self.effectorChain = []

    # splitter
    if self.config.isVerticalSplit():
      self.effectorChain.append(VerticalSplitter())

    if self.config.isHorizontalSplit():
      self.effectorChain.append(HorizontalSplitter())

    # rotate
    if 0 < self.config.getRotateDegree():
      self.effectorChain.append(Rotater(self.config.getRotateDegree()))

    # saddle stitch
    if self.config.isSaddleStitch():
      effector = SaddleStitchSorter()
      effector.setFrontPageLocation(self.config.getFrontPageLocation())
      self.effectorChain.append(effector)

    # reverse
    if self.config.doReverse():
      self.effectorChain.append(Reverser())
