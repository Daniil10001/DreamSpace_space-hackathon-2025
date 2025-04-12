import numpy as np
import matplotlib.pyplot as plt
from random import randint
import os

SIZE = 3000
MAX = 512
MIN = 0

Clear_Map = np.loadtxt('text\\Volcano_Clear_Map.txt')
Cloud_Map = np.loadtxt('text\\Cloud_Map.txt')
for z in range(3):
    boba = 1 # Boba = отношению сигнал/шум (10, 5, 2)
    if z==0:
        boba = 10
    elif z==1:
        boba = 5
    else:
        boba =2
    Defect_Map = np.loadtxt(f'text\\Defect_Map{z+1}.txt')

    Volcano_vector = [1,1]
    Cloud_vector = [-5,-5]
    step = 2

    for i in range(10):
        center_x, center_y = 1500, 1500  # Центр исходного массива
        half_size = 1000
        V_Map = Clear_Map[(center_x - half_size)+Volcano_vector[0]*step*i:(center_x + half_size)+Volcano_vector[0]*step*i,(center_y - half_size)+Volcano_vector[1]*step*i:(center_y + half_size)+Volcano_vector[1]*step*i]
        C_Map = Cloud_Map[(center_x - half_size)+Cloud_vector[0]*step*i:(center_x + half_size)+Cloud_vector[0]*step*i,(center_y - half_size)+Cloud_vector[1]*step*i:(center_y + half_size)+Cloud_vector[1]*step*i]
        D_Map = (Defect_Map[center_x - half_size:center_x + half_size,center_y - half_size:center_y + half_size])*(2/boba) #калибруем величину шума
        Map = V_Map+C_Map+D_Map

        # Сохранение в папку film и images
        results_dir = "film"
        np.savetxt(os.path.join(results_dir,f'{z}{i+1}.txt'), Map, fmt='%.0f')
        results_dir = "images"
        plt.imsave(os.path.join(results_dir,f'{z}{i+1}.png'), Map, cmap='gray', vmin=MIN, vmax=MAX)

        # plt.imshow(Map, cmap='gray', vmin=MIN, vmax=MAX)
        # plt.show()

print("Yep!")