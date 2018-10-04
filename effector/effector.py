from abc import ABCMeta

class Effector(metaclass=ABCMeta):
  def apply(self, pdf):
    return pdf

