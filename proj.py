####################
##LOADING PICTURES##
####################

pictures = []                                     ##Creates the list pictures
fldr = "c:/Users/Kailey/Desktop/CST205PR1/"       ##pathway to pictures I want
                                                  ##
                                                  ##
im1 = makePicture(fldr + "1.png")                 ##Lines 9-26: Making picture objects from pathway files
pictures.append(im1)                              ##and appending them (adding them) the the pictures list created earlier
im2 = makePicture(fldr + "2.png")                 ##
pictures.append(im2)                              ##
im3 = makePicture(fldr + "3.png")                 ##
pictures.append(im3)                              ##
im4 = makePicture(fldr + "4.png")                 ##
pictures.append(im4)                              ##
im5 = makePicture(fldr + "5.png")                 ##
pictures.append(im5)                              ##
im6 = makePicture(fldr + "6.png")                 ##
pictures.append(im6)                              ##
im7 = makePicture(fldr + "7.png")                 ##
pictures.append(im7)                              ##
im8 = makePicture(fldr + "8.png")                 ##
pictures.append(im8)                              ##
im9 = makePicture(fldr + "9.png")                 ##
pictures.append(im9)                              ##
                                                  ##
width = getWidth (im1)                            ##
height = getHeight (im1)                          ##
finpic = makeEmptyPicture(width,height)           ##Creates a blank picture that will be where the new pixels are placed

##############################
##GETTING PIXELS USING LOOPS##
##############################

redpixl = []                                      ##Creates redpixl list, where red pixel values will be stored
grpixl = []                                       ##Creates grpixl list, where green pixel values will be stored
blupixl = []                                      ##Creates blupixl list, where blue pixel values will be stored
width = getWidth(im1)                             ##Determines the width of the images, which will be the width of the new image
height = getHeight(im1)                           ##Determines the height of the images, which will be the height of the new image
                                                  ##
for x in range (0,width):                         ##Following code will loop as long as the x value is within the range
  for y in range (0,height):                      ##Following code will loop as long as the y value is within the range
    for index in range(0,9):                      ##Loop chooses which image the program looks at to collect values
      pix = getPixel(pictures[index], x, y)       ##Gets the pixel RGB values for each pixel in every image (1-9)
                                                  ##
      redpx = getRed(pix)                         ##Stores R value of the RGB value into the variable redpx
      greenpx = getGreen(pix)                     ##Stores G value of the RGB value into the variable greenpx
      bluepx = getBlue(pix)                       ##Stores B value of the RGB value into the variable bluepx
                                                  ##
      redpixl.append(redpx)                       ##Lines49-51 store the RGB values obtained into the corresponding lists
      grpixl.append(greenpx)                      ##
      blupixl.append(bluepx)                      ##
                                                  ##
    redpixl.sort()                                ##Lines 53-55 sorts the values in each list from smallest to largest value
    grpixl.sort()                                 ##
    blupixl.sort()                                ##
                                                  ##
    rlength = len(redpixl)                        ##Lines 57-59 determines the length of each list and stores that value into
    glength = len(grpixl)                         ##the corresponding variable. This is important for determining what value
    blength = len(blupixl)                        ##is the median value for each pixel.

#######################################
##DETERMINING THE NEW PIXEL RGB VALUE##
#######################################
    
    chpix = getPixel(finpic, x, y)                                                         ##Variable created for the Final Picture's pixels
    newcolor = makeColor(redpixl[rlength/2], grpixl[glength/2], blupixl[blength/2])        ##A color is created by choosing the middle value of each of the RGB lists for every pixel within the width and height range
    setColor (chpix, newcolor)                                                             ##The old pixel is substituted with the new pixel (color)

##########################
##TYING UP LOOSE STRINGS##
##########################
    redpixl = []           ##Each list is cleared to help the program run faster.
    grpixl = []            ##
    blupixl = []           ##

#################
##FINAL PRODUCT##
#################

show (finpic)              ##The final picture (without the pesky tourist) is displayed

#############
## CREDITS ##
#############

##Project by: Kailey Sarmiento
##Team: 15, Group: C
##Team Members: Anthony Avina & Israel Andrade (Thank you both for all your help!)
##TA: Lesly Garcia Jimenez (Thank you for your help!)
##CST 231, Spring 2016