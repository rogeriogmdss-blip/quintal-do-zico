# Projeto: Quintal do Zico — Análise de vendas
# Tecnologias: Python, Pandas e Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path("dados/vendas_anonimizadas.csv")
OUT = Path("graficos")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(BASE, parse_dates=["Data"])

# 1. Conferência inicial
print("Registros:", len(df))
print("Quentinhas:", int(df["Quantidade"].sum()))
print("Faturamento: R$", round(df["Total"].sum(), 2))

# 2. Conferência quantidade x valor unitário
df["Total_calculado"] = df["Quantidade"] * df["Valor unitário"]
df["Divergencia"] = (df["Total"] - df["Total_calculado"]).abs() > 0.01
print("Possíveis divergências:", int(df["Divergencia"].sum()))

# 3. Análise por dia
por_dia = (
    df.groupby("Data")
      .agg(Pedidos=("Data", "size"),
           Quentinhas=("Quantidade", "sum"),
           Faturamento=("Total", "sum"))
      .reset_index()
)

# 4. Análise por prato
por_prato = (
    df.groupby("Prato")
      .agg(Quentinhas=("Quantidade", "sum"),
           Faturamento=("Total", "sum"))
      .reset_index()
      .sort_values("Quentinhas", ascending=False)
)

# 5. Análise por canal
por_canal = (
    df.groupby("Canal")
      .agg(Pedidos=("Data", "size"),
           Quentinhas=("Quantidade", "sum"),
           Faturamento=("Total", "sum"))
      .reset_index()
      .sort_values("Quentinhas", ascending=False)
)

# 6. Análise por pagamento
por_pagamento = (
    df.groupby("Pagamento")
      .agg(Pedidos=("Data", "size"),
           Faturamento=("Total", "sum"))
      .reset_index()
      .sort_values("Faturamento", ascending=False)
)

# 7. Gráfico: quentinhas por dia
plt.figure(figsize=(8, 4.5))
plt.bar(por_dia["Data"].dt.strftime("%d/%m"), por_dia["Quentinhas"])
plt.title("Quentinhas registradas por dia")
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig(OUT / "01_quentinhas_por_dia.png")
plt.close()

# 8. Gráfico: faturamento por dia
plt.figure(figsize=(8, 4.5))
plt.bar(por_dia["Data"].dt.strftime("%d/%m"), por_dia["Faturamento"])
plt.title("Faturamento registrado por dia")
plt.xlabel("Data")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.savefig(OUT / "02_faturamento_por_dia.png")
plt.close()

# 9. Gráfico: quentinhas por prato
plt.figure(figsize=(9, 5))
plt.barh(por_prato["Prato"], por_prato["Quentinhas"])
plt.gca().invert_yaxis()
plt.title("Quentinhas registradas por prato")
plt.xlabel("Quantidade")
plt.ylabel("Prato")
plt.tight_layout()
plt.savefig(OUT / "03_quentinhas_por_prato.png")
plt.close()

# 10. Gráfico: quentinhas por canal
plt.figure(figsize=(8, 4.5))
plt.bar(por_canal["Canal"], por_canal["Quentinhas"])
plt.title("Quentinhas registradas por canal")
plt.xlabel("Canal")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig(OUT / "04_quentinhas_por_canal.png")
plt.close()

# 11. Gráfico: faturamento por pagamento
plt.figure(figsize=(8, 4.5))
plt.bar(por_pagamento["Pagamento"], por_pagamento["Faturamento"])
plt.title("Faturamento por forma de pagamento")
plt.xlabel("Pagamento")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.savefig(OUT / "05_faturamento_por_pagamento.png")
plt.close()
