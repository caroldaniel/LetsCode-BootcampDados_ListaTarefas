from source.Tarefas import Tarefas
import csv

#Inicio SetUp
# Transformar o csv em uma lista
arquivo = open('tarefas.csv')
with open('tarefas.csv') as arquivo:
  tabela = csv.reader(arquivo, delimiter=',', lineterminator='\n')

  conteudo = list(tabela)
#Remover todas as listas vazia
[conteudo.remove(i) for i in conteudo if i==[]]
[conteudo.remove(i) for i in conteudo if i==[]]
print(conteudo)
#lista com tudo
lista = conteudo
#Fim SetUp

#criar_nova_tarefa
def nova_tarefa():
    titulo = input('Digite o título para a tarefa: ')
    data = input('Digite a data que ela deva ser concluída (AAAA/MM/DD): ')
    categoria = input('Digite a categoria da tarefa: ')
    pendente = 'Pendente'
    nova_tarefa = [titulo, data, categoria, pendente]
    lista.append(nova_tarefa)

#visualizar as tarefas de um dia
def visualizar():
    data = input('Qual a data: ')
    for i in lista:
        if data in i:
            print(i)

#alterar o status baseado no titulo
def alterar_status():
    titulo = input('Qual o titulo da tarefa: ')
    for i in lista:
        if titulo in i:
            if i[3] == 'Pendente':
                i[3] = 'Concluído'
            else:
                i[3] = 'Pendente'

#remover uma tarefa das lista baseada no titulo
def remover_tarefa():
    titulo = input('Qual o titulo: ')
    for i in lista:
        if titulo in i:
            lista.remove(i)
        
def fechar_programa():
	lista_Tarefas = Tarefas('tarefas.csv')
	for i in range(len(lista)):
		titulo =  lista[i][0]
		data = lista[i][1]
		categoria = lista[i][2]
		status = lista[i][3]
		lista_Tarefas.adicionar(titulo,data,categoria,status)
	lista_Tarefas.fechar()
           
#MainMenu
comando = 'False'
while comando!= '5':
    print('\n1. Adicionar tarefa \n2. Alterar status da Tarefa \n3. Remover tarefa \n4. Visualizar tarefas \n5. Fechar \n')
    comando = input('Escolha uma opção: ')
    if comando == '1':
        print('Adicionar')
        nova_tarefa()
    elif comando =='2':
        print('Alterar')
        alterar_status()
    elif comando =='3':
        print('Remover')
        remover_tarefa()
    elif comando =='4':
        print('Visualizar')
        visualizar()
    elif comando =='5':
        print('Fechar')
        fechar_programa()
    else:
        print('Escolhar uma opção válida! [1 2 3 4 5]')