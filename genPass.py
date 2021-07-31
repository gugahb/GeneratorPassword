#Criando meu próprio gerador de senhas em Python

import random

#aqui coloque os caracteres minusculos, caso não queira algum só remover
min = 'abcdefghijklmnopqrstuvwxyz'
#aqui coloque os caracteres MAIUSCULOS, caso não queira algum só remover
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#aqui coloque os números caso não queira algum só remover
num = '0123456789'
#aqui coloque os símbolos caso não queira algum só remover
sybs = '[]{}()*#;/,-_%'

#qual tamanho da senha que você quer?
qnt = input('Digite qual tamanho da senha: ')
qntInt = int(qnt)
length = qntInt

#fazendo senha com todos
all = min + max + num + sybs
passwordAll = "".join(random.sample(all,length))

#só maiúsculas e números
MAXnum = max + num
passwordMAXnum = "".join(random.sample(MAXnum,length))

#só minusculas e maiúsculas
MAXmin = max + min
passwordMAXmin = "".join(random.sample(MAXmin,length))

# pronto, basta executar o seu código
print ('passwordAll = ' + passwordAll) 
print ('passwordMAXnum = ' + passwordMAXnum) 
print ('passwordMAXmin = ' + passwordMAXmin)

#Crie a sua combinação como quiser