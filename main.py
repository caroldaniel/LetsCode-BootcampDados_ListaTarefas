from source.Tarefas import Tarefas

lista = Tarefas('tarefas.csv')

for i in range(2):
	titulo = input('Digite o título para a tarefa: ')
	data = input('Digite a data que ela deva ser concluída (AAAA/MM/DD): ')
	categoria = input('Digite a categoria da tarefa: ')
	pendente = True
	lista.adicionar(titulo, data, categoria, pendente)

lista.fechar()