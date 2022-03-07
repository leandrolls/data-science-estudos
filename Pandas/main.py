import pandas as pd
from IPython.core.display_functions import display

#venda = {'data':['15/02/2021', '16/05/2021'],
#         'valor':[500,300],
#         'produto': ['feijao', 'arroz'],
#         'qtd':[50,40],
#         }

#vendas_df = pd.DataFrame(venda)

#Importar a partir de uma base de dados
vendas_df = pd.read_excel('Vendas.xlsx')

gerente_df = pd.read_csv('Gerentes.csv', sep=';')

# vendas_df = vendas_df.merge(gerente_df)
display (gerente_df)