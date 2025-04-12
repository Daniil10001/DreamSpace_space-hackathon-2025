import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Данные
data = [
    {'b': 0.040, 'l_over_b': 300, 'Re': 1630},
    {'b': 0.060, 'l_over_b': 200, 'Re': 1630},
    {'b': 0.060, 'l_over_b': 200, 'Re': 5500},
    {'b': 0.100, 'l_over_b': 120, 'Re': 5500},
    {'b': 0.187, 'l_over_b': 60, 'Re': 5500},
    {'b': 0.100, 'l_over_b': 120, 'Re': 9500},
    {'b': 0.120, 'l_over_b': 50, 'Re': 10000},
    {'b': 0.120, 'l_over_b': 25, 'Re': 10000},
    {'b': 0.187, 'l_over_b': 64, 'Re': 10000}
]

# Константы
dP = 1e10 # atm
rho = 1000.0  # плотность жидкости (кг/м³), примерное значение для воды
atm_to_pa = 101325.0  # 1 атм в Паскалях
inch_to_m = 0.0254  # дюймы в метры


# Функция для определения скорости из числа Рейнольдса
def get_velocity(Re, b):
    b_m = b * inch_to_m
    # Re = sqrt(dP * b^2 / (rho * v^2)) => v = sqrt(dP * b^2 / (rho * Re^2))
    v = np.sqrt((dP * atm_to_pa * b_m ** 2) / (rho * Re ** 2))
    return v


# Функция для расчета x/b в зависимости от угла alpha
def calculate_x_over_b(alpha_deg, v, b):
    alpha = np.deg2rad(alpha_deg)
    g = 9.81  # ускорение свободного падения (м/с²)

    # Время полета до падения на наклонную поверхность
    # Уравнение траектории: y = v*t - 0.5*g*t^2
    # Наклонная поверхность: y = tan(alpha) * x
    # Расстояние x = v * t
    # Подставляем x в уравнение наклонной поверхности:
    # v*t*tan(alpha) = v*t - 0.5*g*t^2 => t = 2*v*(1 - tan(alpha))/g
    # Но если alpha = 0, то t = 0 (что соответствует x = 0)
    # Для alpha > 0:
    if alpha_deg == 0:
        return 0.0
    else:
        t = (2 * v * (np.sin(alpha))) / (g * np.cos(alpha))
        x = v * t * np.cos(alpha)  # горизонтальная проекция
        x_surface = x / np.cos(alpha)  # расстояние вдоль наклонной поверхности
        x_over_b = x_surface / (b * inch_to_m)
        return x_over_b


# Углы alpha для построения графиков (от 0 до 90 градусов)
alpha_deg_range = np.linspace(0, 60, 100)

# Построение графиков для каждого случая
plt.figure(figsize=(12, 8))

for case in data:
    b = case['b']
    Re = case['Re']
    l_over_b = case['l_over_b']

    v = get_velocity(Re, b)
    x_over_b_values = [calculate_x_over_b(alpha_deg, v, b) for alpha_deg in alpha_deg_range]

    plt.plot(alpha_deg_range, x_over_b_values, label=f'b={b} inch, l/b={l_over_b}, Re={Re}')

plt.xlabel('Угол alpha (градусы)')
plt.ylabel('x/b')
plt.title('Зависимость x/b от угла alpha для разных случаев')
plt.legend()
plt.grid(True)
plt.show()