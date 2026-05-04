# Calculadora em Python com CustomTkinter

Este é um projeto simples de calculadora desktop desenvolvido em Python, utilizando a biblioteca CustomTkinter para a interface gráfica.

O objetivo principal do projeto foi praticar conceitos fundamentais de programação, como:

- organização de código em arquivos separados;
- criação de classes;
- funções e métodos;
- tratamento de erros;
- manipulação de interface gráfica;
- lógica de operações matemáticas sequenciais.

## Funcionalidades

A calculadora permite realizar operações básicas:

- soma;
- subtração;
- multiplicação;
- divisão;
- apagar o último caractere;
- limpar a expressão;
- calcular expressões com mais de dois valores de forma sequencial.

Exemplo:

```text
10 + 5 + 2 = 17

Observação: nesta versão, as operações são calculadas da esquerda para a direita, sem prioridade matemática entre multiplicação/divisão e soma/subtração.

Tecnologias utilizadas
Python
CustomTkinter
Estrutura do projeto
calculadora-python-customtkinter/
│
├── app.py
├── calculadora.py
├── requirements.txt
└── README.md
calculadora.py

Arquivo responsável pela lógica das operações matemáticas.

app.py

Arquivo responsável pela interface gráfica e pela interação com o usuário.

Como executar
Clone o repositório:
git clone https://github.com/seu-usuario/calculadora-python-customtkinter.git
Acesse a pasta do projeto:
cd calculadora-python-customtkinter
Instale as dependências:
pip install -r requirements.txt
Execute o projeto:
python app.py
Sobre o desenvolvimento

Este projeto foi desenvolvido como exercício de prática em Python e interface gráfica. Durante o desenvolvimento, consultei materiais de apoio e utilizei IA como ferramenta auxiliar para tirar dúvidas, revisar trechos específicos do código e melhorar a organização da estrutura do projeto.

A lógica principal foi estudada, testada e ajustada durante o processo, com foco em compreender o funcionamento do código e evoluir a aplicação de forma prática.

Possíveis melhorias futuras

Algumas melhorias que podem ser implementadas em versões futuras:

respeitar a prioridade matemática das operações;
adicionar suporte a parênteses;
adicionar potência e raiz quadrada;
criar histórico de cálculos;
melhorar o design da interface;
permitir uso pelo teclado;
adicionar testes automatizados.
Status

Projeto em desenvolvimento.
