import pandas as pd
import Levenshtein as lev

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


for i, data1 in enumerate(dataset1):
    district1 = data1["District"]
    
    matching_district = None
    kpi2 = None

    for j, data2 in enumerate(dataset2):
        district2 = data2["District"]
        kpi2 = data2["KPI_2"]

        if i == j:
            similarity_ratio = lev.ratio(district1, district2)
            if similarity_ratio > 0.8:
                data1["District"] = data2["District"]

    
df1 = pd.DataFrame(dataset1)
df2 = pd.DataFrame(dataset2)
    
  
df = pd.merge(df1, df2, on='District')
print(df)