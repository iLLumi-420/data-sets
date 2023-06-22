import pandas as pd

data1 = {
    'District': ['Kathmandu', 'Kavrepalanchowk', 'Dhanusa'],
    'KPI_1' : [0.8, 0.75, 0.85]
}

data2 = {
    'District': ['Kathmandu', 'Kavrepalanchowk', 'Dhanusa'],
    'KPI_2' : [0.35, 0.65, 0.6]
}

dataset1 = pd.DataFrame(data1)

dataset2 = pd.DataFrame(data2)

merged_dataset = pd.merge(dataset1, dataset2, on='District')
print(merged_dataset)









# District | KPI_1
# Kathmandu | .8
# Kavre palanchowk | .75
# Dhanusa | .85

# District | KPI_2
# Kathmandu | .35
# Kavrepalanchowk | .65
# Dhanusha | .6

