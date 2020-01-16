f = 'C:\\Users\\AAMP\\Documents\\CompSciFirst Year\\CPS 109\\tinyscene.jpg'
p = 'C:\\Users\\AAMP\\Documents\\CompSciFirst Year\\CPS 109\\tinywaldo.jpg'
template = makePicture(f)
searchImage = makePicture(p)
setMediaPath('C:\\Users\\AAMP\\Documents\\CompSciFirst Year\\CPS 109\\')

def compareOne(template, searchImage,x1,y1):
  w = getWidth(template) #this is where you get the width of the template
  h = getHeight(template) #this is where you get the height of the template
  diff = 0 #this is where you initialize a variable for the final difference 
  for x in range (x1,x1+w): #this is where you go through the width of the template
    for y in range (y1,y1+h): #this is where you go through the height of the template
      pixel = getPixel(template,x-x1,y-y1) #this is where you get a pixel from the template going from the width and height
      pixel2 = getPixel(searchImage,x,y) #This is where you get a pixel from searchimage going from the x and y inouts
      r = getRed(pixel) #here we get the red pixels for template
      r1 = getRed(pixel2) #here we get the red pixels for search image
      diff += abs(r1-r)
  return diff #here you return
      
      
def compareAll(template,searchImage):
  w = getWidth(searchImage) #here we get the width of the search image
  h = getHeight(searchImage) #here we get the height of the search image
  tw = getWidth(template) #here we get the width of the template
  th = getHeight(template) #here we get the height of the template
  matrix = [[0 for i in range(w-tw)] for j in range(h-th)] #here we make the matrix
  for x in range(w-tw): #here we set the range from the width of the search image minus the template width
    for y in range(h-th):  #here we set the range from the height of the search image minus the template height
      matrix[y][x]= compareOne(template,searchImage,x,y) #here we set the matrix to compareOne function
  return matrix #here we return the matrix
    
def find2Dmin(matrix):
  minrow = 0 #here we initialize the minrow
  mincol = 0 #here we initiaize the mincol
  lownum = matrix[0][0] #here we get lownum equal to the matrix coordinate
  for x in range (len(matrix)): #here we go through length of the matrix 
    for y in range(len(matrix[x])): #here we go through the length of the matrix column
      if matrix[x][y]<lownum: #here we check if the matrix is less than lownum
        lownum = matrix[x][y] #if so, then we set lownum to the matrix
        minrow = y #we make minrow equal to y 
        mincol = x #we make mincol equal to x
  return (minrow, mincol) #here we return the minrow and mincol
    
def displayMatch(searchImage,x1,y1,w1,h1,color):
  pixels = getPixels(searchImage) #here we get all the pixels of the search image
  for pixel in pixels: #here we go through all of the pixels of the search image
    x = getX(pixel) #here we get the x coordinates of the search image
    y = getY(pixel) #here we get the y coordinates of the search image
    if x1<=x<=(x1+w1) and y1<=y<=(y1+h1): #here we check if x1 is less than or equal to x which is less than or equal to x1 plus 2 or x1 plus width minus 2 is less than or equal to y which is less than or equal to y1 plus height
      if x1<=x<=(x1+2) or (x1+w1-2)<=x<=(x1+w1) or y1<=y<=(y1+2) or (y1+h1-2)<=y<=(y1+h1):
        setColor(pixel,color) #here we set the color
  show(searchImage)
  

def grayscale(pic):
  pixels = getPixels(pic) #this is where you gather all of the pixels for the picture
  for pixel in pixels: #this is where you go through each pixel in the the picture
    red = getRed(pixel) #here we get the red pixels
    green = getGreen(pixel) #here we get the green pixels
    blue = getBlue(pixel) #here we get the blue pixels
    intensify = (red+green+blue)/3 #here we grayscale the picture
    setColor(pixel,makeColor(intensify,intensify, intensify)) #here we set the gray color

  
def findWaldo(template,searchImage):
  grayscale(template) #here you gray scale the template
  grayscale(searchImage) #here you gray scale the searchimage
  matrix = compareAll(template,searchImage) #here you get the matrix from the compareAll function
  minXY = find2Dmin(matrix) #here we get the smallest coordinate from te find2Dmin function
  displayMatch(searchImage,minXY[0],minXY[1],getWidth(template),getHeight(template),green) #here we make the box around Waldo