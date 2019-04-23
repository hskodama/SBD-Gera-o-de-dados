import pickle
import random
import csv
import string
# a. RNE (ID) : Char(8) {chave primária}
# b. Nome : Varchar(40)
# c. Nome pai : Varchar(40)
# d. Nome mãe : Varchar(40)
# e. Nacionalidade : Char(3)
# f. Estado_mora : Char(2)
# g. Passaporte : Char(8)
# h. Data de expedição : Date
# i. Data de expiração : Date
# j. Órgão emissor : Varchar(20)
with open('data/RNE.data', 'rb') as rne:
    list_rne = pickle.load(rne) 
with open('names/names.txt', 'r') as name:
    names = [line.strip() for line in name]
with open('names/surname.txt', 'r') as surname:
    surnames = [line.strip() for line in surname]
with open('data/nacionalidade.data', 'rb') as nacionalidade:
    nacionalidades = pickle.load(nacionalidade)
with open('data/estados.data', 'rb') as estado:
    estados = pickle.load(estado)
with open('data/datas.data', 'rb') as data:
    datas = pickle.load(data)

with open('pessoa.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['RNE', 'nome', 'nome_pai', 'nome_mae', 'nacionalidade', 'estado_mora', 'passaporte', 'data_exped', 'data_expir'])

    for i in range(200000):
        data_emiss = random.choice(datas)
        aux_date = int(data_emiss[6]) * 1000 + int(data_emiss[7]) * 100 + int(data_emiss[8]) * 10 + int(data_emiss[9]) + 4
        data_exp = data_emiss[:-4] + str(aux_date)

        filewriter.writerow([random.choice(list_rne), random.choice(names) + " " + random.choice(surnames), random.choice(names) + " " + random.choice(surnames), random.choice(names) + " " + random.choice(surnames), random.choice(nacionalidades), random.choice(estados), random.choice(list_rne), data_emiss, data_exp])
# ########## PICKLE RNE ############
# with open('datas.data', 'rb') as f:
#     list = pickle.load(f)



########## NAMES ############

# with open('names/names.txt', 'r') as f:
#     myNames = [line.strip() for line in f]

# print(random.choice(myNames))


