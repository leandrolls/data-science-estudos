# Definir valores para os exemplos
import matplotlib.pyplot as plt

valoresx = [0, 12, 35, 41, 10]
valoresy = [65, 12, 16, 92, 43]

# Criando uma figura
figura = plt.figure(figsize=(20, 3))
figura.suptitle("Titulo Figura")

# Definindo posicionamento dos gráficos
# Definido por 1 linha, 3 colunas e o gráfico que será plotado ficara na posicao 1
figura.add_subplot(131)
# Plotando o gráfico
plt.plot(valoresx, valoresy, label="Um dado qualquer")
plt.legend()
plt.title("Gráfico 1")

figura.add_subplot(132)
plt.scatter(valoresx, valoresy)
plt.title("Gráfico 2")

figura.add_subplot(133)
plt.bar(valoresx, valoresy)
plt.title("Gráfico 3")

plt.savefig('grafico.png', dpi =100)
plt.show(figura)

