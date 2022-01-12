from source.Tarefas import Tarefas
from datetime import date

#Inicio SetUp
tarefas = Tarefas('tarefas.csv')

# Funções de input
def input_titulo_categoria() -> str:
	titulo = input().strip().title()
	return titulo

def input_data() -> str:
	dia = input('Dia (DD): ')
	while dia.isnumeric() == False or len(dia) != 2 or int(dia) <= 0 or int(dia) > 31:
		dia = input('---Dia inválido!\nDia (DD): ')
	mes = input('Mês (MM): ')
	while mes.isnumeric() == False or len(mes) != 2 or int(mes) <= 0 or int(mes) > 12:
		mes = input('---Mês inválido!\nMês (MM): ')
	ano = input('Ano (AAAA): ')
	while ano.isnumeric() == False or len(ano) != 4 or int(ano) <= 1900 or int(ano) > 2500:
		ano = input('---Ano inválido!\nAno (AAAA): ')
	return (f'{ano}/{mes}/{dia}')

# Funções do menu
## Criar nova tarefa
def nova_tarefa():
	print('Digite o título da tarefa: ', end='')
	titulo = input_titulo_categoria()
	print('Digite a data para conclusão da tarefa: ')
	data = input_data()
	print('Digite a categoria da tarefa: ', end='')
	categoria = input_titulo_categoria()
	pendente = 'Pendente'
	ok = tarefas.adicionar(titulo, data, categoria, pendente)
	if ok == False:
		print('Tarefa de mesmo nome e data já existe na lista de tarefas!')
    
## Visualizar tarefas por data
def visualizar():
	print(f'''Deseja visualizar tarefas de Hoje, pesquisar por Data ou mostrar Todas?
	Se [H], a pesquisa retornará as tarefas do dia de hoje;
	Se [D], a pesquisa retornará as tarefas da data especificada;
	Se [T], a pesquisa retornará todas as tarefas da lista.
	''')
	opcao = input('(H/D/T)\n').strip().upper()
	while opcao != 'H' and opcao != 'D' and opcao != 'T':
		opcao = input('Opção inválida!\n(H/D/T)').strip().upper()
	if opcao == 'H':
		hoje = date.today()
		data = f'{hoje.year:04.0f}/{hoje.month:02.0f}/{hoje.day:02.0f}'
		lista = tarefas.visualizar_data(data)
		print(lista)
	elif opcao == 'D':
		data = input_data()
		lista = tarefas.visualizar_data(data)
		print(lista)
	else:
		lista = tarefas.visualizar_todas()
		print(lista)

#alterar o status baseado no titulo
def alterar_status():
	print('Digite o título da tarefa: ', end='')
	titulo = input_titulo_categoria()
	print('Digite a data para conclusão da tarefa: ')
	data = input_data()
	ok = tarefas.alterar_status(titulo, data)
	if ok == False:
		print('Tarefa não encontrada!')

#remover uma tarefa das lista baseada no titulo
def remover_tarefa():
	print('Digite o título da tarefa: ', end='')
	titulo = input_titulo_categoria()
	print('Digite a data para conclusão da tarefa: ')
	data = input_data()
	ok = tarefas.remover(titulo, data)
	if ok == False:
		print('Tarefa não encontrada!')
                   
# Main Menu
def main():
	while True:
		comando = input(f'''\n--- DIGITE UMA OPÇÃO PARA PROSSEGUIR
[1] Adicionar tarefa
[2] Alterar status da tarefa
[3] Remover tarefa
[4] Visualizar todas as tarefas 
[5] Fechar programa

OPÇÃO: ''')
		if comando == '1':
			print('ADICIONAR TAREFA\n')
			nova_tarefa()
		elif comando =='2':
			print('ALTERAR STATUS DA TAREFA\n')
			alterar_status()
		elif comando =='3':
			print('REMOVER TAREFA\n')
			remover_tarefa()
		elif comando =='4':
			print('VISUALIZAR LISTA\n')
			visualizar()
		elif comando =='5':
			print('FECHAR PROGRAMA\n')
			break
		else:
			print('OPÇÃO INVÁLIDA\n')

# Execução do programa
main()