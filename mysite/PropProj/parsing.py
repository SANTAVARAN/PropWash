from bs4 import BeautifulSoup
import requests
def ParseSpecs(html):
    page=requests.get(html)
    soup = BeautifulSoup(page.text, 'html.parser')
    spec_name_list = soup.find(id='tab-id-2-container')
    spec_name_list_full=spec_name_list.find_all('ul')
    MaxVoltage=''
    Protocols=''
    for spec_name in spec_name_list_full:
        #print(spec_name.text)
        if spec_name.text.find('Input:')>0:
            MaxVoltage+=spec_name.text[spec_name.text.find('Input:')+14:spec_name.text.find('Input:')+18]
        if spec_name.text.find('Input voltage range:')>0:
            MaxVoltage+=spec_name.text[spec_name.text.find('Input voltage range:')+14:spec_name.text.find('Input voltage range:')+18]
        if spec_name.text.find('TR/SA')>0:
            Protocols+=spec_name.text[spec_name.text.find('TR/SA')+18:spec_name.text.find('TR/SA')+20]
    if len(MaxVoltage):
        MaxVoltage=MaxVoltage[MaxVoltage.find("S")-1:MaxVoltage.find("S")+1]
        print("MaxVoltage list is: ",MaxVoltage,"   =====>   ",spec_name.text[spec_name.text.find('Input:'):spec_name.text.find('Input:')+10])
    if len(Protocols):
        print("Protocols list is: ", Protocols)
    MaxVoltage=''
def ParseItems(html):
    page = requests.get(html)
    FCTestList=[]
    soup = BeautifulSoup(page.text, 'html.parser')
    part_name_list = soup.find_all(class_='grid-content')
    for part_name in part_name_list:
        print(part_name.text)
        if 'Полетный контроллер' or 'Flight Controller' in part_name.text:
            FCTestList.append(part_name.text)
            toHref = soup.find_all(class_='grid-entry-title entry-title')
            for result in toHref:
                tohref2=result.find('a')
                ParseSpecs(tohref2.attrs['href'])
    #print(FCTestList)

ParseItems('http://www.mateksys.com/?page_id=3834')
#ParseSpecs("http://www.mateksys.com/?portfolio=f722-px#tab-id-2")