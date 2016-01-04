def blend(pic1, pic2):

  # Assumes the pictures are the same size

  width, height = getWidth(pic1), getHeight(pic1)

  blendedPic = makeEmptyPicture(width, height)

  for x in xrange(width):
    for y in xrange(height):
      
      targetPixel = getPixel(blurPic, x, y)

      p1 = getPixel(pic1, x, y)
      p2 = getPixel(pic2, x, y)

      r1, g1, b1 = getRed(p1), getGreen(p1), getBlue(p1)
      r2, g2, b2 = getRed(p2), getGreen(p2), getBlue(p2)

      blurColor = makeColor( (r1+r2)/2 , (g1+g2)/2, (b1+b2)/2 )

      setColor(targetPixel, blurColor)

  return blurPic

#Steps to take in command\/
#p1 = makePicture(pickAFile()) *this line choses the dome
#p2 = makePicture(pickAFile()) *this line choses the surface
#blendedPic = blend(p1, p2) *this executes the algorithm to the desired pictures, in this case P1(the dome) ontop P2(the surface)
#show(blendedPic) *this finally shows the effect on screen

def BW(pic):
  picture = duplicatePicture(pic)
  for px in getPixels(picture):
    
    luminance = ( getRed(px) + getBlue(px) + getGreen(px) )/3
    if luminance < 50:
      setColor(px, makeColor(50, 50, 50))
    elif luminance < 100:
      setColor(px, makeColor(100, 100, 100))
    elif luminance < 150:
      setColor(px, makeColor(150, 150, 150))
    elif luminance < 200:
      setColor(px, makeColor(200, 200, 200))
    else:
      setColor(px, white)
  return picture
# This effect essentially tones down All RGB (red, green & blue) values of the image leaving it a simple black and white frame.
# STEPS TO TAKE: \/
# pic = makePicture(pickAFile())
# BWpic = BW(pic)
# show(BWpic)

def edge(pic, precision = 4): #the value at the end of this line determines the strength of effect (4 is recommended)
  
  picture = duplicatePicture(pic)
  width, height = getWidth(pic) , getHeight(pic)
  
  for y in xrange(height - 1):
    for x in xrange(width - 1):
      
      px = getPixel(picture, x, y) # original pixel
      right = getPixel(picture, x + 1, y)
      below = getPixel(picture, x, y + 1)
      
      luminance = lambda px: (getRed(px) + getBlue(px) + getGreen(px) )/3
      
      LR = luminance(right)
      LB = luminance(below)
      LO = luminance(px)
      
      if abs(LR - LO) > precision and abs(LB - LO) > precision:
        setColor(px, black)
      else:
        setColor(px, white)
  
  return picture

# picture = makePicture(pickAFile())
# edgeSpace = edge(picture)
# show(edgeSpace)

def stretch(pic, widthStretch = 1, heightStretch = 1):
  widthStretch = abs(int(widthStretch))
  heightStretch = abs(int(heightStretch))
  
  w, h = getWidth(pic), getHeight(pic)
  stretchedImage = makeEmptyPicture(w*widthStretch, h*heightStretch)
  
  for y in xrange(0, h*heightStretch, heightStretch):
    for x in xrange(0, w*widthStretch, widthStretch):
      color = getColor(getPixel(pic, x/widthStretch, y/heightStretch))
      
      for cellY in xrange(y, y + heightStretch):
        for cellX in xrange(x, x + widthStretch):
          
          targetPixel = getPixel (stretchedImage, cellX, cellY )
          setColor(targetPixel, color)
          
  return stretchedImage

#STEPS TO TAKE:
# y = makePicture(pickAFile())
# i = stretch(y, #number, #number) // y is the image, the first value is the height stretch, the second value is width stretch
# show(i)
