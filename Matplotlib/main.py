import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,6,9,7]

plt.plot(x,y, label = 'Dados', linestyle='dashed',color='r', lw=3.0)

#Ajustar o gráfico
plt.axis(xmin=0, xmax=4, ymin=5,ymax=9)

#Nomeando eixos e titulo
plt.ylabel('Eixo Y')
plt.xlabel('Eixo x')
plt.title('Titulo ')

#Definindo intervalos que quero q mostrem no grafico
plt.xticks([0,2,4,6,8,10])
plt.yticks([1,5,10,15])

#Definindo legenda
plt.legend()

plt.show()

# plt.scatter(x,y)
# plt.show()
#
# plt.bar(x,y)
# plt.show()
