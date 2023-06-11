import os
import time
import csv
import requests
from plyer import notification
from bs4 import BeautifulSoup
import chime

def main():
	clear()
	price()

def clear():
	if os.path.isfile("mods.txt"):
		os.remove("./mods.txt")

	os.system("cls||clear")
	print("remove mods: Done")
	chime.success()
	time.sleep(1)
	os.system("cls||clear")


def price():
	srep = input("Введите название мода(Оставьте поле пустым, если все): ")
	os.system("cls||clear")
	page = 1

	while True:
		response = requests.get(f"https://modrinth.com/mods?q={srep}&o={20*page-20}&g=categories:%27fabric%27&v=1.20")
		sopu = BeautifulSoup(response.content, "html.parser")
		items = sopu.select("div.search-results-container > div#search-results.project-list.display-mode--list > article.project-card.base-card.padding-bg")

		pagelist = sopu.select("div.columns.paginates.pagination-before > a.right-arrow.paginate.has-icon")
		#print(pagelist[0]["tabindex"])
		
		for mod in items:
			title = mod.select("div.title > a > h2.name")
			modslist = str(title[0].text.strip())
			#print(modslist)
			try:
				with open("mods.txt", "a") as MyFile:
					MyFile.write(modslist + "\n")
			except UnicodeEncodeError:
				pass
		print(f"Страница {page}: Done")
		page += 1

		if pagelist[0]["tabindex"] == "-1":
			os.system("cls||clear")
			print("DONE")
			done()
			break

def done():
	chime.success()
	notification.notify(message = 'Cбор данных: готов', app_name = 'script', title='Закончено')
	time.sleep(1)

main()