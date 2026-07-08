# Calculadora
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

