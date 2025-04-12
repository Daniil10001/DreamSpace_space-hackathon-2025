import numpy as np
import matplotlib.pyplot as plt
import os

SIZE = 3000
MAX = 512
MIN = 0

loc = 256  # Параметр положения (мода распределения)
scale = 50  # Параметр масштаба (чем больше - тем шире распределение)

for i in range(3):
    # Создание шума по Лапласу
    Laplace_Noise = np.random.laplace(loc=loc, scale=scale, size=(SIZE,SIZE))

    # Сохранение в папку text и images
    results_dir = "text"
    np.savetxt(os.path.join(results_dir,f'Laplace_Noise{i+1}.txt'), Laplace_Noise, fmt='%.0f')
    results_dir = "images"
    plt.imsave(os.path.join(results_dir,f'Laplace_Noise{i+1}.png'), Laplace_Noise, cmap='gray', vmin=MIN, vmax=MAX)

    # plt.imshow(Laplace_Noise, cmap='gray', vmin=MIN, vmax=MAX)
    # plt.show()

print("Yep!")