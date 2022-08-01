from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import re
from _datetime import datetime


def gera_planilha(dados: list, arquivo: str):
    # Criando DataFrame
    dataset = pd.DataFrame(dados)

    # Gerando arquivo excel
    dataset.to_excel(arquivo, index=False)


def coleta_links(lista: list) -> list:
    try:
        link_list: list = []
        compie = re.compile('https://')
        for item in lista:
            if compie.match(str(item.get('href'))):
                link: dict = {'Link': item.get('href'), 'Hora_Acesso': datetime.now().isoformat()[11:19]}
                link_list.append(link)

        return link_list

    except Exception:
        raise


def acessa_link(url: str) -> list:
    try:
        # User agent
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 /'
                                '(KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.71'}

        # Request
        req = Request(url, headers=header)
        response = urlopen(req)
        html = response.read()

        #Objeto Soup
        soup = BeautifulSoup(html, 'html.parser')
        return soup.findAll('a')
    except Exception:
        raise


def get_links(url: str, depth: int, name: str):
    try:
        lista_comparativa: list = []
        lista_links: list = []
        for i in range(depth + 1):
            if len(lista_links) == 0:
                lista_links += coleta_links(acessa_link(url))
            else:
                lista_iterate: list = []
                iterador: list = []
                # Separando links que ainda não foram acessados
                for item_lista in lista_links:
                    if item_lista not in lista_comparativa:
                        iterador.append(item_lista)
                # Acessando os links e inserindo-os na lista
                for item in iterador:
                    lista_iterate += coleta_links(acessa_link(item['Link']))
                lista_comparativa = lista_links.copy()
                lista_links += lista_iterate
        # Chamando método para gerar a planilha
        gera_planilha(lista_links, arquivo=name)

    except HTTPError as e:
        print(e.status, e.reason)

    except URLError as e:
        print(e.reason)

    except PermissionError as e:
        print("Erro ao acessar o arquivo: " + e.filename)
        print("Verifique se possui permissão para gerar/acessar o arquivo ou se ele está aberto")

    finally:
        print("Processo finalizado!")

if __name__ == '__main__':
    get_links('https://www.google.com/search?client=opera&q=Robert+Mitchum&sourceid=opera&ie=UTF-8&oe=UTF-8',
              depth=1,
              name='links.xlsx')
