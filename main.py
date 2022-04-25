# The horizontal (x) and vertical (y) movement of the pictures.
# Negative values are possible for movement into opposite direction.

x_movement = 0
y_movement = 0

file_red = 'red.txt'
file_blue = 'blue.txt'

# Do not edit below!

import linecache
import matplotlib
from matplotlib import pyplot
import numpy as np

red, blue = [], []


# Importing textfile, formatting it into arrays
def file_formatting(txtfile_name, array):
    imported_array = linecache.getlines(txtfile_name)
    for line in imported_array:
        line = line.replace('\n', '')
        oneD = line.split('\t')
        array.append(oneD)

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = float(array[i][j])

    return array


# Movement of arrays horizontally where one of the arrays stays static
def moveX(arrayMoving, arrayStatic, pixelsAmount):
    for i in range(len(arrayStatic)):
        for c in range(pixelsAmount):
            arrayStatic[i].insert(0, 0)

    for a in range(len(arrayMoving)):
        for z in range(pixelsAmount):
            arrayMoving[a].append(0)


# Movement of arrays vertically where one of the arrays stays static
def moveY(arrayMoving, arrayStatic, pixelsAmount):
    for a in range(pixelsAmount):
        arrayMoving.append([])
        for i in range(len(arrayMoving[0])):
            arrayMoving[len(arrayMoving) - 1].append(0)

    for b in range(pixelsAmount):
        arrayStatic.insert(0, [])
        for i in range(len(arrayStatic[50])):
            arrayStatic[0].append(0)


# Converting the image to a .txt file
def writetext(array, filename):
    with open(filename, 'w') as f:
        for i in range(len(array)):
            if i > 0:
                f.write('\n')
            for j in range(len(array[i])):
                f.write(str(array[i][j]))
                if j < len(array[i]) - 1:
                    f.write('\t')


# Calculating percentage of pixels that are blue + print it to terminal
def calculate_percentages(input_array):
    b = len(input_array)
    a = np.array(input_array)
    a[a > 0] = 0
    a = a[a != 0]
    print(f'Amount of pixels > 0: {len(a)}')
    print(f'Amount of pixels in total {((b - abs(x_movement)) * (b - abs(y_movement)))}')
    print(f'{len(a) / ((b - abs(x_movement)) * (b - abs(y_movement))) * 100}%')


# Create results array and creating graphical image.
def create_results(base, subtract):
    result = np.subtract(np.array(subtract, dtype=float), np.array(base, dtype=float), dtype=float)
    slicedresult = result[abs(y_movement):len(blue) - abs(y_movement), abs(x_movement):len(blue) - abs(x_movement)]

    calculate_percentages(slicedresult)

    # Creating image
    fig = pyplot.figure()
    colormap = matplotlib.colors.LinearSegmentedColormap.from_list('my_colormap', ['blue', 'white', 'red'], 256)
    img2 = pyplot.imshow(slicedresult, cmap=colormap, clim=(-0.1, 0.1))
    pyplot.colorbar(img2, cmap=colormap)
    pyplot.xlabel('Amount of Pixels Horizontally')
    pyplot.ylabel('Amount of Pixels Vertically')
    fig.show()


# Executing functions
def main():
    file_formatting(f'{file_blue}', blue)
    file_formatting(f'{file_red}', red)

    # If statements below enable positive and negative movement.
    if x_movement >= 0:
        moveX(blue, red, abs(x_movement))
    else:
        moveX(red, blue, abs(x_movement))

    if y_movement >= 0:
        moveY(blue, red, abs(y_movement))
    else:
        moveY(red, blue, abs(y_movement))

    create_results(blue, red)


main()
