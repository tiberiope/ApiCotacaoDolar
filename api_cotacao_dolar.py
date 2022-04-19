import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(cotacao)
print('\n')

cotacao = cotacao.json()
print(cotacao)
print('\n')

inf_dolar = cotacao['USDBRL']
print(inf_dolar)
print('\n')

cotacao_dolar = cotacao["USDBRL"]["bid"]
print(cotacao_dolar)