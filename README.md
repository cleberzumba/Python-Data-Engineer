# Python-Data-Engineer
Análise de dados e visualizações de gráficos.

O objetivo final é mostrar métricas específicas em algumas visualizações de gráficos. Um Dataset em formato CSV contém dados de candidatos que participaram dos processos seletivos (dados simulados) de uma empresa, e terá que fazer algumas análises e manipulações em cima desses dados.

Criei uma aplicação em Python para migrar os dados para um banco de dados relacional. O banco de dados que escolhi foi o PostreSQL que eu mesmo instalei, configurei, criei o banco de dados e criei o usuário do banco. Além disso, fiz análises e manipulações nos dados e mostrei esses dados do banco de dados em visualizações de gráficos; Então, esses dados irão ser armazenados em um banco de dados e os relatórios irão vir do banco de dados, não do arquivo CSV.

As visualizações são as seguintes:

- Contratações por tecnologia (gráfico de pizza)
- Contratações por ano (gráfico de barras horizontal)
- Contratações por antiguidade (gráfico de barras)
- Contratações por país ao longo dos anos (apenas EUA, Brasil, Colômbia e Equador) (gráfico multilinha)


## Tecnologias

Tecnologias que utilizei:

- Python
- Jupiter Notebook
- Banco de dados PostgreSQL


## Dados

Tenho 50 mil linhas de dados sobre candidatos. Os campos que estou usando são:

- First Name
- Last Name
- Email
- Country
- Application Date
- Yoe (years of experience)
- Seniority
- Technology
- Code Challenge Score
- Technical Interview


**Todos os dados aqui são totalmente falsos!!!**

**aqui fiz o trabalho de DBA, Engenheiro de Dados e Analista de Dados.**
