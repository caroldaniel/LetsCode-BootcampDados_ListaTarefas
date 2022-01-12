import csv

class Tarefas:
	file_url = ''

	# Método construtor
	def __init__(self, url_lista:str):
		# Criar arquivo da lista
		self.file_url = url_lista
		with open(self.file_url, "w", encoding = 'utf-8') as file:
			w = csv.writer(file)
			w = w.writerows([['Título', 'Data', 'Categoria', 'Status']])

	# Método de adicionar tarefa a lista
	def adicionar(self, titulo:str, data:str, categoria:str, pendente:str) -> bool:
		with open(self.file_url, "r") as read_file:
			r = csv.reader(read_file)
			for row in r:
				if row[0] == titulo or row[1] == data:
					return False
		with open(self.file_url, "a", encoding = 'utf-8') as file:
			tarefa = []
			tarefa.append(titulo)
			tarefa.append(data)
			tarefa.append(categoria)
			tarefa.append(pendente)
			# Criar objeto de gravação
			a = csv.writer(file)
			a.writerows([tarefa])
			return True

	# Método de remover tarefa da lista
	def remover(self, titulo:str, data:str) -> bool:
		lista = []
		removido = False
		with open(self.file_url, "r") as read_file:
			r = csv.reader(read_file)
			for row in r:
				if row[0] != titulo or row[1] != data:
					lista.append(row)
				else:
					removido = True
		with open(self.file_url, "w", encoding = 'utf-8') as write_file:
			w = csv.writer(write_file)
			w.writerows(lista)
		return removido

	# Método de alterar status de determinada tarefa
	def alterar_status(self, titulo:str, data:str) -> bool:
		lista = []
		alterado = False
		with open(self.file_url, "r") as read_file:
			r = csv.reader(read_file)
			for row in r:
				if row[0] == titulo and row[1] == data:
					alterado = True
					new_row = row
					if new_row[3] == 'Pendente':
						new_row[3] = 'Completo'
					else:
						new_row[3] = 'Pendente'
					lista.append(new_row)
				else:
					lista.append(row)
		with open(self.file_url, "w", encoding = 'utf-8') as write_file:
			w = csv.writer(write_file)
			w.writerows(lista)
		return alterado
	
	def visualizar_status(self, status:str) -> list:
		lista = []
		with open(self.file_url, "r") as read_file:
			r = csv.reader(read_file)
			for row in r:
				if row[3] == status:
					lista.append(row)
		return lista

	def visualizar_data(self, data:str) -> list:
		lista = []
		with open(self.file_url, "r") as read_file:
			r = csv.reader(read_file)
			for row in r:
				if row[1] == data:
					lista.append(row)
		return lista
	
	def visualizar_todas(self) -> list:
		lista = []
		with open(self.file_url, "r") as read_file:
			r = csv.reader(read_file)
			for row in r:
				lista.append(row)
		return lista
		
# .strftime('%d/%m/%Y às %H:%M (UTC-3)')