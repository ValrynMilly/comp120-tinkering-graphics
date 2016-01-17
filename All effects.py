def blend(pic1, pic2):

  # Assumes the pictures are the same size

  width, height = getWidth(pic1), getHeight(pic1)

  blendedPic = makeEmptyPicture(width, height)

  for x in xrange(width):
    for y in xrange(height):
      
      targetPixel = getPixel(blendedPic, x, y)

      p1 = getPixel(pic1, x, y)
      p2 = getPixel(pic2, x, y)

      r1, g1, b1 = getRed(p1), getGreen(p1), getBlue(p1)
      r2, g2, b2 = getRed(p2), getGreen(p2), getBlue(p2)

      blendedColor = makeColor( (r1+r2)/2 , (g1+g2)/2, (b1+b2)/2 )

      setColor(targetPixel, blendedColor)

  return blendedPic

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

def negative(picture):

  copy = duplicatePicture(picture)

  for px in getPixels(copy):
    
    R = getRed(px)
    G = getGreen(px)
    B = getBlue(px)
    
    negativeColor = makeColor(255 - R, 255-G, 255-B)
    setColor(px, negativeColor)
      
  return copy


# This is the program that would run all effects with one input.
# The images I used were the same size of 600px, 600px
# Images included with source code
# P1 is Dome
# P2 is Pillars of creation

def main():
  p1 = makePicture(pickAFile())
  p2 = makePicture(pickAFile())
  blendedPic = blend(p1, p2)
  show(blendedPic)  
  BWpic = BW(blendedPic)
  show(BWpic)
  edgeSpace = edge(BWpic)
  show(edgeSpace)
  negativePic = negative(edgeSpace)
  show(negativePic)