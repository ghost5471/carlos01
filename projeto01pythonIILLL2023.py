import os
import pandas as pd
import plotly.express as px
import win32com.client as win32

lista_arquivo = os.listdir("C:/Users/NT-STC-01/projeto/Vendas/")

print(lista_arquivo)

tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
  if "Vendas" in arquivo:
    tabela = pd.read_csv(f"C:/Users/NT-STC-01/projeto/Vendas/{arquivo}")
    tabela_total = pd.concat([tabela_total,tabela])
    print(tabela_total)

print(tabela_total)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by = "Quantidade Vendida", ascending = False)
print(tabela_produtos)


tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]


tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by = "Faturamento", ascending = False)
print(tabela_faturamento)


tabela_loja = tabela_total.groupby("Loja").sum()
tabela_loja = tabela_loja[["Faturamento"]]
print(tabela_loja)



grafico = px.bar(tabela_loja, x = tabela_loja.index, y = "Faturamento")
grafico.show()


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'vclaudinogomes@gmail.com'
mail.Subject = 'relatório'
mail.HTMLBody = f'''
produtos

faturamentos
'''
mail.sned()