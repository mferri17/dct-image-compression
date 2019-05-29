
import os
import random
import string
from datetime import datetime
import imageio
import numpy as np
from scipy.fftpack import dctn, idctn


def compress_image(user, image, F, d):

    # paths
    imagename = randomString(10)
    image_folder = f'media/{user}/{imagename}'

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    image_path = f'{image_folder}/1-original.jpg'
    image_grey_path = f'{image_folder}/2-gray.jpg'
    image_compress_path = f'{image_folder}/3-grey-compress-F{F}_d{d}.jpg'

    # input image
    img = imageio.imread(image)
    bnimg = img[:, :, 0]
    imageio.imwrite(image_path, img)  # original image
    imageio.imwrite(image_grey_path, bnimg)  # black & white image

    (rows, cols) = bnimg.shape

    # splitting bnimg in FxF blocks
    for i in range(0, int(rows / F)):
        for j in range(0, int(cols / F)):

            rowsLower = i * F
            colsLower = j * F
            rowsUpper = (i+1) * F
            colsUpper = (j+1) * F
            block = bnimg[rowsLower:rowsUpper, colsLower:colsUpper]

            # c = DCT2(f)
            c = dctn(block, type=2, norm='ortho')

            # filtering frequences to the right of d-diagonal
            (blockRows, blockCols) = block.shape
            for k in range(0, blockRows - 1):
                for l in range(0, blockCols - 1):
                    if(k + l >= d):
                        c[k, l] = 0

            # ff = IDCT2(c)
            ff = idctn(c, type=2, norm='ortho')

            # normalizing idct
            ff = np.round(ff)
            for index, value in np.ndenumerate(ff):
                if value < 0:
                    ff[index] = 0
                elif value > 255:
                    ff[index] = 255

            bnimg[rowsLower:rowsUpper, colsLower:colsUpper] = ff


    imageio.imwrite(image_compress_path, bnimg)  # compress image
    # return image_path, image_compress_path


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
