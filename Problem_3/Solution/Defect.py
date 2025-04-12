import numpy as np
import matplotlib.pyplot as plt
from random import randint
import os

SIZE = 3000
MAX = 512
MIN = 0

Map = np.loadtxt('noise\\1.txt')

for i in range(round(10e-3 * SIZE**2)):
    x, y = randint(0,SIZE-1), randint(0,SIZE-1)
    Map[x, y] = randint(450, 512)


# Сохранение в папку text и images
results_dir = "text"
np.savetxt(os.path.join(results_dir,"Defect_Map.txt"), Map, fmt='%.0f')
results_dir = "images"
plt.imsave(os.path.join(results_dir,'Defect_Map.png'), Map, cmap='gray', vmin=MIN, vmax=MAX)

plt.imshow(Map, cmap='gray', vmin=MIN, vmax=MAX)
plt.show()

print("Yep!")