import sys
import traceback

from parser import parser
from config import Config
from pdf_modifier import PdfModifier

def build_config(args):
  config = Config()

  config.setInputFilePath(args.pdf_file_path)
  config.setOutputFilePath(args.output)
  config.setSuffix(args.suffix)

  if args.vertical:
    config.setVerticalSplit()
  if args.horizontal:
    config.setHorizontalSplit()

  if args.rotate:
    config.setRotateDegree(args.rotate)

  if args.saddle_stitch:
    config.setSaddleStitch()
    if args.front_first:
      config.setFrontPageLocation(Config.FRONT_FIRST)
    if args.front_second:
      config.setFrontPageLocation(Config.FRONT_SECOND)

  if args.reverse:
    config.setReverse()
  if args.verbose:
    config.setVerbose()

  return config

def main():
  args = parser.parse_args()

  try:
    config = build_config(args)
    pdf_modifier = PdfModifier(config)
    pdf_modifier.execute()

    sys.exit(0)
  except Exception as e:
    if args.verbose:
      print("{:=^30}".format(" Stack Trace"))
      traceback.print_exc()
    else:
      t, v, tb = sys.exc_info()
      print("%s\n", v)
      sys.exit(1)

if __name__ == "__main__":
  main()
