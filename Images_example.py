# Herman Li
# Dec 11, 2023
# Images Example


from PIL import Image

# Open up kid green
with Image.opem("./Images?kid-green.jpg") as im:
    
# Grab the pixel in the top left corner
    pixel = im.getpixel((0,0))
    print(pixel)
# print the pixel information
# print the pixel information