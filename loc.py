import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], 
                  index = ['cobra', 'viper', 'sidewinder'], 
                  columns = ['max_speed', 'shield'])

print(df)
print()
print(df.loc['viper'])
print()
print(df.loc[['cobra', 'viper']])
print()
print(df.loc[['viper', 'cobra']])
print()
print(df.loc['cobra':'viper', ['max_speed', 'shield']])