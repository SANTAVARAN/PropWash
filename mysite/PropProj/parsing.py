from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('/Users/arsenijsitnickij/Documents/SHP/PropWash/git/mysite/db.sqlite3')
c = conn.cursor()
def add_part(partname,type):
    c.execute("INSERT INTO PropProj_part (Name,Type) VALUES ('%s','%s')"%(partname,type))
    conn.commit()
def add_part_spec(partid,value):
    c.execute("INSERT INTO PropProj_partspecs (PartID_id,value,SpecID_id) VALUES ('%s','%s','%s')"%(partid,value,4))
    conn.commit()
def ParseSpecs(html):
    page = requests.get(html)
    soup = BeautifulSoup(page.text, 'html.parser')
    spec_name_list = soup.find(id='tab-id-2-container')
    spec_name_list_full = spec_name_list.find_all('ul')
    #print(spec_name_list.text)

    MaxVoltage = ''
    Protocols = ''
    OutputData=['','']
    for spec_name in spec_name_list_full:
        # print(spec_name.text)
        if spec_name.text.count('Input:') > 0:
            MaxVoltage += spec_name.text[spec_name.text.find('Input:') + 14:spec_name.text.find('Input:') + 18]
        if spec_name.text.count('Input voltage range:') > 0:
            pos = spec_name.text.find('Input voltage range:')
            #print("I found pos, its ", pos)
            #print("Slice is", spec_name.text[pos + 20:pos + 40])
            MaxVoltage += spec_name.text[pos + 20:pos + 40]
        if spec_name.text.count('TR/SA') > 0:
            Protocols += spec_name.text[spec_name.text.find('TR/SA') + 18:spec_name.text.find('TR/SA') + 23]
        if spec_name.text.count('Smartaudio & Tramp VTX protocol:') > 0:
            Protocols += spec_name.text[spec_name.text.find('Smartaudio & Tramp VTX protocol:') +33:spec_name.text.find('Smartaudio & Tramp VTX protocol:') + 36]

    if len(MaxVoltage) and MaxVoltage.find("S") > -1:
        MaxVoltage = MaxVoltage[MaxVoltage.find("S") - 1:MaxVoltage.find("S") + 1]
        OutputData[0]=MaxVoltage
    else:
        MaxVoltage="-"
        OutputData[0]=MaxVoltage
    if len(Protocols):
        print("Is TR/SA supported?: ", Protocols)
        OutputData[1] = Protocols
    else:
        Protocols="No"
        print("Is TR/SA supported?: ", Protocols)
        OutputData[1] = Protocols
    MaxVoltage = ''
    return (OutputData)
def ParseItems(html):
    page = requests.get(html)
    FCTestList = []
    soup = BeautifulSoup(page.text, 'html.parser')
    part_name_list = soup.find_all(class_='grid-content')
    for part_name in part_name_list:

        if 'Полетный контроллер' or 'Flight Controller' in part_name.text:
            FCTestList.append(part_name.text)
    toHref = soup.find_all(class_='grid-entry-title entry-title')
    i=12
    for result in toHref:
        tohref2 = result.find('a')
        print()
        #add_part(FCTestList[i],"FC")

        add_part_spec(i,ParseSpecs(tohref2.attrs['href'])[1])
        print(tohref2.attrs['href'])
        print()
        i += 1


    #print(FCTestList)


ParseItems('http://www.mateksys.com/?page_id=3834')
#ParseSpecs("http://www.mateksys.com/?portfolio=f411-wing")
#ParseSpecs("http://www.mateksys.com/?portfolio=f722-std#tab-id-2")