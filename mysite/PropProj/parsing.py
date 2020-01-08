from bs4 import BeautifulSoup
import requests
def ParseItems(html):
    page = requests.get(html)
    soup = BeautifulSoup(page.text, 'html.parser')
    part_name_list = soup.find(class_='v_item-it')
    print("Trying to parse: ",html," ",part_name_list)
    part_name_list_items = part_name_list.find_all('a')
    for part_name in part_name_list_items:
        names = part_name.contents[0]
        print(names)
ParseItems('https://air-hobby.ru/katalog/category/52-poletnie-kontrolleri.html?limit=16&limitstart=0')