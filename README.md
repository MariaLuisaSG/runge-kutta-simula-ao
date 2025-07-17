# Simulação de Movimento Humano com RK4 e Dados de Aceleração
Este projeto implementa o método de Runge-Kutta de quarta ordem (RK4) em Python para estimar a posição vertical de um indivíduo durante a corrida, a partir de sinais de aceleração.
A aceleração pode ser fornecida por sensores reais (como o Delsys Trigno, que foi o mais usado) ou gerada sinteticamente com características semelhantes a um padrão de passadas.
O sinal simulado é construído com uma onda senoidal de 2,5 Hz (aproximadamente 150 passos por minuto), amostrada a 370,37 Hz, (frequência típica do sensor Delsys Trigno, e com ruído gaussiano adicionado para maior realismo). O sinal é salvo em um arquivo CSV com colunas de tempo e aceleração no eixo Y.
Com esses dados, uma função de interpolação linear é criada para fornecer aceleração contínua ao longo do tempo. 
O sistema de equações diferenciais que modela o movimento (\( dx/dt = v \), \( dv/dt = a(t) \)) é então resolvido numericamente com RK4, permitindo reconstruir a trajetória da posição ao longo do tempo com base apenas nos dados de aceleração.

O projeto contém dois scripts principais:  
1- Gerar_dados.py — gera e plota o sinal de aceleração simulado  
2- Simular_posicao.py — realiza a simulação de posição com RK4 e plota o resultado

As bibliotecas utilizadas são: numpy, pandas, scipy e matplotlib.
Este projeto pode ser útil em estudos de biomecânica, validação de modelos de movimento humano, ou aplicações com sensores inerciais embarcados.

Autora: Maria Luisa Saraiva   
Licença: MIT
