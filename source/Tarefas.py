import csv

class Tarefas:
	file = ''
	index = 0
	# Método construtor
	def __init__(self, url_lista:str):
		# Criar arquivo da lista
		self.file = open( url_lista, "w", encoding = 'utf-8')
		# Criar objeto de gravação

	# Método de adicionar tarefa a lista
	def adicionar(self, titulo:str, data:str, categoria:str, pendente:str):
		tarefa = []
		tarefa.append(titulo)
		tarefa.append(data)
		tarefa.append(categoria)
		tarefa.append(pendente)
		w = csv.writer(self.file)
		w.writerow(tarefa)
		self.index += 1
	
	def fechar(self):
		self.file.close()
		
# .strftime('%d/%m/%Y às %H:%M (UTC-3)')