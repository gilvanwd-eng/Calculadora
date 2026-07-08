# Calculadora.sh
O usuario abre a calculadora com dois cliques no arquivo caculadora.sh
digita um numero preciona tecla enter
digita o segundo numero preciona tecla enter
e visualiza o resultado da soma.

# Comandos Utilizados

Linha 1 - #!/bin/bash - Identifica que deve-se usar interpretador Bash para rodar as demais linhas
Linha 3 - echo -  Exibe mensagem na tela.
Linha 4 - read n1 - Script pausa a execução. Oterminal fica piscando aguardando ser digitado o segundo numero, esse valor é guardao na variavel n1.
Linha 6 - echo - exibe segunda mensagem na tela.
Linha 7 - Script pausa novamente, aguardando que o usuario digite o segundo valor n2.
Linha 9 - echo - o Bash identifica a estrutura $((...)), que serve para operações aritiméticas.
Resumindo ele busca os valores guardados nas variaveis n1 e n2 e faz a soma entregando assim o resultado.

# Calculadora.py
O script realiza a captura, validação e soma de dois numeros de forma segura trando possiveis erros de digitação.

# Comandos Utilizados
função while true para criar um laço de repetição infinito
try - tenta receber a entrada do usuario (input) transforma em numero decimal (float) retorna valor (return) sai da função e quebra o laço automaticamente.
Caso o usuario digito letras por exemplo exibira uma mensagem de "entrada invalida", fazendo o usuario digitar novamente
função main - chama a ler_numero duas vezes para guardar os valores n1 e n2
entrega o resultado.
soma.is_integer() verifica se o numero decimal termina em 0.
caso termine int(soma) transforma em apenas um numero.
print exibe o resultado na tela.
