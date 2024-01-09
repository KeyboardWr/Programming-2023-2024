# Jelly Bean Colour COunter
# Herman Li
 #Jan 9, 2024


# Version #1
# - count red pixels/ Beans
# - Re[prt pm the [ercemtage pf a;; red beans

from PIL import Image

import colour_helper

red_pixels = []

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

# Visit every pixel in the image
for y in range(jelly_bean_img):
    for x in range(jelly_bean_img):
    # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x,y))

    # If this pixel is red
        if colour_helper.pixel_to_name(current_pixel) == "red":
        # Store its location somewhere
            red_pixels.append(x,y)
print(red_pixels)


# Count all the locations of red pixels
# Divide by the total pixels in the image


# Generate the report

