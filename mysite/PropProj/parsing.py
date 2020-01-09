from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('/Users/arsenijsitnickij/Documents/SHP/PropWash/git/mysite/db.sqlite3')
c = conn.cursor()
def add_part(partname,type,ImageUrl):
    c.execute("INSERT INTO PropProj_part (Name,Type,ImageUrl) VALUES ('%s','%s')"%(partname,type,ImageUrl))
    conn.commit()
def add_part_spec(partid,value):
    c.execute("INSERT INTO PropProj_partspecs (PartID_id,value,SpecID_id) VALUES ('%s','%s','%s')"%(partid,value,4))
    conn.commit()
def ParseSpecs(html):
    page = requests.get(html)
    soup = BeautifulSoup(page.text, 'html.parser')
    spec_name_list = soup.find(class_='p__article')
    spec_name_list_full = spec_name_list.find_all('li')
    #print(spec_name_list.text)

    MaxCurrent = ''
    PeakCurrent=''
    OutputData=['','']
    for spec_name in spec_name_list_full:
        # print(spec_name.text)
        if spec_name.text.count('Рабочий ток:') > 0:
            MaxCurrent += spec_name.text[spec_name.text.find('Рабочий ток:') :spec_name.text.find('Рабочий ток:') + 19]
        if spec_name.text.count('Максимальный ток:') > 0:
            PeakCurrent += spec_name.text[spec_name.text.find('Максимальный ток:') + 17:spec_name.text.find('Максимальный ток:') + 25]
    print(html)
    if len(MaxCurrent):
        MaxCurrent = MaxCurrent[MaxCurrent.find("А") - 5:MaxCurrent.find("А")-1 ]
        print("Maxcurrent: ", MaxCurrent)
        OutputData[0]=MaxCurrent
    else:
        MaxCurrent="-"
        OutputData[0]=MaxCurrent
        print("Maxcurrent: ", MaxCurrent)
    if len(PeakCurrent):
        print("PeakCurrent: ", PeakCurrent)
        OutputData[1] = PeakCurrent
    else:
        PeakCurrent="No"
        print("PeakCurrent: ", PeakCurrent)
        OutputData[1] = PeakCurrent
    MaxCurrent = ''
    #return (OutputData)
def ParseItems(html):
    page = requests.get(html)
    FCTestList = []
    soup = BeautifulSoup(page.text, 'html.parser')
    part_name_list = soup.find(class_='vmBrowse clearfix overflow')
    part_name_list_full=part_name_list.find_all('a')
    #print(soup.find_all('a'))
    #part_name_list = soup.find_all('div', {'class': ["vmBrowse", "clearfix", "overflow"]})
    #print(part_name_list)
    part_name_list_full = part_name_list.find_all('a')
    img_name_list_full=part_name_list.find_all_next('img')
    images=[]
    for img_name in img_name_list_full:
        img = img_name.attrs['src']
        img="air-hobby.ru"+img
        images.append(img)
    i=0
    for part_name in part_name_list_full:
        if 'Регулятор' or 'Flight Controller' in part_name.text:
            FCTestList.append(part_name.text)
            sliced=part_name.text.replace("отзывов","")
            sliced = sliced.replace("отзыва", "")
            sliced = sliced.replace("отзыв", "")
            sliced=sliced[:len(sliced)-2]
            #print(sliced)
            #if len(sliced)>0:
                #add_part(sliced,"ESC")
            toHref = part_name.attrs['href']
            toHref="https://air-hobby.ru"+toHref
            add_part(FCTestList[i],"FC",images[i])
            #print(ParseSpecs(toHref))
            #add_part(sliced,"motor")
        i+=1


    #print(FCTestList)


ParseItems('https://air-hobby.ru/katalog/category/51-motori.html')
#ParseSpecs("http://www.mateksys.com/?portfolio=f411-wing")
#ParseSpecs("http://www.mateksys.com/?portfolio=f722-std#tab-id-2")