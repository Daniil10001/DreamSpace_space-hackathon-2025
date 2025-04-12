import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import os

MAX = 512
MIN = 0
SIZE = 3000
SCALE = SIZE//512 * 200

def Generate_Cloud(width = SIZE, height = SIZE, threshold=0.4, scale=SCALE, octaves=4, seed=36):
    noise = PerlinNoise(octaves=octaves, seed=seed)
    Cloud_Map = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            Cloud_Map[i][j] = noise([i / scale, j / scale])

    # Нормализация и применение порога
    Cloud_Map = (Cloud_Map - Cloud_Map.min()) / (Cloud_Map.max() - Cloud_Map.min())
    Binary_Map = Cloud_Map < threshold # 0 или 1
    return Binary_Map*MAX


Cloud_Map = Generate_Cloud() # Генерация облаков

# Сохранение в папку text и images
results_dir = "text"
np.savetxt(os.path.join(results_dir,"Cloud_Map.txt"), Cloud_Map, fmt='%.0f')
results_dir = "images"
plt.imsave(os.path.join(results_dir,'Cloud_Map.png'), Cloud_Map, cmap='gray', vmin=MIN, vmax=MAX)


plt.imshow(Cloud_Map, cmap='gray', vmin=MIN, vmax=MAX)
plt.show()

print("Yep!")