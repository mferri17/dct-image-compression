import numpy as np
from scipy.fftpack import dctn, idctn

array = np.array([231, 32, 233, 161, 24, 71, 140, 245])
matrix = np.matrix('231 32 233 161 24 71 140 245;247 40 248 245 124 204 36 107;234 202 245 167 9 217 239 173;193 190 100 167 43 180 8 70;11 24 210 177 81 243 8 112;97 195 203 47 125 114 165 181;193 70 174 167 41 30 127 245;87 149 57 192 65 129 178 228')

dct1 = dctn(array, type = 2, norm='ortho')
dct2 = dctn(matrix, type = 2, norm='ortho')

check1 = idctn(dct1, type=2, norm='ortho')
check2 = idctn(dct2, type=2, norm='ortho')

print(np.allclose(array, check1))
print(np.allclose(matrix, check2))