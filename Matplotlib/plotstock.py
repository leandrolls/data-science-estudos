import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display

cotacao_df = pd.read_csv("indexData.csv")

cotacao_df1 = cotacao_df[['Index','Date','Close']]


dfremove = cotacao_df1.loc[(cotacao_df1['Index']!='NYA')]
cotacao_dffinal = cotacao_df1.drop(dfremove.index)

cotacao_dffinal = cotacao_dffinal[13900:]

plt.plot(cotacao_dffinal['Date'],cotacao_dffinal['Close'])
plt.show()