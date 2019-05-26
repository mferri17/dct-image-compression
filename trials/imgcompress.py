import imageio
import numpy as np
from scipy.fftpack import dctn, idctn

# input parameters
F = 8
d = 4

# input image
img = imageio.imread('imageio:astronaut.png') 


bnimg = img[:, :, 0]  
imageio.imwrite('imgs/astronaut.jpg', img) # original image
imageio.imwrite('imgs/astronaut-gray.jpg', bnimg) # black & white image


(rows, cols) = bnimg.shape

# splitting bnimg in FxF blocks
for i in range(1, int(rows / F)):
    for j in range(1, int(cols / F)):

        rowsLower = (i-1) * F
        colsLower = (j-1) * F
        rowsUpper = i * F
        colsUpper = j * F
        block = bnimg[rowsLower:rowsUpper, colsLower:colsUpper]

        # c = DCT2(f)
        c = dctn(block, type=2, norm='ortho')  

        # filtering frequences to the right of d-diagonal
        (blockRows, blockCols) = block.shape
        for k in range(0, blockRows - 1):
            for l in range(0, blockCols - 1):
                if(k + l >= d):
                    c[k,l] = 0

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



imageio.imwrite(f'imgs/astronaut-gray-compress-F{F}_d{d}.jpg', bnimg) # compress image