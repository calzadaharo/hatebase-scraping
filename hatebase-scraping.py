#!/home/rodrigo/yes/bin/python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

file = open("/home/rodrigo/Documentos/paper/hatebase-scraping/hateful-lexicon-ge.csv", "w")

for i in range(1,3):
    url = "https://hatebase.org/search_results/language_id=deu%7Cpage=1"+str(i)

    html_doc = urlopen(url).read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.table

    for i in table.find_all('a'):
        if (i.string != "(Recent)"):
            file.write(i.string + os.linesep)

file.close()
