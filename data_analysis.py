import numpy as np
import pandas as pd
from pandas.core.common import flatten
import json

data_df = pd.read_csv("data.csv")


coaches_in_tier_n = dict()
coaches_in_tier_n[0] = ['Paul Brown']

all_coaches = set(data_df['name'])
f = open("Paul_Brown_numbers.json", "a")

print("Starting coaches: {}".format(len(all_coaches)))


for i in range(1,11):
    coach_name = []
    for j in coaches_in_tier_n[i-1]:
        coachs_team = data_df[data_df['name'] == j][['team', 'year']].values
        coachs_team = sorted(coachs_team, key = lambda x: x[1])
        for k in coachs_team:
            coach = data_df[(data_df['team'] == k[0]) & (data_df['year'] == k[1]) & (data_df['name'] != j)][['name']].values.tolist()
            coach_name.append(coach)
    subtraction_list = []
    for l in range(1,i):
        subtraction_list.extend(coaches_in_tier_n[i-l])
    coaches_in_tier_n[i] = list(set(flatten(coach_name)) - set(subtraction_list))
    all_coaches = all_coaches - set(flatten(coach_name))
    if len(coaches_in_tier_n[i]) == 0:
        coaches_in_tier_n['undefined'] = list(all_coaches)
        print("Coaches with no connections: {}".format(all_coaches))
        break

    print("coaches left: {}".format(len(all_coaches)))
    print("There are {} coaches in tier {}".format(len(coaches_in_tier_n[i]),i))


json_object = json.dumps(coaches_in_tier_n)
f.write(json_object)
f.close()