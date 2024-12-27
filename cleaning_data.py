import pandas as pd
import re


teams_df = pd.read_csv('teams.csv', header=0)
preclean_data_df = pd.read_csv('preclean_data.csv', header=0, sep=r',(?![^{}]*\})', engine='python')

coach_name = []
coach_position = []

f = open("data.csv", "a")
f.write("name,position,record,team,year\n")


for i in preclean_data_df.index:
    coaches_data = preclean_data_df.loc[i,'Data'] = preclean_data_df.loc[i,'Data'].strip("{}")
    Data = re.split(r', (?=(?:"[^"]*?(?: [^"]*)*))|, (?=[^",]+(?:,|$))', coaches_data)
    team = preclean_data_df.loc[i,'Team']
    year = preclean_data_df.loc[i,'Year']
    for j in Data:
        string = j.replace("\"", "")
        if re.match(r"^Coach:\\n", string):
            match = re.search(r"Coach:\\n(.+?)\s\((\d+-\d+-\d+)\)", j)
            coach_name = match.group(1)
            coach_position = 'Head Coach'
            record = match.group(2)
            f.write("{coach_name},{coach_position},{record},{team},{year}\n".format(coach_name=coach_name,coach_position=coach_position,record=record,team=team,year=year))
        elif re.match(r"^Other Notable Asst.:", string):
            matches = re.findall(r"(\w+\s\w+)\s\(([^)]+)\)", string)
            for i in matches:
                f.write("{coach_name},{coach_position},{record},{team},{year}\n".format(coach_name=i[0],coach_position=i[1],record=record,team=team,year=year))
        elif re.match(r"^Defensive Coordinator:", string):
            match = re.search(r"Defensive Coordinator:\s(.+)", string)
            coach_name = match.group(1).split(", ")
            coach_position = 'Defensive Coordinator'
            for k in coach_name:
                f.write("{coach_name},{coach_position},{record},{team},{year}\n".format(coach_name=k,coach_position=coach_position,record=record,team=team,year=year))

        elif re.match(r"^Offensive Coordinator:", string):
            match = re.search(r"Offensive Coordinator:\s(.+)", string)
            coach_name = match.group(1).split(", ")
            coach_position = 'Offensive Coordinator'
            for k in coach_name:
                f.write("{coach_name},{coach_position},{record},{team},{year}\n".format(coach_name=k,coach_position=coach_position,record=record,team=team,year=year))
