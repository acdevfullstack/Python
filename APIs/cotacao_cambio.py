# API - Cotação de Moedas estrangeiras e Cryptos
import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_libra = requisicao_dic["GBPBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizada: {datetime.now()}\nDolar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nLibra: R${cotacao_libra}\nBTC: R${cotacao_btc}")


