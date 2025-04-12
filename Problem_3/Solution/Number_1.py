import numpy as np
import matplotlib.pyplot as plt
import os

SIZE = 3000
MAX = 512
MIN = 0

picture_Gaus = np.loadtxt('text\\Gaussian_Noise.txt')
picture_Koshi = np.loadtxt('text\\Cauchy_Noise.txt')
picture_Laplas = np.loadtxt('text\\Laplace_Noise.txt')
# picture_Cloud = np.loadtxt('text\\Cloud_Map.txt')

Map_1 = (picture_Gaus+picture_Koshi+picture_Laplas)/3

# Сохранение в папку noise и images
results_dir = "noise"
np.savetxt(os.path.join(results_dir,"1.txt"), Map_1, fmt='%.0f')
results_dir = "images"
plt.imsave(os.path.join(results_dir,'Map_1.png'), Map_1, cmap='gray', vmin=MIN, vmax=MAX)

plt.imshow(Map_1, cmap='gray', vmin=MIN, vmax=MAX)
plt.show()

print("Yep!")