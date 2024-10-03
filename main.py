import pandas as pd
import numpy as np

#extramiles
import re

filepath = '/Users/jasonhardjawidjaja/desktop/Data Science/Week4Assignment/data.csv'

df = pd.read_csv(filepath)

#1
print(df.head())

print(df.tail())

df.info()

print(df.describe())

#2
print(df.isnull().sum())

#3
pd.set_option("display.max_rows", 100)

#4
df.rename(columns={"data": "Year", "Quarter": "Number of Workers (in thousands) - Total"}, inplace=True)

#5
df.index.name = "Custom Index Name"
df.index = range(1, len(df) + 1)

#6
df_melted = df.melt(id_vars=["Year"], value_vars=["Number of Workers (in thousands) - Total"],
                    var_name="Measurement", value_name="Value")
print(df_melted)

df_pivoted = df_melted.pivot_table(index='Year', columns='Measurement', values='Value', aggfunc='mean').reset_index()
print(df_pivoted)


#7
df2 = pd.DataFrame({
    "Year": [2019, 2020, 2021, 2022],
    "Additional Info": ["Info1", "Info2", "Info3", "Info4"]
})
df_merged = df.merge(df2, on='Year', how='left')
print(df_merged)

df_concatenated = pd.concat([df, df2], axis=1)
print(df_concatenated)

#8
df['Year'] = df['Year'].apply(lambda x: int(x) + 1)  # Increment year by 1
df_transformed = df.apply(lambda col: col.map(lambda x: str(x).upper() if isinstance(x, str) else x))
print(df_transformed)

#14 & 15
df['Number of Workers (in thousands) - Total'] = df['Number of Workers (in thousands) - Total'].astype(str).apply(
    lambda x: re.sub(r'\W+', '', x) if pd.notnull(x) else x)


