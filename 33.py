# pip install beautifulsoup4

# from bs4 import BeautifulSoup
# import re

# def get_copywriter(tag):
#     whois =tag.find('div', class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None

# f = open('index.html', encoding="utf-8").read()
# soup =BeautifulSoup(f, "html.parser")

# copywriter=[]
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw=get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)


# row = soup.find("div", class_="name") # find -вернет первый найденый элемент
# row = soup.find_all("div", class_="name") # find_all -возвращает все найденные элементы
# row = soup.find_all("div", class_="row")[1] # find_all -возвращает Только один блок
# row = soup.find_all("div", class_="row")[1].find("div", class_="links") # указывается элементы по цепочке
# row = soup.find("div", {'class': "name"})
# row = soup.find("div", {'data-set': "salary"}) # для ключей с дефисом
# alena = soup.find("div", text = "Alena")# находим Алену
# alena = soup.find("div", text = "Alena").parent # находим родительский элемент
# alena = soup.find("div", text = "Alena").parent.parent # находим родительский элемент
# alena = soup.find("div", text = "Alena").find_parent(class_="row")# находим родительский элемент c классом row
# row = soup.find("div", id = "whois3")
# row = soup.find("div", id = "whois3").find_next_sibling() # после найденого находим
# row = soup.find("div", id = "whois3").find_previous_sibling() # перед найденого находим
#
#
# print(row)


#
# def get_salary(s):
#     patter = r"\d+"
#     # res = re.findall(patter,s)[0] # или
#     res = re.search(patter,s)
#     print(res)
#
# f = open('index.html', encoding="utf-8").read()
# soup =BeautifulSoup(f, "html.parser")
# # row = soup.find('div', {"data-set": "salary"}).text
# row = soup.find_all('div', {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)

# import requests
#
# r= requests.get('https://ru.wordpress.org/')
# print(r.content)
# print(r.text)

# print(r.status_code)
# print(r.headers)
# print(r.headers['Content-Type'])


# import requests
# from bs4 import BeautifulSoup
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup=BeautifulSoup(html, "lxml")# html.parser или  с библиотекой lxml вот так
#     p1=soup.find("header", id="masthead").find("p", class_='site-title').text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ =='__main__':
#     main()


# import requests
# import csv
# from bs4 import BeautifulSoup
# import re
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter =";", lineterminator ="\r")
#         writer.writerow((data['name'], data["url"], data['rating']))
#
# def get_data(html):
#     soup=BeautifulSoup(html, "lxml")# html.parser или  с библиотекой lxml вот так
#     s=soup.find_all("section", class_="plugin-section")[1]
#     plugins =s.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r= refined(rating)
#         data ={'name': name, "url": url, 'rating': r}
#         write_csv(data)
#     # return len(plugins)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ =='__main__':
#     main()

# 17/02/2022

# import csv
# from bs4 import BeautifulSoup
# import requests
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["name"], data['url'], data['snippet'], data['active'], data['cv']))
#
#
# def refind_cv(s):
#     return s.split(" ")[-1]
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ''
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except ValueError:
#             snippet = ''
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ''
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cv = refind_cv(c)
#         except ValueError:
#             cv = ''
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cv': cv
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 5):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


from parse import Parser

def main():
    pars = Parser('https://www.ixbt.com/live/index/type/news/', "news.txt")
    pars.run()

if __name__ == '__main__':
    main()


