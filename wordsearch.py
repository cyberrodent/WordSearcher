#given the number of columns and rows for array of random letters, see if any of the provided words are in the grid.
import random
import re
import string

class ScanOpts:
    tag = "DefaultTag"
    outer_loop = []
    inner_loop = []
    flip_xy = False
    desc = False
    while_block = False
    def __init__(self, outer, inner):
        self.outer_loop = outer
        self.inner_loop = inner
    def test(self, needle, haystack):
        if re.search(needle, haystack):
            return True
        return False

class Grid:
  """
  Repesents a x,y grid of characters.
  Provides methods to get and print the grid
  as well as generate it.
  """
  def __init__(self, numRows, numCols):
    self.letterbag = string.ascii_lowercase
    self.grid = []
    self.numRows = numRows
    self.numCols = numCols
    self.__makeRandomLetterGrid()

  def __makeRandomLetterGrid(self):
    """Generates the x,y array we call grid"""
    for x in range(self.numRows):
      row = []
      for y in range(self.numCols):
        row.append(self.__getRandChar())
      self.grid.append(row)
    return self.grid

  def __getRandChar(self):
    """Pict a random one from the letterbag"""
    return self.letterbag[random.randint(0,25)]

  def get(self):
    """simple getter"""
    return self.grid

  def draw(self):
    """Print the grid to stdout"""
    for x in range(self.numRows):
      print self.grid[x]

  def upsidedown(self):
    for l in range(self.numRows):
      upsideDownGrid = []
      for l in range(self.numCols-1,-1,-1):
        upsideDownGrid.append(self.grid[l])
    return upsideDownGrid

present = 0

numbers = raw_input("How many rows and how many columns do you want the grid to have? (Enter as: rows,columns) ")
parsed = [int(x.strip()) for x in numbers.split(',')]
numRows = parsed[0]
numColumns = parsed[1]


#making the grid
gameGrid = Grid(numRows, numColumns)
grid = gameGrid.get()
grid_upsidedown = gameGrid.upsidedown()
gameGrid.draw()


wordString = raw_input("What words would you like to search for? Please enter them separated by a comma. (i.e. cat,dog,fish)" )
words = wordString.split(',')
sep=''



"""
#checking rows left to right
for r in range(numRows):
  rowString = sep.join(grid[r])
  for w in range(len(words)):
    if re.search(words[w], rowString):
      print "The word", words[w], "appears in the grid"
      present = 1
      
#checking rows right to left
for r in range(numRows):
  reverseRow = []
  for l in range(numColumns-1,-1,-1):
   reverseRow.append(grid[r][l])
  rowString = sep.join(reverseRow)
  for w in range(len(words)):
    if re.search(words[w], rowString):
      print "The word", words[w], "appears in the grid"
      present = 1
      
# checking columns top to bottom
for c in range(numColumns):
  columnVector = []
  for r in range(numRows):
    columnVector.append(grid[r][c])
  columnString = sep.join(columnVector)
  for w in range(len(words)):
    if re.search(words[w], columnString):
      print "The word", words[w], "appears in the grid"
      present = 1

#checking columns upside-down
for r in range(numRows):
  upsideDownGrid = []
  for l in range(numColumns-1,-1,-1):
   upsideDownGrid.append(grid[l])
    
for c in range(numColumns):
  columnVector = []
  for r in range(numRows):
    columnVector.append(upsideDownGrid[r][c])
  columnString = sep.join(columnVector)
  for w in range(len(words)):
    if re.search(words[w], columnString):
      print "The word", words[w], "appears in the grid"
      present = 1


 
#### diagonal, right-side-up ####
#first, diagonals from the top
for c in range(numColumns-1):
  r = 0
  diagVector = []
  while c <= numColumns-1:
    diagVector.append(grid[r][c])
    r=r+1
    c=c+1
  diagString = sep.join(diagVector)
  for w in range(len(words)):
    if re.search(words[w], diagString):
      print "The word", words[w], "appears in the grid"
      present = 1
      
#diagonals from the lefthand side, and I don't need to repeat the one starting at 0,0
for r in range(1,numRows-1):
  c = 0
  diagVector = []
  while r <= numRows-1:
    diagVector.append(grid[r][c])
    r=r+1
    c=c+1
  diagString = sep.join(diagVector)
  for w in range(len(words)):
    if re.search(words[w], diagString):
      print "The word", words[w], "appears in the grid"
      present = 1

#diagonals from the bottom up towards the right
for c in range(numColumns-1,-1,-1):
  r = 0
  diagVector = []
  while c >= 0:
    diagVector.append(grid[r][c])
    r=r+1
    c=c-1
  diagString = sep.join(diagVector)
  for w in range(len(words)):
    if re.search(words[w], diagString):
      print "The word", words[w], "appears in the grid"
      present = 1

#diagonals going from the righthand side
for r in range(1,numRows-1):
  c = numColumns-1
  diagVector = []
  while r <= numRows-1:
    diagVector.append(grid[r][c])
    r=r+1
    c=c-1
  diagString = sep.join(diagVector)
  for w in range(len(words)):
    if re.search(words[w], diagString):
      print "The word", words[w], "appears in the grid"
      present = 1

#### diagonals, upside down ####
#going to use the already stored UpsideDownGrid and use the same algorithms as before
for c in range(numColumns-1,-1,-1):
  r = 0
  diagVector = []
  while c >= 0:
    diagVector.append(upsideDownGrid[r][c])
    r=r+1
    c=c-1
  diagString = sep.join(diagVector)
  for w in range(len(words)):
    if re.search(words[w], diagString):
      print "The word", words[w], "appears in the grid"
      present = 1
      
for r in range(1,numRows-1):
  c = numColumns-1
  diagVector = []
  while r <= numRows-1:
    diagVector.append(upsideDownGrid[r][c])
    r=r+1
    c=c-1
  diagString = sep.join(diagVector)
  for w in range(len(words)):
    if re.search(words[w], diagString):
      print "The word", words[w], "appears in the grid"
      present = 1


"""




"""
---------------------------------------
"""


def scan(o, words, grid):
    """o is an object with our options in it"""
    finds = []
    words_range = range(len(words))
    for y in o.outer_loop:
        vector = []
        x = 0
        if o.desc:
          x = len(o.inner_loop) - 1
        if o.while_block:
          while y <= (len(o.outer_loop)-1):
            if o.flip_xy:
              vector.append(grid[y][x])
            else:
              vector.append(grid[x][y])
            y = y + 1 
            if o.desc:
              x = x - 1
            else:
              x = x + 1
          scanString = sep.join(vector)
          print "scanning " + scanString

        elif not o.inner_loop:
          scanString = sep.join(grid[y])

        else:
          for x in o.inner_loop:
            if o.flip_xy:
              vector.append(grid[x][y])
            else:
              vector.append(grid[y][x])
            scanString = sep.join(vector)

        for w in words_range:
          if o.test(words[w], scanString):
            finds.append(words[w])
    return finds

def printscan(o, words, grid):
  print "scanned " + o.tag
  the_scan = scan(o, words, grid)
  print the_scan
  return the_scan


# good trick for python lambda object
#  down_scan_opts = type('lamdbaobject', (object,), {})()

L2R = ScanOpts(range(numRows), False)
L2R.tag = "Left to Right"
finds = printscan(L2R, words, grid)

R2L = ScanOpts(range(numRows), range(numColumns-1,-1,-1))
R2L.tag = "Right to Left"
finds = printscan(R2L, words, grid)

T2B = ScanOpts(range(numRows), range(numColumns))
T2B.tag = "Top to Bottom"
T2B.flip_xy = True
finds = printscan(T2B, words, grid)

B2T = ScanOpts(range(numRows), range(numColumns-1,-1,-1))
B2T.tag = "Bottom to Top"
B2T.flip_xy = True
finds = printscan(B2T, words, grid)

DL2R = ScanOpts(range(numColumns), None)
DL2R.tag = "Middle Diagonal moving left to right"
DL2R.while_block = True
finds = printscan(DL2R, words, grid)

UL2R = ScanOpts(range(numColumns-1,-1,-1), None)
UL2R.tag = "Diagonally from the bottom left, going up to the right"
UL2R.while_block = True
UL2R.flip_xy = True
finds = printscan(UL2R, words, grid)

DR2L = ScanOpts(range(numColumns-1,-1,-1), range(numRows))
DR2L.tag = "Bottom right reading down to the left as we move up the right edge"
DR2L.while_block = True
DR2L.desc = True
DR2L.flip_xy = True
finds = printscan(DR2L, words, grid)

RR2L = ScanOpts(range(numColumns-1,-1,-1), range(numRows))
DR2L.tag = "Down and right to left and we move across the top row"
RR2L.while_block = True
RR2L.desc = True
RR2L.flip_xy = True
finds = printscan(RR2L, words, grid_upsidedown)




present = len(finds)

if present == 0:
  print "Sorry kid! None of the words you listed are in the grid."

