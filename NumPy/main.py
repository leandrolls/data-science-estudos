import numpy as np
from numpy.random import default_rng

## Array de uma dimensao
a = np.array([1,2,3,4,5,6])
print (a)

## Array de duas dimensões
b = np.array([[1,2,3,4,5,6],[11,12,13,14,15,16]])
print (b)

## Array composto apenas de zeros
arrayDeZeros = np.zeros(shape=(5,3,6))
## No argumento 'shape' definimos as dimensões do array.
# Ou seja, em uma dimensão temos um tamanho 5, na outra 3 e na outra 6.
print(arrayDeZeros)

## Array composto apenas de 1
arrayDeUm = np.ones(2)
print(arrayDeUm)

## Array criado com mais informações
arrayArrange = np.arange(50,200,30)
#Aqui informamos que o nosso array começará de 50 irá de 30 em 30 até chegar em 200 que é o limite.
print(arrayArrange)

#Como eu descubro o tamanho de um array ?
print(arrayDeZeros.shape)

#Como descubro quantos dados tem em um array ?
print(arrayDeZeros.size)

#Como eu descubro quantas dimensões um array tem ?
print(arrayDeZeros.ndim)

#Como transformar um vetor de uma dimensão para uma matrix de 2 dimensões
#Criando o vetor de uma dimensão
a = np.array([1,2,3])
#Criando uma nova dimensão no vetor a
a2 = a[np.newaxis,:]

#Como faço para concatenar dois vetores (vetor c e vetor d)
c = np.array([1,2,3])
d = np.array([4,5,6])

e = np.concatenate((a,b))
# ou
f = np.concatenate((b,a))

#---------------------------------

a = np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])
print(a)
#Consultando itens de uma array:
MAIOR_8 = a[a>8]
print(MAIOR_8)
#É possível colocar condições específicas e das mais variadas para consulta de array.

#---------------------------------
#Gerando números aleatórios
rng = default_rng()
aleatorio = rng.integers(10, size=(2,4))
#nos argumentos foram passados que quero gerar valores aleatorios menores que 10 e que seja um vetor de duas dimensoes e de tamanho 4)
print (aleatorio)

#Diferença entre Arrays e Listas
# É mais rápido usar arrays para manipulação de quantiaade dados maiores
#Um array só permite que exista um tipo de dado na array, seja interios, char, etc.
#Listas não permitem operações matemáticas entre si


