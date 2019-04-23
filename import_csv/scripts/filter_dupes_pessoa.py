import pandas as pd
records = pd.read_csv('pessoa.csv')
deduped = records.drop_duplicates(['RNE'])
deduped.to_csv('../csv/pessoa_deduped.csv', index=False)