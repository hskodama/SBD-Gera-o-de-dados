import pandas as pd
records = pd.read_csv('../csv/pessoa_deduped.csv')
reduced = records[:170000]
reduced.to_csv('../csv/pessoa_reduced.csv', index=False)