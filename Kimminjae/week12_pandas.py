import pandas as pd

df1 = pd.DataFrame({'a': [11, -2, 7],
                    'b': [9, 8, 77],
                    'c': [55, 33, 19]
                    }, index=[1, 2, 3])
df2 = pd.DataFrame([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
                   )

print(df1)
print(df2)
