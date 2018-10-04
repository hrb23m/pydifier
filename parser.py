import argparse

parser = argparse.ArgumentParser(
  prog = "pydifier", 
  add_help = True)

### File option ###
# Input File
parser.add_argument('pdf_file_path', 
  action = 'store',
  type = str,
  metavar = "PDF_PATH",
  help = 'Pdf file path to be fixed.'
  )

# Output File
parser.add_argument('-o', '--output', 
  action = 'store',
  type = str,
  help = 'Output pdf file path .'
  )

# Output File suffix before extension
parser.add_argument('-s', '--suffix',
  action = 'store',
  default = 'fix',
  type = str,
  help = 'Output pdf file path suffix before .pdf extention.'
  )

### Split option ###
split_group = parser.add_mutually_exclusive_group(required=False)
# Vertical split
split_group.add_argument('-sv', '--vertical',
  action = 'store_true',
  default = False,
  help = 'Split pdf page vertically.')

# horizontal split
split_group.add_argument('-sh', '--horizontal',
  action = 'store_true',
  default = False,
  help = 'Split pdf page horizontally.')

### Rotate option ###
# rotate
parser.add_argument('-r', '--rotate',
  action = 'store',
  type = int,
  choices = [90, 180, 270],
  help = 'Rotate pdf page clockwise specified degree.'
  )

### Front page location ###
front_page = parser.add_mutually_exclusive_group(required=False)
# Front page is located 
front_page.add_argument('-ff', '--front-first',
  action = 'store_true',
  default = False,
  help = 'First page is located on first page when using saddle stitch option.'
  ) 

front_page.add_argument('-fs', '--front-second',
  action = 'store_true',
  default = True,
  help = 'First page is located on second page when using saddle stitch option.'
  ) 

### Binding option ###
parser.add_argument('-ss', '--saddle-stitch',
  action = 'store_true',
  default = False,
  help = 'Scanned PDF that is saddle stich binding.'
  )

### Order option ###
# Reverse output 3 
parser.add_argument('-rv', '--reverse',
  action = 'store_true',
  default = False,
  help = 'Output pdf pages reversely.')

### Others ###
# Verbose mode
parser.add_argument('--verbose',
  action = 'store_true',
  default = False,
  help = 'Run as verbose mode.'
  )

# Version
parser.add_argument('-v', '--version',
  action = 'version',
  version = '%(prog)s 0.1',
  help = 'Show version.'
  )
