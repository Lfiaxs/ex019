from random import choice
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O escolhido entre eles para apagar o quadro foi aluno(a) {} '.format(escolhido))

