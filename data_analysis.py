import numpy as np
import pandas as pd
from pandas.core.common import flatten

data_df = pd.read_csv("data.csv")


coaches_in_tier_n = dict()
coaches_in_tier_n[0] = ['Paul Brown']

all_coaches = set(data_df['name'])
print("Starting coaches: {}".format(len(all_coaches)))

coach_name = []
for i in range(1,11):
    coach_name = []
    for j in coaches_in_tier_n[i-1]:
        coachs_team = data_df[data_df['name'] == j][['team', 'year']].values
        coachs_team = sorted(coachs_team, key = lambda x: x[1])
        for k in coachs_team:
            coach = data_df[(data_df['team'] == k[0]) & (data_df['year'] == k[1]) & (data_df['name'] != j)][['name']].values.tolist()
            coach_name.append(coach)
    coaches_in_tier_n[i] = list(set(flatten(coach_name)))
    all_coaches = all_coaches - set(flatten(coach_name))
    if coaches_in_tier_n[i] == coaches_in_tier_n[i-1]:
        coaches_in_tier_n['undefined'] = all_coaches
        print("Coaches with no connections: {}".format(all_coaches))
        break
    print("coaches left: {}".format(len(all_coaches)))
    print("There are {} coaches in tier {}".format(len(coaches_in_tier_n[i]),i))
