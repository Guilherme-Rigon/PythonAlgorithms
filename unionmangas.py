#-*-coding:utf-8-*-
"""
@author: Guilherme Luiz Simões Rigon
"""
from bs4 import BeautifulSoup
import requests

page = 1
arquivo = open('MyAnimeList.txt','w', encoding = "utf-8")

while True:
	BaseURL = "https://unionleitor.top/lista-mangas/a-z/{0}/*".format(str(page))

	response = requests.get(BaseURL)

	bs = BeautifulSoup(response.text, 'lxml')

	mangaList = bs.find_all('div', class_='bloco-manga')

	if len(mangaList) == 0:
		#arquivo.close() #por algum motivo desconhecido até o momento ao passar por aqui o arquivo perde todo seu conteudo;
		break;

	VMangaList = []

	for manga in mangaList:
		VMangaList.append(manga.find_all('a')[1].text+' => '+manga.find_all('a')[0].get('href'))

	for manga in VMangaList: #For a mais usado para a visualização e inútil em um futuro código final;
		arquivo.writelines(manga+'\n')
		print(manga)
	page+=1

print("O ultimo mangá foi encontrado na página: "+str(page-1))