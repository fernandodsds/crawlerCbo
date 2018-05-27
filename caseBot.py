#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from writeDatabase import insereEmCBO
from datasetRead import readCSV
cbos = readCSV()
logging.basicConfig(filename='crawler.log', level=logging.INFO)

print('0 de '+str(len(cbos))+' a serem verificados')
contador = 0
for cboType,cboCod in zip(cbos['tipo'],cbos['codigo']):
    if(cboType != "Sinônimo"):
        insereEmCBO(cboCod.replace("-", ""))
        contador = contador+1
        print('\033[32m'+str(contador) +' de '+str(len(cbos))+' a serem verificados \033[0;0m')
        logging.info(str(contador) +' de '+str(len(cbos))+' a serem verificados')

    else:
        contador = contador+1
        print('\033[31m'+str(contador) +' de '+str(len(cbos))+' a serem verificados - '+cboCod+' NAO INSERIDO POR SER SINONIMO \033[0;0m')
        logging.info(str(contador) +' de '+str(len(cbos))+' a serem verificados - '+cboCod+' NAO INSERIDO POR SER SINONIMO')
