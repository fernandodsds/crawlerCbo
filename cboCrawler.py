# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import unicodedata
import requests
def scrapper(cod):
    cod = str(cod)
    r  = requests.get("http://www.ocupacoes.com.br/cbo-mte/"+cod)

    data = r.text#.index('<h2>','</div>>')

    soup = BeautifulSoup(data,"html.parser")
    pageSplit = {'codigo': cod}
    lists = soup.findAll('h4')

    for list in lists:
        item = {}
        uls = []
        item.update({list.next:[]})
        for nextSibling in list.findNextSiblings():
            if nextSibling.name == 'h4':
                break
            if nextSibling.name == 'ul':
                uls = nextSibling
                tagLi  =  uls.findAll('li')
                [item[list.next].append(x.get_text()) for x in tagLi]
                pageSplit.update(item)

    topics = soup.findAll('h2')
    if(len(topics)>=2):
        pageSplit.update({'titulo':topics[0].next})
        for i in range(1,len(topics)):
            pageSplit.update({topics[i].next:topics[i].next.next})
        return(pageSplit)
    else:
        return (-1)
