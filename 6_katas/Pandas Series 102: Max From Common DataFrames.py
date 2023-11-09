# Max From Common DataFrames

# Input parameters

# Two pandas.DataFrame objects

# Task

# Your function must return a new pandas.DataFrame with the same data and columns from the first parameter. For common columns in both inputs you must return the greater value of each cell for that column.

# You must not modify the original inputs.

# Input DataFrame will never be empty. The number rows of both inputs will be the same.

# Examples

# Inputs

#    A    B    C
# 0  2.5  2.0  2.0
# 1  2.0  2.0  2.0
#    C    B    D    E
# 0  1.0  6.0  7.0  1.0
# 1  8.5  1.0  9.0  1.0
# Output

#    A    B    C
# 0  2.5  6.0  2.0
# 1  2.0  2.0  8.5
# Hint: Use pandas methods



import pandas as pd

def max_common(df_a, df_b):
    # Create a new DataFrame to hold the merged and max values
    merged_max_df = pd.DataFrame()

    # Iterate over columns in df_a
    for col in df_a.columns:
        # Check if the column exists in both DataFrames
        if col in df_b.columns:
            take_larger = lambda s1, s2: s1 if s1.sum() > s2.sum() else s2
            # Use the max function to get the greater value for each cell
            merged_max_df[col] = df_a[col].combine(df_b[col], take_larger)
            #merged_max_df[col] = df_a[col].combine(df_b[col], max)
        elif col in df_b.columns and df_b[col].empty:
            merged_max_df[col] = df_b[col]
        else:
            # If the column only exists in df_a, add it to the new DataFrame
            merged_max_df[col] = df_a[col]
        

    return merged_max_df




df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
df1.combine(df2, take_smaller)


# shorter

# def max_common(df_a, df_b):
#     return pd.concat([df_a, df_b]).filter(items=df_a.columns).groupby(level=0).max()

# or

# def max_common(df_a, df_b): 
#     df_c = pd.concat([df_a, df_b])[df_a.columns]
#     return df_c.groupby(df_c.index).max()