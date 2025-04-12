import numpy as np
import matplotlib.pyplot as plt
import os

#Суперпозиция шумов

SIZE = 3000
MAX = 512
MIN = 0

for i in range(3):
    picture_Gaus = np.loadtxt(f'text\\Gaussian_Noise{i+1}.txt')
    picture_Koshi = np.loadtxt(f'text\\Cauchy_Noise{i+1}.txt')
    picture_Laplas = np.loadtxt(f'text\\Laplace_Noise{i+1}.txt')
    # picture_Cloud = np.loadtxt('text\\Cloud_Map.txt')

    Map_1 = (picture_Gaus+picture_Koshi+picture_Laplas)/3

    # Сохранение в папку noise и images
    results_dir = "noise"
    np.savetxt(os.path.join(results_dir,f'{i+1}.txt'), Map_1, fmt='%.0f')
    results_dir = "images"
    plt.imsave(os.path.join(results_dir,f'Map_{i+1}.png'), Map_1, cmap='gray', vmin=MIN, vmax=MAX)

    # plt.imshow(Map_1, cmap='gray', vmin=MIN, vmax=MAX)
    # plt.show()

print("Yep!")