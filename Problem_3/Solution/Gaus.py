import numpy as np
import matplotlib.pyplot as plt
import os

SIZE = 3000
MAX = 512
MIN = 0

mean = 256 # Среднее значение (сигнал до 10 раз сильнее)
std_dev = 50 # Стандартное отклонение

for i in range(3):
    # Создание шума по Гауссу
    Gaussian_Noise = np.random.normal(mean, std_dev, (SIZE,SIZE))

    # Сохранение в папку text и images
    results_dir = "text"
    np.savetxt(os.path.join(results_dir,f'Gaussian_Noise{i+1}.txt'), Gaussian_Noise, fmt='%.0f')
    results_dir = "images"
    plt.imsave(os.path.join(results_dir,f'Gaussian_Noise{i+1}.png'), Gaussian_Noise, cmap='gray', vmin=MIN, vmax=MAX)

    # plt.imshow(Gaussian_Noise, cmap='gray', vmin=MIN, vmax=MAX)
    # plt.show()

print("Yep!")