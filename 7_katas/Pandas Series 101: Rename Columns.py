# Rename Columns

# Input parameters

# pandas.DataFrame object
# sequence
# Task

# Your function must return a new pandas.DataFrame object with same data than the original input but now its column names are the elements of the sequence. You must not modify the original input.

# The number of columns of the input will always be equal to the size of the sequence.

# Examples

#    0  1  2
# 0  1  2  3
# 1  4  5  6

# names = ['A', 'B', 'C']
#    A  B  C
# 0  1  2  3
# 1  4  5  6


import pandas as pd

def rename_columns(df, names):  
    df_copy = df.copy()
    df_copy.columns = names
    return df_copy


df_input = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
names = ('A', 'B', 'C')
df_output = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('ABC'))
user_solution = rename_columns(df_input, names)
print(user_solution.head())


#even simpler 

import pandas as pd

def rename_columns(df, names):  
    return pd.DataFrame(data=df.values, columns=names)