
from PIL import Image
# numpy is something in-built or something that I downloaded as part of my Python installation so I don't need to do 'from'
# import numpy as np
from colorama import Fore, Back, Style

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# from PIL, I created an object called 'im' which is an instance of the Image class
img = Image.open(r"E:\Python\Projects\ASCII-Art\ascii-zebra.jpg")
#img.show()

# img. size returns width (number of pixel columns) x height (number of pixel rows)
print(img.format, img.size, img.mode)

# each block of lists outputted (in this case, printed) is a row of pixels in the image. Remember that matrices are R (rows) x C (columns)
# pixel_matrix = np.asarray(img)
#print(pixel_matrix)

'''
The below returns a flattened list of tuples representing RGB values for one pixel (not an array/matrix),
so let's do it manually instead of using numpy just as a super mini-challenge :)
'''

all_pixels = list(img.getdata())
#print(all_pixels)
#print(len(all_pixels))
pixel_matrix = []
starting_point = 0
for i in range(0, img.size[1]):
    pixel_matrix.append(all_pixels[starting_point : starting_point+img.size[0]])
    # update the starting point
    starting_point = starting_point+img.size[0]

#print(pixel_matrix)
#print(pixel_matrix[0])
#print(pixel_matrix[0][0])


# Remember that len(array) returns number of rows

def convertRGBtoBrightness(pixel_matrix, conversionType):
    #if we wanna invert the brightness, just do the reverse index or multiply values instead of dividing them to undo it
    brightness_matrix = []
    for x in range(0, len(pixel_matrix)):
        current_row = []
        for y in range(0, len(pixel_matrix[x])):
            pixel = pixel_matrix[x][y]
            #print(pixel)
            if conversionType == "average":
                temp = 0
                for i in range(0, len(pixel)):
                    temp += pixel[i]
                # len(pixel) is supposed to be 3
                average = temp / len(pixel)
                current_row.append(average)
            elif conversionType == "lightness":
                temp = (max(pixel) + min(pixel)) / 2
                current_row.append(temp)
            elif conversionType == "lumonisty":
                temp = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
                current_row.append(temp)
        brightness_matrix.append(current_row)
    return brightness_matrix

brightness_matrix = convertRGBtoBrightness(pixel_matrix, "average")


ASCII_matrix = []
# remember min brightness value is 0 and the max brightness value is 255
print(len(ASCII_CHARS))
# scale each brightness value to the ASCII characters by dividing each brightness value by 65
for i in range(0, len(brightness_matrix)):
    current_row = []
    for j in range(0, len(brightness_matrix[0])):
        divider = 255/len(ASCII_CHARS)
        scaled_val = brightness_matrix[i][j] / divider
        ASCII_val = ASCII_CHARS[int(scaled_val)-1]
        current_row.append(ASCII_val)
    ASCII_matrix.append(current_row)

for row in ASCII_matrix:
    # use list comprehensions because they're concise
    line = [pixel+pixel+pixel for pixel in row]
    # .join is better than using + for string concatenation because it is much faster
    print(Fore.GREEN + "".join(line))
