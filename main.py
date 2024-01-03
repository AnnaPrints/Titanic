#%%
from pathlib import Path

import pandas as pd
titanic_df = pd.read_csv(Path().joinpath('data', 'titanic.csv'))
titanic_tt = pd.read_csv(Path().joinpath('data', 'titanic.csv'))