#given the number of columns and rows for array of random letters, see if any of the provided words are in the grid.
import random
import re
import string

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


present = 0

numbers = raw_input("How many rows and how many columns do you want the grid to have? (Enter as: rows,columns) ")
parsed = [int(x.strip()) for x in numbers.split(',')]
numRows = parsed[0]
numColumns = parsed[1]


#making the grid
gameGrid = Grid(numRows, numColumns)
grid = gameGrid.get()
gameGrid.draw()


wordString = raw_input("What words would you like to search for? Please enter them separated by a comma. (i.e. cat,dog,fish)" )
words = wordString.split(',')
sep=''

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

if present == 0:
  print "Sorry kid! None of the words you listed are in the grid."

