import requests
import pandas as pd
from datetime import datetime
import time

while True:

    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_bitcon = requisicao_dic["BTCBRL"]["bid"]

    cotacoes = pd.read_excel("Cotações.xlsx")
    cotacoes.loc["0","Cotacao"] = cotacao_dolar
    cotacoes.loc["1","Cotacao"] = cotacao_euro
    cotacoes.loc["2","Cotacao"] = cotacao_bitcon
    cotacoes.loc["0","Data Última Atualização"] = datetime.now()

    cotacoes.to_excel("Cotações.xlsx", index=False)
    print(f"Cotacao atualizada {datetime.now()}")

    time.sleep(120)