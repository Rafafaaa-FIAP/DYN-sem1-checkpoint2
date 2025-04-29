
from node import Node
from linkedList import LinkedList

'''
Integrantes
RM553521 - Rafael Cristofali
RM553377 - Enzo Rodrigues
RM553384 - Maria Julia
RM553266 - Hugo Santos
'''

'''
Exercício 1 
Escreva uma função recursiva chamada ‘contar_digitos_pares’que receba
um número inteiro positivo e retorne a quantidade de dígitos pares no número.
Exemplo de Entrada e Saída:
  Entrada: 2486
  Saída: 4 (todos os dígitos são pares: 2, 4, 8, 6)
  Entrada: 1357
  Saída: 0 (nenhum dígito é par)
  Entrada: 1234
  Saída: 2 (dígitos pares: 2, 4)
'''
# def contar_digitos_pares(digit):
#     if (digit == 0):
#         return 0
#
#     lastDigit = digit % 10
#
#     if (lastDigit % 2 == 0):
#         return 1 + contar_digitos_pares(digit // 10)
#     else:
#         return contar_digitos_pares(digit // 10)
#
# print(contar_digitos_pares(2486))
# print(contar_digitos_pares(1357))
# print(contar_digitos_pares(1234))



'''
Exercício 2
Crie uma função chamada find_max na lista ligada. Essa função deve retornar qual o maior elemento armazenado na lista. 
'''
# def find_max(listaLigada):
#     current = listaLigada.head
#
#     max = 0
#
#     while (current):
#         if (current.data > max):
#             max = current.data
#         current = current.next
#
#     return max
#
#
# lista = LinkedList()
# lista.insert_at_end(10)
# lista.insert_at_end(30)
# lista.insert_at_end(50)
# print(find_max(lista))

'''
Exercício 3
Considerando as listas ligadas, crie uma função chamada insert_after, que insere um novo dado após um valor específico. Essa função deve receber um dado a ser inserido e um dado a ser buscado. Quando ela encontrar o dado buscado deverá inserir o dado a ser inserido após esse dado. Se o dado de busca não for encontrado na lista, o novo dado é inserido no final da lista.
'''
# def insert_after(listaLigada, dataToFind, insertData):
#     current = listaLigada.head
#     while current:
#         if current.data == dataToFind:
#             new_node = Node(insertData)
#             new_node.next = current.next
#             current.next = new_node
#         current = current.next
#     return listaLigada
#
# lista = LinkedList()
# lista.insert_at_end(1)
# lista.insert_at_end(2)
# lista.insert_at_end(3)
# lista.insert_at_end(4)
# lista.insert_at_end(5)
# print(insert_after(lista, 2, 0).display())
