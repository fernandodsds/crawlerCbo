#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
def readCSV():
    csv =  pd.read_csv('lista.csv', names=['codigo','descricao','tipo'])
    teste = csv
    print(teste)
    return (teste)
