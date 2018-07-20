# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image


# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename)


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(any_img):
    any_img.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(any_img, filename):
    any_img.save(filename)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(any_img):
    new_img = Image.new("RGB" , any_img.size)

    #In the Obamicon filter,
    #lighter colors get set to yellow. >546
    yellow = (252,227,166)
    # Medium-light colors get coded as light blue. 346 < intensity <= 546
    lightBlue = (112,150,158)
    #Medium-dark colors get set to red. 182 <= intensity <= 364
    red = (217,26,33)
    # Dark colors get set to dark blue. intensity < 182
    darkBlue = (0,51,76)
    # Gather data into list
    newPixels = []
    #Get data/list of pixels from original image
    ImagePixel = list(any_img.getdata())

    for individualPixel in ImagePixel :
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue

    #lighter colors get set to yellow. >546
    # Medium-light colors get coded as light blue. 346 < intensity <= 546
    #Medium-dark colors get set to red. 182 <= intensity <= 364
    # Dark colors get set to dark blue. intensity < 182
        if intensity < 182 :
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182 :
            newPixels.append(red)
        elif intensity < 546 and intensity >= 364 :
            newPixels.append(lightBlue)
        else :
            newPixels.append(yellow)
    new_img.putdata(newPixels)
    return new_img

def Kaylie(any_img):
    new_img = Image.new("RGB" , any_img.size)

    #In the Obamicon filter,
    #lighter colors get set to yellow. >546
    yellow = (0,0,128)
    # Medium-light colors get coded as light blue. 346 < intensity <= 546
    lightBlue = (199,21,133)
    #Medium-dark colors get set to red. 182 <= intensity <= 364
    red = (238,44,44)
    # Dark colors get set to dark blue. intensity < 182
    darkBlue = (42,36,34)
    # Gather data into list
    newPixels = []
    #Get data/list of pixels from original image
    ImagePixel = list(any_img.getdata())

    for individualPixel in ImagePixel :
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue

    #lighter colors get set to yellow. >546
    # Medium-light colors get coded as light blue. 346 < intensity <= 546
    #Medium-dark colors get set to red. 182 <= intensity <= 364
    # Dark colors get set to dark blue. intensity < 182
        if intensity < 182 :
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182 :
            newPixels.append(red)
        elif intensity < 546 and intensity >= 364 :
            newPixels.append(lightBlue)
        else :
            newPixels.append(yellow)
    new_img.putdata(newPixels)
    return new_img
