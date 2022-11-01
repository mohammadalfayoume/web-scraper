from xml.sax.handler import all_properties
import requests # pip install requests
from bs4 import BeautifulSoup # to parse the data and search about data
from pprint import pprint

URL='https://en.wikipedia.org/wiki/The_Big_Bang_Theory'

page= requests.get(URL) # get all of the content of the web page (bytes)
# print(page.content)

soup= BeautifulSoup(page.content, 'html.parser') # convert data from bytes to html
# pprint(soup)

all_sup=soup.find_all('sup',class_='noprint')
def get_citations_needed_count():
    
    cout=0
    for span in all_sup:
        sup= span.find('span').text
        if sup == 'citation needed':
            cout+=1
    return cout

def get_citations_needed_report():
    list=[]
    for span in all_sup:
        sup= span.find('span').text
        if sup == 'citation needed': 
            p= span.find('span').parent.parent.parent.parent.text
            list.append(p)
    return list

counts=get_citations_needed_count()
all_paragraphs=get_citations_needed_report()
def results():
    print("The number of Citation needed in the The Big Bang Theory wikipedia is "+str(counts),'\n')
    n=1
    for p in all_paragraphs:
        print(str(n) +'- Citation needed for '+"\""+ p +"\"",'\n')
        n+=1
        
results()
    
    