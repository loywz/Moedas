import re
import threading

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

def requisicao(url):
    resposta_html = requests.get(url, headers=headers)
    return resposta_html.text
    

def parsing(resposta_html):
    soup = BeautifulSoup(resposta_html, 'html.parser')
    return soup


def valorMoeda(soup):
    soup = soup.findAll("span", class_="DFlfde SwHCTb")[0]
    return soup
print('-'*50)
print("Euro, Dolar, Dolar Canadense, Bitcoin")
print('-'*50)
escolha = input("Escreva uma moeda para saber o valor: ")
try:
    if escolha == "Dolar":
        resposta = requisicao("https://www.google.com/search?q=dolar+hoje&rlz=1C1GCEA_enBR942BR942&oq=dola&aqs=chrome.0.69i59l3j0i131i433j69i57j0i131i433j0i433j0i131i433j0i433l2.1319j1j7&sourceid=chrome&ie=UTF-8")
        soup = parsing(resposta)
        resultado = valorMoeda(soup)
        print('-'*50)
        print("1 Real Brasileiro = {} Dolares".format(resultado.text))
        print('-'*50)

    elif escolha == "Euro":
        resposta = requisicao("https://www.google.com/search?q=euro+hoje&rlz=1C1GCEA_enBR942BR942&oq=dola&aqs=chrome.0.69i59l3j0i131i433j69i57j0i131i433j0i433j0i131i433j0i433l2.1319j1j7&sourceid=chrome&ie=UTF-8")
        soup = parsing(resposta)
        resultado = valorMoeda(soup)
        print('-'*50)
        print("1 Real Brasileiro = {} Euros".format(resultado.text))
        print('-'*50)

    elif escolha == "Dolar canadense":
        resposta = requisicao("https://www.google.com/search?q=cad+hoje&rlz=1C1GCEA_enBR942BR942&oq=dola&aqs=chrome.0.69i59l3j0i131i433j69i57j0i131i433j0i433j0i131i433j0i433l2.1319j1j7&sourceid=chrome&ie=UTF-8")
        soup = parsing(resposta)
        resultado = valorMoeda(soup)
        print('-'*50)
        print("1 Real Brasileiro = {} Dolares Canadenses ".format(resultado.text))
        print('-'*50)

    elif escolha == "Bitcoin":
        resposta = requisicao("https://www.google.com/search?q=bitcoin+hoje&rlz=1C1GCEA_enBR942BR942&oq=dola&aqs=chrome.0.69i59l3j0i131i433j69i57j0i131i433j0i433j0i131i433j0i433l2.1319j1j7&sourceid=chrome&ie=UTF-8")
        soup = parsing(resposta)
        resultado = valorMoeda(soup)
        print('-'*50)
        print("1 Real Brasileiro = {} Bitcoins ".format(resultado.text))
        print('-'*50)

    else:
        print("Escolha invalida")
except:
    print("Moeda não encontrada")
