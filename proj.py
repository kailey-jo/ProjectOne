##loading pictures
pictures = []
fldr = "c:/Users/Kailey/Desktop/CST205PR1/"
im1 = makePicture(fldr + "1.png")
pictures.append(im1)
im2 = makePicture(fldr + "2.png")
pictures.append(im2)
im3 = makePicture(fldr + "3.png")
pictures.append(im3)
im4 = makePicture(fldr + "4.png")
pictures.append(im4)
im5 = makePicture(fldr + "5.png")
pictures.append(im5)
im6 = makePicture(fldr + "6.png")
pictures.append(im6)
im7 = makePicture(fldr + "7.png")
pictures.append(im7)
im8 = makePicture(fldr + "8.png")
pictures.append(im8)
im9 = makePicture(fldr + "9.png")
pictures.append(im9)

finpic = makeEmptyPicture(width,height)

##getting pixels using loop
redpixl = []
grpixl = []
blupixl = []
width = getWidth(im1)
height = getHeight(im1)

for x in range (0,width):
  for y in range (0,height):
    for index in range(0,9):
      pix = getPixel(pictures[index], x, y)
      
      redpx = getRed(pix)
      greenpx = getGreen(pix)
      bluepx = getBlue(pix)
      
      redpixl.append(redpx)
      grpixl.append(greenpx)
      blupixl.append(bluepx)
      
    redpixl.sort()
    grpixl.sort()
    blupixl.sort()
    
    rlength = len(redpixl)
    glength = len(grpixl)
    blength = len(blupixl)
    
    chpix = getPixel(finpic, x, y) 
    newcolor = makeColor(redpixl[rlength/2], grpixl[glength/2], blupixl[blength/2])
    setColor (chpix, newcolor)
    
    redpixl = []
    grpixl = []
    blupixl = []
show (finpic)