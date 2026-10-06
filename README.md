# Quintal do Zico — Análise de Dados de Vendas

## Sobre o projeto

Projeto acadêmico e prático desenvolvido no curso de CST em Ciência de Dados, utilizando registros de vendas de um pequeno negócio familiar do segmento de alimentação.

O objetivo foi transformar registros manuais em uma base estruturada, realizar tratamento e análise exploratória dos dados e gerar informações que pudessem apoiar decisões relacionadas à produção, vendas e organização do negócio.

## Problema

Os pedidos eram registrados predominantemente em caderno e também recebidos por WhatsApp e telefone. Esse formato funcionava para a rotina diária, mas dificultava consultas, comparações e análises históricas.

## Solução desenvolvida

- Organização dos registros em uma base estruturada;
- Padronização dos principais campos;
- Conferência de quantidade × valor unitário;
- Identificação de registros especiais, como doações;
- Análise por dia, prato, canal e forma de pagamento;
- Criação de gráficos para facilitar a interpretação dos resultados.

## Principais resultados

No período analisado foram registrados:

- 97 pedidos;
- 197 quentinhas;
- R$ 5.015,00 em valores registrados;
- 6 registros identificados como doação;
- 4 possíveis divergências entre quantidade × valor unitário × total informado.

O prato com maior quantidade registrada foi a feijoada, com 80 quentinhas. O dia com maior movimento na base foi 24/09/2026, com 109 quentinhas e R$ 2.940,00 registrados.

## Tecnologias

- Python
- Pandas
- Matplotlib
- Jupyter Notebook / Google Colab
- Excel

## Estrutura

```text
quintal-do-zico-analise-vendas/
├── README.md
├── dados/
│   └── vendas_anonimizadas.csv
├── codigo/
│   └── analise_quintal_do_zico.py
└── graficos/
    ├── 01_quentinhas_por_dia.png
    ├── 02_faturamento_por_dia.png
    ├── 03_quentinhas_por_prato.png
    ├── 04_quentinhas_por_canal.png
    └── 05_faturamento_por_pagamento.png
```

## Privacidade

A versão disponibilizada para portfólio não contém nomes de clientes, endereços ou observações pessoais. Os dados foram anonimizados para fins de demonstração acadêmica.

## Aprendizados

O projeto permitiu aplicar, em uma situação real, conceitos de coleta, organização, tratamento, validação, análise exploratória e comunicação de dados. Também mostrou que uma solução simples pode transformar registros cotidianos em informações úteis para tomada de decisão.
