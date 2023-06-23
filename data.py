import pandas as pd
from difflib import get_close_matches

dataset1 = [
    {"District": "Kathmandu", "KPI_1": 0.8},
    {"District": "Kavre palanchowk", "KPI_1": 0.75},
    {"District": "Dhanusa", "KPI_1": 0.85}
]

dataset2 = [
    {"District": "Kathmandu", "KPI_2": 0.35},
    {"District": "Kavrepalanchowk", "KPI_2": 0.65},
    {"District": "Dhanusha", "KPI_2": 0.6}
]

df1 = pd.DataFrame(dataset1)
df2 = pd.DataFrame(dataset2)

def find_closest_match(word, choices):
    matches = get_close_matches(word, choices)
    return matches[0] if matches else None

districts2 = df2['District'].to_list()

df1['District'] = df2["District"].apply(lambda x: find_closest_match(x, districts2))    
    
  
df = pd.merge(df1, df2, on='District')
print(df)