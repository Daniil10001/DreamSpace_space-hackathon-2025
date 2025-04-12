import numpy as np
import matplotlib.pyplot as plt
import os

SIZE = 3000
MAX = 512
MIN = 0

loc = 256 # Параметр положения (аналог среднего)
scale = 50 # Параметр масштаба (аналог стандартного отклонения)

# Создание шума по Коши
Cauchy_Noise = np.random.standard_cauchy((SIZE,SIZE)) * scale + loc

# Сохранение в папку text и images
results_dir = "text"
np.savetxt(os.path.join(results_dir,"Cauchy_Noise.txt"), Cauchy_Noise, fmt='%.0f')
results_dir = "images"
plt.imsave(os.path.join(results_dir,'Cauchy_Noise.png'), Cauchy_Noise, cmap='gray', vmin=MIN, vmax=MAX)

plt.imshow(Cauchy_Noise, cmap='gray', vmin=MIN, vmax=MAX)
plt.show()

print("Yep!")