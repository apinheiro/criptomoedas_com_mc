# Cotações em Criptomoedas

## Objetivo

Este código fonte foi disponibilizado para fazer a cotação da criptomoeda conforme trabalho de Tratamento de Incertezas

## Obtendo a chave de acesso

A chave de acesso deve ser requisitada no site http://coinapi.io. 

Esta chave permite fazer até 100 consultas gratuitas por dia, o que é suficiente para o projeto da disciplina.

## Consumindo dados históriocos

Os dados históricos podem ser consumidos diretamente da API. O arquivo <code>get_cotacao_btc.py</code> mostra um exemplo do consumo histórico do Bitcoin cotado em dolar e organizado em tempos de 1 hora.

No meu script, estou pegando apenas o valor final, mas você pode alterar o código para pegar outras informações.

## Consumindo cotação atual.

Este código ainda não está pronto, mas será feito um script para que você possa pegar os valores da cotação atual de uma criptomoeda. No meu caso, como pego valores históricos, posso colocar para o código me retornar o valor das últimas X horas.

