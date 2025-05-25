import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

#  CARREGANDO OS DADOS DO SENSOR
df = pd.read_csv('aceleracao_simulada.csv')  
sensor_times = df['tempo'].values     # Tempo em segundos
sensor_acc = df['ay'].values          # Aceleração vertical (eixo Y)

# CRIA A FUNÇÃO DE INTERPOLAÇÃO LINEAR
accel_interp = interp1d(sensor_times, sensor_acc, kind='linear', fill_value='extrapolate')

# NOVA FUNÇÃO DE ACELERAÇÃO BASEADA NOS DADOS DO SENSOR
def acceleration(t):
    return accel_interp(t)

#  SISTEMA DE EDOs: posição e velocidade
def f(t, Y):
    x, v = Y
    dxdt = v
    dvdt = acceleration(t)
    return np.array([dxdt, dvdt])

# MÉTODO DE RUNGE-KUTTA 4
def runge_kutta_4_system(f, t0, Y0, h, n):
    t_vals = [t0]
    x_vals = [Y0[0]]
    v_vals = [Y0[1]]

    t = t0
    Y = np.array(Y0)

    for i in range(n):
        k1 = h * f(t, Y)
        k2 = h * f(t + h/2, Y + k1/2)
        k3 = h * f(t + h/2, Y + k2/2)
        k4 = h * f(t + h, Y + k3)

        Y = Y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h

        t_vals.append(t)
        x_vals.append(Y[0])
        v_vals.append(Y[1])

    return t_vals, x_vals, v_vals

# PARÂMETROS BASEADOS NO ARQUIVO DE DADOS

t0 = sensor_times[0]
x0 = 0
v0 = 0
h = 0.0027  # frequência do sensor Delsys Trigno (370,37 Hz)
n = int((sensor_times[-1] - sensor_times[0]) / h)

# CHAMADA DO RK
t_vals, x_vals, v_vals = runge_kutta_4_system(f, t0, [x0, v0], h, n)

#  CONDIÇÕES INICIAIS
x0 = 0      # posição inicial
v0 = 0      # velocidade inicial (pode ajustar)

#  EXECUTA O MÉTODO RK4
t_vals, x_vals, v_vals = runge_kutta_4_system(f, t0, [x0, v0], h, n)

#  PLOT DO RESULTADO: POSIÇÃO SIMULADA
plt.plot(t_vals, x_vals, label='Posição (x) integrada da aceleração', color='purple')
plt.title('Simulação de posição com Runge-Kutta e dados do sensor')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição estimada (m)')
plt.grid(True)
plt.legend()
plt.show()
