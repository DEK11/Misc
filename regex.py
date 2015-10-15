from bs4 import BeautifulSoup
import re

data = open("Report123.html",'r').read()
soup = BeautifulSoup(data)
tr_list = soup.table.findAll("tr")

head = True

for tr in tr_list:
	if head:
		head = False
		continue
	td = tr.findAll("td")[12]
	dates = re.findall(r'\d{1,2} {0,1}-[a-zA-Z0-9]{2,4}- {0,1}\d{2}', str(td))
	
	#dates = re.findall(r'\d{1,2} -[a-zA-Z]{3}-\d{2}', str(td))

	for date in dates:
		tag = soup.new_tag("td")
		tag.string = date
		tr.append(tag)

html = soup.prettify(soup.original_encoding)
with open("output.html", "wb") as file:
    file.write(bytes(html, 'UTF-8'))
