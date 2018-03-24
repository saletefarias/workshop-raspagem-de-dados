# workshop-raspagem-de-dados
Scripts utilizados no workshop do dia 24-03-18
## Raspagem de dados Web  Python @UNDB
Workshop reallizado durante a Semana de Inovação 2018 na UNDB

## O que é
A **raspagem de dados** (_data scraping_) é uma técnica computacional de coleta automatizada de dados. 

## Pré-requisitos
- Instalação do [Python 3](https://www.python.org/download/releases/3.0/)

- Instalação das bibliotecas. A partir do terminal de comando execute:
```
pip install beautifulsoup4 requests numpy scipy matplotlib
ou
pip3 install beautifulsoup4 requests numpy scipy matplotlib 

Recomendamos instalar o jupyter notebook para eventuais demonstrações
pip install jupyter
ou
pip3 install jupyter
```

*** O pip é o gerenciador de pacotes do Python.

Para os scripts que usaremos durante o workshop a instalação do `beautifulsoup4` é suficiente. `numpy`, `scipy` e `matplotlib` serão utilizadas apenas em exemplos mais avançados que envolvem visualização de dados e não serão abordados durante a apresentação devido ao tempo.

Para garantir que a instalação foi realizada com sucesso, abra o console Python, faça a importação da biblioteca e chame pela classe `BeautifulSoup`:

```
>>> from bs4 import BeautifulSoup
>>> BeautifulSoup
<class 'bs4.BeautifulSoup'>
```

## Exemplos de projetos que fazem uso de raspagem de dados:
- [Operação Serenata de Amor](https://serenatadeamor.org/)
- [SACSP](https://sacsp.mamulti.com/)

## Para saber mais:
- [Repositório de treinamento do Masanori](https://github.com/fmasanori/treinamento)
- [Livro Web Scraping com Python](https://novatec.com.br/livros/web-scraping-com-python/)

### Nossa equipe:
* Ana Clara Cavalcante ([anaclaracavalcante14@gmail.com])
* Meyrianne Martins ([meirymartinsp.rodrigues@gmail.com])
* Salete Farias ([@saletefarias][saletefarias@gmail.com])
