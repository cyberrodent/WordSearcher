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

  def drawType(self, gtype):
    """Print the grid to stdout"""
    if gtype == "mirror":
      mirror = self.mirror()
      for x in range(self.numRows):
        print mirror[x]
    elif gtype == "upsidedown":
      usd = self.upsidedown()
      for x in range(self.numRows):
        print usd[x]
    elif gtype == "upsidedownmirror":
      usd = self.upsidedownmirror()
      for x in range(self.numRows):
        print usd[x]

  def upsidedownmirror(self):
    """Return upside down mirror version of grid"""
    for l in range(self.numRows):
      upsideDownGrid = []
      for l in range(self.numCols-1,-1,-1):
        upsideDownGrid.append(self.grid[l][::-1])
    return upsideDownGrid

  def upsidedown(self):
    """Return upsidedown grid"""
    for l in range(self.numRows):
      upsideDownGrid = []
      for l in range(self.numCols-1,-1,-1):
        upsideDownGrid.append(self.grid[l])
    return upsideDownGrid

  def mirror(self):
    """Return a mirror of the grid"""
    for l in range(self.numRows):
      mirrorGrid = []
      for l in range(self.numCols):
        row = self.grid[l][::-1]
        mirrorGrid.append(row)
    return mirrorGrid




"""
given some options, a list of words and a grid,
find the words in the grid
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





all_finds = []
present = 0

numbers = raw_input("How many rows and how many columns do you want the grid to have? (Enter as: rows,columns) ")
parsed = [int(x.strip()) for x in numbers.split(',')]
numRows = parsed[0]
numColumns = parsed[1]


#making the grid
gameGrid = Grid(numRows, numColumns)
grid = gameGrid.get()
grid_upsidedown = gameGrid.upsidedown()
grid_mirror = gameGrid.mirror()
grid_upsidedownmirror = gameGrid.upsidedownmirror()
gameGrid.draw()



wordString = raw_input("What words would you like to search for? Please enter them separated by a comma. (i.e. cat,dog,fish)" )
words = wordString.split(',')
sep=''




#
# Setup scan options and scan for our words
#

# Orthogonal
L2R = ScanOpts(range(numRows), False)
L2R.tag = "Left to Right"
finds = printscan(L2R, words, grid)
all_finds.append(finds)

R2L = ScanOpts(range(numRows), range(numColumns-1,-1,-1))
R2L.tag = "Right to Left"
finds = printscan(R2L, words, grid)
all_finds.append(finds)


# Orthogonal
T2B = ScanOpts(range(numRows), range(numColumns))
T2B.flip_xy = True
T2B.tag = "Top to Bottom"
finds = printscan(T2B, words, grid)

all_finds.append(finds)
B2T = ScanOpts(range(numRows), range(numColumns-1,-1,-1))
B2T.flip_xy = True
B2T.tag = "Bottom to Top"
finds = printscan(B2T, words, grid)
all_finds.append(finds)



# TODO: With the grid variants we should be able to simplify these
# and probably the scan routine too - just hand in the right 
# grid variants to achieve all the scans we need.

# Top Down, Left to Right Diagonal

# starts at the "bottom" of the grid and attempts to find
# top-down left-right matches, scanning from the bottom
# to the top of the grid
UL2R = ScanOpts(range(numColumns-1,-1,-1), None)
UL2R.while_block = True
UL2R.flip_xy = True
UL2R.tag = "Diagonal: TopDown LeftRight x=0 "
finds = printscan(UL2R, words, grid)
all_finds.append(finds)
# Top Down Left to Right Diagonal
# Starting at 0,0 and scanning diagonally down l2r.
DL2R = ScanOpts(range(numColumns), None)
DL2R.while_block = True
DL2R.flip_xy = False
DL2R.tag = "Diagonal: TopDown LeftRight y=0 "
finds = printscan(DL2R, words, grid)
all_finds.append(finds)

# do the 2 above scans with the upside down grid
UL2R.tag = "Diagonal: BottomUp LeftRight y=maxy "
finds = printscan(UL2R, words, grid_upsidedown)
all_finds.append(finds)
DL2R.tag = "Diagonal: BottomUp LeftRight y=maxy "
finds = printscan(DL2R, words, grid_upsidedown)
all_finds.append(finds)

# do the 2 above scans with the mirror grid
UL2R.tag = "Diagonal: TopDown RightLeft x=maxx "
finds = printscan(UL2R, words, grid_mirror)
all_finds.append(finds)
DL2R.tag = "Diagonal: TopDown  RightLeft y=0"
finds = printscan(DL2R, words, grid_mirror)
all_finds.append(finds)

# do the 2 above scans with the mirror grid
UL2R.tag = "Diagonal: BottomUp RightLeft x=maxx "
finds = printscan(UL2R, words, grid_upsidedownmirror)
all_finds.append(finds)
DL2R.tag = "Diagonal: BottomUp RightLeft y=maxy "
finds = printscan(DL2R, words, grid_upsidedownmirror)
all_finds.append(finds)


present = len(all_finds)

if present == 0:
  print "Sorry kid! None of the words you listed are in the grid."

