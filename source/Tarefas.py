import csv

class Tarefas:
	file = ''
	index = 0
	# Método construtor
	def __init__(self, url_lista:str):
		# Criar arquivo da lista
		self.file = open('./listas/' + url_lista, "a", encoding = 'utf-8')
		# Criar objeto de gravação

	# Método de adicionar tarefa a lista
	def adicionar(self, titulo:str, data:str, categoria:str, pendente:bool):
		tarefa = []
		tarefa.append(titulo)
		tarefa.append(data)
		tarefa.append(categoria)
		if pendente == True:
			tarefa.append('Pendente')
		else:
			tarefa.append('Concluída')
		w = csv.writer(self.file)
		w.writerow(tarefa)
		self.index += 1
	
	def fechar(self):
		self.file.close()
		
# .strftime('%d/%m/%Y às %H:%M (UTC-3)')