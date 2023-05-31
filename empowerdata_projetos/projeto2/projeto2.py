# Projeto 2 - Automação de tarefas
"""
Passo a passo do problema
    1 - Buscar dados das ações automaticamente
    2 - Realizar as análises solicitadas pelo gestor (cotação maxima, minima e atual)
    3 - Enviar automaticamente o e-mail com o resultado da análise
"""

# Passo 1

import yfinance as yf  # Extrai dados de ações do Yahoo Finanças

ticker = input('Digite o código da ação: ') # Armazena o ticker da ação solicitada

dados = yf.Ticker(ticker).history('6mo') # Aqui é solicitado seu histórico dos últimos 6 meses
fechamento = dados.Close # Aqui pegamos os dados da coluna de fechamento (Close) e armazenamos em uma variável

# print(fechamento.plot()) # Exibe o gráfico, não está funcionando no vscode procurando uma solução

# Passo 2

maxima = round(fechamento.max(), 2) # Retorna cotação maxima
minima = round(fechamento.min(), 2) # Retorna cotação minima
atual = round(fechamento[-1], 2) # Retorna cotação atual passando o indice negativo para retornar a ultima linha

# Passo 3



