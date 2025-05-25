import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parâmetros baseados no sensor Delsys Trigno 
frequencia = 370.37  # Hz
dt = 1 / frequencia  # ≈ 0.0027 s
tempo_total = 2  # segundos de simulação
t = np.arange(0, tempo_total, dt)

# Simula aceleração no eixo y (padrão de corrida vertical)
# Exemplo: função com picos como em strides (passadas)
acc_y = 10 * np.sin(2 * np.pi * 2.5 * t) + np.random.normal(0, 0.5, size=len(t))
# 2.5 Hz ≈ cadência de corrida (150 passos/min)

# Cria o DataFrame
df = pd.DataFrame({'tempo': t, 'ay': acc_y})

# Salva o CSV
df.to_csv('aceleracao_simulada.csv', index=False)

# Visualiza o sinal
plt.plot(t, acc_y, color = 'purple')
plt.title('Aceleração simulada do sensor (eixo Y)')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s²)')
plt.grid(True)
plt.show()
