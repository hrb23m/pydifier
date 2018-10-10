import os

class Config:
  FRONT_FIRST  = 1
  FRONT_SECOND = 2

  def __init__(self):
    self.input_file_path   = None
    self.output_file_path  = None
    self.suffix            = "fix"
    self.vertical_split    = False
    self.horizontal_split  = False
    self.rotate_degree     = 0
    self.frontPageLocation = Config.FRONT_SECOND
    self.saddle_stitch     = False
    self.reverse           = False
    self.verbose           = False

  def setInputFilePath(self, path):
    self.input_file_path = path

  def getInputFilePath(self):
    return self.input_file_path

  def setOutputFilePath(self, path):
    self.output_file_path = path

  def getOutputFilePath(self):
    if self.output_file_path is None:
      input_file_dirpath  = os.path.dirname(self.input_file_path)
      input_file_basename = os.path.basename(self.input_file_path)
      input_file_name, input_file_extention = os.path.splitext(input_file_basename)

      output_file_basename = input_file_name + "_" + self.getSuffix() + input_file_extention

      self.output_file_path = os.path.join(input_file_dirpath, output_file_basename)

    return self.output_file_path

  def setSuffix(self, suffix):
    self.suffix = suffix

  def getSuffix(self):
    return self.suffix

  def setVerticalSplit(self):
    self.vertical_split = True

  def resetVerticalSplit(self):
    self.vertical_split = False

  def isVerticalSplit(self):
    return self.vertical_split

  def setHorizontalSplit(self):
    self.hotizontal_split = True

  def resetHorizontalSplit(self):
    self.horizontal_split = False

  def isHorizontalSplit(self):
    return self.horizontal_split
  
  def setRotateDegree(self, degree):
    self.rotate_degree = degree

  def getRotateDegree(self):
    return self.rotate_degree

  def setFrontPageLocation(self, location):
    self.frontPageLocation = location

  def getFrontPageLocation(self):
    return self.frontPageLocation

  def setSaddleStitch(self):
    self.saddle_stitch = True

  def resetSaddleStitch(self):
    self.saddle_stitch = False

  def isSaddleStitch(self):
    return self.saddle_stitch

  def setReverse(self):
    self.reverse = True

  def resetReverse(self):
    self.reverse = False

  def doReverse(self):
    return self.reverse

  def setVerbose(self):
    self.verbose = True

  def resetVerbose(self):
    self.verbose = False

  def verbose(self):
    return self.verbose
