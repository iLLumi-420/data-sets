import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

data1 = {
    'District': ['Kathmandu', 'Kavre palanchowk', 'Dhanusa'],
    'KPI_1' : [ .8, .75, .85]
}

data2 = {
    'District': ['Kathmandu', 'Kavrepalanchowk', 'Dhanusha'],
    'KPI_2' : [.35, .65, .6]
}

dataset1 = pd.DataFrame(data1)

dataset2 = pd.DataFrame(data2)

def find_best_match(distict, district_list):
    return process.extractOne(distict, district_list, scorer=fuzz.ratio)[0]

dataset1['District'] = dataset1['District'].apply(lambda x: find_best_match(x, dataset2['District']) )


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

