import numpy as np
import matplotlib.pyplot as plt
from random import randint
import os

SIZE = 3000
MAX = 512
MIN = 0

Defect_Map = np.loadtxt('text\\Defect_Map.txt')
Clear_Map = np.loadtxt('text\\Volcano_Clear_Map.txt')
Cloud_Map = np.loadtxt('text\\Cloud_Map.txt')

Volcano_vector = [1,1]
Cloud_vector = [-5,-5]
step = 2

for i in range(10):
    center_x, center_y = 1500, 1500  # Центр исходного массива
    half_size = 1000
    V_Map = Clear_Map[(center_x - half_size)+Volcano_vector[0]*step*i:(center_x + half_size)+Volcano_vector[0]*step*i,(center_y - half_size)+Volcano_vector[1]*step*i:(center_y + half_size)+Volcano_vector[1]*step*i]
    C_Map = Cloud_Map[(center_x - half_size)+Cloud_vector[0]*step*i:(center_x + half_size)+Cloud_vector[0]*step*i,(center_y - half_size)+Cloud_vector[1]*step*i:(center_y + half_size)+Cloud_vector[1]*step*i]
    D_Map = Defect_Map[center_x - half_size:center_x + half_size,center_y - half_size:center_y + half_size]
    Map = V_Map+C_Map+D_Map

    # Сохранение в папку film и images
    results_dir = "film"
    np.savetxt(os.path.join(results_dir,f'{i+1}.txt'), Map, fmt='%.0f')
    results_dir = "images"
    plt.imsave(os.path.join(results_dir,f'{i+1}.png'), Map, cmap='gray', vmin=MIN, vmax=MAX)

    plt.imshow(Map, cmap='gray', vmin=MIN, vmax=MAX)
    # plt.show()

print("Yep!")