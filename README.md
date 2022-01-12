# TodoList: Projeto de POO

Neste projeto você vai desenvolver uma lista de tarefas utilizando o Python. À princípio, sua lista de tarefas deverá funcionar no console e você deve dispor de algumas opções para o usuário, as quais são elencadas adiante.

## Requisitos Funcionais

A aplicação deve dispor de um menu com as seguintes opções para o usuário:

1. **Adicionar tarefa:** Ao solicitar essa opção o usuário poderá criar uma nova tarefa. Para isso, ele deverá informar o título, a data de realização e a categoria da tarefa. Você deverá salvar essas três informações (além de uma informação de que o status da tarefa está como *Pendente*) dentro de um arquivo CSV (`tarefas.csv`, por exemplo).
2. **Alterar status da Tarefa:** Ao solicitar essa opção o usuário poderá alterar o status de uma determinada tarefa, ou seja, se a tarefa está como *Pendente*, ficará como *Concluída*, e vice-versa. Para isso, ele deve informar o título da tarefa. Você deverá alterar a coluna de *Status* do arquivo, referente à tarefa que possui o título informado pelo usuário.
3. **Remover tarefa:** Ao solicitar essa opção o usuário poderá escolher uma tarefa para que essa seja removida. Para isso, ele deve informar o título da tarefa. Você deve remover a linha do arquivo que contém a tarefa cujo título foi informado pelo usuário.
4. **Visualizar tarefas:** Ao solicitar essa opção o usuário poderá escolher um dia específico para ver as tarefas agendadas para ele. Para isso, após escolher essa opção, o usuário precisa informar uma data. Você deve procurar pelas atividades que estão programadas para aquele dia específico (dentro do arquivo csv), e exibir todas elas.
5. **Fechar:** Ao solicitar essa opção o programa deverá ser encerrado.

## Instruções do Projeto

- O projeto deve ser realizado em grupo, sendo cada um composto por 2 integrantes.
- O projeto deve ser desenvolvido utilizando o Git, e os commits devem ser realizados por ambos os integrantes da equipe. Lembrando que isso ficará guardado no histórico de commits do projeto.
- **O projeto deve ser realizado com a utilização do conceito de Orientação a Objetos.** Ou seja, você deve pensar na lista de tarefas como uma classe que possui atributos e métodos.
- Embora a estrutura do projeto deva ter os requisitos funcionais citados na seção anterior, sinta-se à vontade para alterar ou até acrescentar outras features. Por exemplo:
    - Você pode querer criar um submódulo com funções que executem algo que você costuma fazer com mais frequência.
    - Você pode adicionar mais opções para o usuário, como editar uma tarefa.
    - Você pode permitir que, no momento da criação de uma tarefa, o usuário possa digitar a data como sendo *hoje* ou *amanhã*, além do formato convencional (`dd/mm/aaaa`).
    - Você pode remover ou alterar o status de uma tafera com base no título e, também, na data (caso haja tarefas com o mesmo título); dessa forma, você evita remover tarefas que possuem o mesmo título.

## **Dicas**

### **1. Como posso obter as tarefas de hoje para exibi-las?**

Para isso, sugiro que você utilize o módulo `datetime` que vimos nas nossas aulas. Observe que, dentro desse módulo existe um submódulo chamado `date`, o qual possui um método chamado `today`. Veja o exemplo abaixo:

```python
import datetime

hoje = datetime.date.today() # Obtendo a data de hoje

dia = hoje.day # obtendo o dia
mes = hoje.month # obtendo o mês
ano = hoje.year # obtendo o ano
```

Com o dia, mês e ano referentes ao dia de hoje, você consegue comparar com as datas que você salva no arquivo csv, não é mesmo? Lembrando que essas datas estão no formato dd/mm/aaaa.

> **OBS.: As variáveis `dia`, `mes` e `ano` são do tipo `int`.**
> 

### **2. Qual comando eu poderia utilizar no Python para limpar o console?**

Para isso, você deve utilizar um comando do sistema, o que é possível de ser feito por meio do módulo `os` do Python. Nesse módulo, existe uma função chamada `system` que te permite utilizar comandos do sistemas (comandos que você utilizaria no cmd, prompt de comando ou Terminal). Sendo assim, veja o exemplo abaixo:

```python
import os

# o comando abaixo vai limpar o seu console, caso você esteja utilizando o Windows
os.system('cls')

# o comando abaixo vai limpar o seu console, caso você esteja utilizando o Linux/Mac
os.system('clear')
```

### **3. Como eu posso fazer para "congelar" a execução do meu programa por um tempo específico?**

Você pode fazer isso utilizando a função `sleep` do módulo `time`. Esse módulo já vem instalado com o Python, portanto, basta você fazer a importação desse módulo ou apenas da função `sleep` (como no exemplo abaixo).

```python
from time import sleep

sleep(3)

print('Essa mensagem só aparece após 3 segundos...')
```

Observando o exemplo acima, você pode notar que a função sleep deve receber um parâmetro, que é o tempo em segundos que o programar irá "dormir", ou seja, "segurar" o seu fluxo de execução. Portanto, o `print` que vem logo abaixo da função `sleep` será executado apenas 3 segundos após a chamada dessa função `sleep`.

### **4. Como posso alterar a cor do texto no console?**

Uma solução ótima para isso seria a biblioteca `rich`. Caso tenha interesse em conhecer essa biblioteca, pode dar uma conferida na [documentação](https://rich.readthedocs.io/en/stable/introduction.html).

Você pode instalar ela com o `pip install rich`. Abaixo eu te dou um exemplo de como utilizar essa biblioteca:

```python
from rich import print

print('[green]Essa mensagem está na cor verde![/]')
```

### 5. Você pode utilizar um “input” mais poderoso

Caso tenha interesse em utilizar um biblioteca para fazer leitura de dados de uma forma mais inteligente/customizada, você pode optar também pela biblioteca `rich`. Para isso, consulte a seção [Prompt](https://rich.readthedocs.io/en/stable/prompt.html) da documentação.
