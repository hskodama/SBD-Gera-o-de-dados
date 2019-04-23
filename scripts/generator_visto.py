import pickle
import random
import csv
import string
from datetime import timedelta  
from datetime import datetime
import pandas as pd

# a. RNE : Char(8) {Chave estrangeira}
# b. Classificação (tipo do visto) : Int {Chave estrangeira}
# c. Data de expedição : Date
# d. Data de expiração : Date
# e. Data de entrada : Date
records = pd.read_csv('../csv/pessoa_deduped.csv')

with open('../data/datas.data', 'rb') as data:
    datas = pickle.load(data)

with open('../csv/visto.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['RNE', 'classificacao', 'data_exped', 'data_expir', 'data_entr'])

    for i in range(170000):
        data_emiss = random.choice(datas)
        aux_date = int(data_emiss[6]) * 1000 + int(data_emiss[7]) * 100 + int(data_emiss[8]) * 10 + int(data_emiss[9])
        data_entr = datetime.strptime(data_emiss, '%m/%d/%Y')
        data_entr = data_entr + timedelta(days=random.randint(1,70))
        data_entr = data_entr.date()

        filewriter.writerow(["", "", data_emiss, "", data_entr])
# # ########## PICKLE RNE ############
# # with open('datas.data', 'rb') as f:
# #     list = pickle.load(f)



# ########## NAMES ############

# # with open('names/names.txt', 'r') as f:
# #     myNames = [line.strip() for line in f]

# # print(random.choice(myNames))


