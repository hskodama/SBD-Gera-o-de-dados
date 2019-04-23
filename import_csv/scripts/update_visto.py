import random
import pandas as pd
import numpy as np
records_visto = pd.read_csv('../csv/visto.csv')
records_pessoa = pd.read_csv('../csv/pessoa_reduced.csv')

records_visto['RNE'] = records_pessoa['RNE'].values
records_visto['classificacao'] = np.random.randint(1, 13, records_visto.shape[0])
records_visto.to_csv('../csv/visto_updated.csv', index=False)