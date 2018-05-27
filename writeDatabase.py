from pymongo import MongoClient
from cboCrawler import scrapper
import logging
def insereEmCBO(cod):
    cliente = MongoClient('localhost', 27017)
    banco = cliente.admin
    cbos = banco.CBO
    cboInfo = scrapper(cod)
    if cboInfo == -1:
        print("CBO Errado")
    else:
        cbo = cbos.insert_one(cboInfo).inserted_id
        print('\033[33m'+str(cbo)+": "+"Inserido CBO "+cod+'\033[0;0m')
        logging.info(str(cbo)+": "+"Inserido CBO "+cod)
